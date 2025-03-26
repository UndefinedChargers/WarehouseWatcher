# FILE :main.py
# PROJECT :Warehouse Watcher
# PROGRAMMER : Amel Korandippillil Sunil
# DESCRIPTION :This file basically contain the intial setup of the UI

import json
import customtkinter as ctk
import threading
from dotenv import load_dotenv
import os
from .Sensor_logic import on_off_battery_switch,adjust_data_one
from .mqtt_handler import MQTTHandler


FIELDS_PER_SENSOR = {
    "Room": ["Data"],
    "Refrigerator": ["Data"],
    "Freezer": ["Data"],
    "AirQuality_warehouse": ["PM2.5","CO2", "VOC"],
    "humidity_warehouse": ["Humidity"]
}

class SimulatorUI(ctk.CTk):
    def __init__(self, sensor_names):
        super().__init__()
        self.title("Warehouse Watcher Simulator UI")
        self.geometry("1050x650")
        self.iconbitmap("./assets/favicon.ico")
        self.sensor_configs = {}
        self.sensor_names = sensor_names
        self.mqtt_handler = None
        self.left_sensor_labels = {}
        self.setup_UI(sensor_names)
        
    # function name:setup_UI
    # Description:This function is used to set up of the setup_UI
    # Parameter:sensor_names
    # return:
    def setup_UI(self, sensor_names):
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(expand=True, fill="both", padx=10, pady=10)

        self.connection_frame = ctk.CTkFrame(self.main_frame)
        self.connection_frame.pack(expand=True)

        self.config_frame = ctk.CTkFrame(self.main_frame)
        self.config_frame.pack(expand=True, fill="both")
        self.config_frame.pack_forget()

        self.setup_connection_frame()
        self.configration_tab(sensor_names)
        
    # function name:setup_connection_frame
    # Description:This function is used to get the setup_connection_frame  for the UI simulator
    # Parameter: void:self
    # return:
    def setup_connection_frame(self):
        frame = self.connection_frame

        inner_frame = ctk.CTkFrame(frame, corner_radius=10)
        inner_frame.pack(expand=True)

        ctk.CTkLabel(inner_frame, text="Cloud Host URL:", font=("Arial", 13)).pack(pady=(20, 5))
        self.host_entry = ctk.CTkEntry(inner_frame, width=400)
        self.host_entry.pack(pady=5)

        ctk.CTkLabel(inner_frame, text="Username:", font=("Arial", 13)).pack(pady=5)
        self.user_entry = ctk.CTkEntry(inner_frame, width=400)
        self.user_entry.pack(pady=5)

        ctk.CTkLabel(inner_frame, text="Password:", font=("Arial", 13)).pack(pady=5)
        self.pass_entry = ctk.CTkEntry(inner_frame, width=400, show="*")
        self.pass_entry.pack(pady=5)

        load_btn = ctk.CTkButton(inner_frame, text="Load from .env", command=self.load_env_credentials)
        load_btn.pack(pady=(15, 5))

        self.connect_btn = ctk.CTkButton(inner_frame, text="Connect", command=self.connect_to_mqtt)
        self.connect_btn.pack(pady=10)

        self.conn_status_label = ctk.CTkLabel(inner_frame, text="", font=("Arial", 12), text_color="grey")
        self.conn_status_label.pack(pady=(5, 10))

    # function name:load_env_credentials
    # Description:This function is used to load the credential into the login in functionality
    # Parameter: void:self
    # return:
    def load_env_credentials(self):
        load_dotenv()
        self.host_entry.delete(0, "end")
        self.user_entry.delete(0, "end")
        self.pass_entry.delete(0, "end")
        self.host_entry.insert(0, os.getenv("HIVEMQ_HOST", ""))
        self.user_entry.insert(0, os.getenv("HIVEMQ_USER", ""))
        self.pass_entry.insert(0, os.getenv("HIVEMQ_PASS", ""))

    # function name:connect_to_mqtt
    # Description:This function basically contain the functionality to connect to the mqtt  
    # Parameter: void:self
    # return:
    def connect_to_mqtt(self):
        host = self.host_entry.get()
        user = self.user_entry.get()
        password = self.pass_entry.get()

        try:
            self.mqtt_handler = MQTTHandler(host, user, password)
            self.mqtt_handler.set_message_callback(self.on_sensor_data_received)
            self.mqtt_handler.connect_and_start()
            self.mqtt_handler.subscribe("Waterloo/Warehouse/#")

            self.conn_status_label.configure(text="Connected successfully!!!", text_color="green")

            # Switch frames after successful connection
            self.connection_frame.pack_forget()
            self.config_frame.pack(expand=True, fill="both")

        except Exception as e:
            self.conn_status_label.configure(text=f"Connection failed: {e}", text_color="red")

    # function name:configration_tab
    # Description:this basically contain the UI for configration_tab
    # Parameter: void:self
    # return:
    def configration_tab(self, sensor_names):
        main_frame = ctk.CTkFrame(self.config_frame)
        main_frame.pack(expand=True, fill="both", padx=10, pady=10)

        main_frame.grid_columnconfigure(0, weight=2)  # left side 
        main_frame.grid_columnconfigure(1, weight=3)  # right side

        left_scrollbar_frame = ctk.CTkScrollableFrame(main_frame, width=600, height=600)
        left_scrollbar_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        right_scrollbar_frame = ctk.CTkScrollableFrame(main_frame)
        right_scrollbar_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        self.Sensor_configration(left_scrollbar_frame, sensor_names)
        self.sensor_display(right_scrollbar_frame)

        
    # function name: Sensor_configration
    # Description: This function basically contain the UI element for the sensor display(button/up/downs)
    # Parameter: void:self
    # return:None
    def Sensor_configration(self, parent_frame, sensor_names):
        row_index = 0
        for sensor_name in sensor_names:
            sensor_frame = ctk.CTkFrame(parent_frame, corner_radius=8)
            sensor_frame.grid(row=row_index, column=0, padx=10, pady=10, sticky="ew")
            sensor_frame.grid_columnconfigure(0, weight=1)
            row_index += 1

            # Title row
            title_label = ctk.CTkLabel(sensor_frame, text=sensor_name, font=("Arial", 14, "bold"))
            title_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

            battery_label = ctk.CTkLabel(sensor_frame, text="Battery:", font=("Arial", 12))
            battery_label.grid(row=0, column=1, padx=5, pady=5, sticky="e")

            battery_var = ctk.BooleanVar(value=True)
            battery_switch = ctk.CTkSwitch(sensor_frame,text="",variable=battery_var,command=lambda name=sensor_name: self.on_battery_switch_toggled(name))
            battery_switch.grid(row=0, column=2, padx=5, pady=5, sticky="w")

            self.sensor_configs[sensor_name] = {"battery_var": battery_var}

            fields = FIELDS_PER_SENSOR.get(sensor_name, [])
            data_field_row = 1
            for field_name in fields:
                lbl = ctk.CTkLabel(sensor_frame, text=f"{field_name}:", font=("Arial", 12))
                lbl.grid(row=data_field_row, column=0, padx=5, pady=5, sticky="e")

                up_btn = ctk.CTkButton(sensor_frame,text="UP",command=lambda s=sensor_name, f=field_name: self.adjust_data(s, f, "up"))
                up_btn.grid(row=data_field_row, column=1, padx=5, pady=5, sticky="w")

                down_btn = ctk.CTkButton(sensor_frame,text="DOWN",command=lambda s=sensor_name, f=field_name: self.adjust_data(s, f, "down"))
                down_btn.grid(row=data_field_row, column=2, padx=5, pady=5, sticky="w")

                data_field_row += 1
    
    # function name:Sensor_Display
    # Description: This function basically contain the UI elements for the Sensor Reading
    # Parameter: void:self
    # return:None
    def sensor_display(self, parent_frame):
        
        display_frame = ctk.CTkFrame(parent_frame, corner_radius=8)
        display_frame.pack(padx=10, pady=10, fill="x")
        header_label = ctk.CTkLabel(display_frame, text="Sensor Readings", font=("Arial", 14, "bold"))
        header_label.pack(pady=(5, 10))
        self.left_sensor_labels = {}

        # creating  a sub-frame for each sensor block
        for sensor_name, fields in FIELDS_PER_SENSOR.items():
            sensor_block_frame = ctk.CTkFrame(display_frame, corner_radius=8)
            sensor_block_frame.pack(pady=5, fill="x")

            sensor_title = ctk.CTkLabel(sensor_block_frame, text=sensor_name, font=("Arial", 13, "bold"))
            sensor_title.pack(anchor="w", padx=10, pady=(5, 2))

            for field in fields:
                # SensorName + FieldName: <Label>
                field_label = ctk.CTkLabel(sensor_block_frame, text=f"{field}: N/A")
                field_label.pack(anchor="w", padx=20, pady=2)

                # Store the reference
                self.left_sensor_labels[(sensor_name, field)] = field_label

    # function name:on_sensor_data_received
    # Description: This function is used  to get the sensor_data received
    # Parameter:topic,payload
    # return:None
    def on_sensor_data_received(self, topic, payload):
    
        try:
            data = json.loads(payload)
        except Exception as e:
            print(f"Error decoding JSON payload: {e}")
            return
        sensor_name = data.get("sensor_name")
        if not sensor_name:
            return

        # Retrieve sensor field readings from the payload
        sensor_values = data.get("data", {})

        # Update sensor field labels
        for field, value in sensor_values.items():
            label_key = (sensor_name, field)
            if label_key in self.left_sensor_labels:
                self.update_label(label_key, value)

      
        if sensor_name in self.sensor_configs:
            current_battery_state = self.sensor_configs[sensor_name]["battery_var"].get()
            if current_battery_state:
               if sensor_values:
                    inferred_battery = not all(v == 0 for v in sensor_values.values())
               else:
                    inferred_battery = True  # If no sensor values, assume battery remains on
               self.sensor_configs[sensor_name]["battery_var"].set(inferred_battery)
               battery_label_key = (sensor_name, "Battery")
               if battery_label_key in self.left_sensor_labels:
                    self.update_label(battery_label_key, "On" if inferred_battery else "Off")



    # function name:update_label
    # Description:This function is used to update the sensor reading label
    # Parameter: label_key,value
    # return:void
    def update_label(self, label_key, value):
        self.after(0, lambda: self.left_sensor_labels[label_key].configure(text=f"{label_key[1]}: {value}"))

    # function name:adjust_data
    # Description: This function basically call the adjust_data_one
    # Parameter:sensor_name,field_name,direction
    # return:None
    def adjust_data(self,sensor_name,field_name,direction="up"):
        adjust_data_one(sensor_name=sensor_name,field_name=field_name,direction=direction,mqtt_handler=self.mqtt_handler)

    # function name:on_battery_switch_toggled
    # Description: This function basically call the battery update function
    # Parameter: void:self
    # return:None
    def on_battery_switch_toggled(self, sensor_name):
      
        is_on = self.sensor_configs[sensor_name]["battery_var"].get()
        # on_off_battery_switch(sensor_name=sensor_name,is_on=is_on,mqtt_handler=self.mqtt_handler,sensor_data_manager=self.sensor_data_manager,msg_display=self.msg_display)
        on_off_battery_switch(sensor_name=sensor_name,is_on=is_on,mqtt_handler=self.mqtt_handler)
        