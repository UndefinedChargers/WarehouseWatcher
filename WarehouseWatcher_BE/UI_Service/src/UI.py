# FILE :main.py
# PROJECT :Warehouse Watcher
# PROGRAMMER : Amel Korandippillil Sunil
# DESCRIPTION :This file basically contain the intial setup of the UI
import json
import customtkinter as ctk
import threading
from src.Sensor_logic import on_off_battery_switch,adjust_data_one
from src.mqtt_handler import MQTTHandler


FIELDS_PER_SENSOR = {
    "Room": ["Temperature"],
    "Refrigerator": ["Temperature"],
    "Freezer": ["Temperature"],
    "AirQuality_warehouse": ["PM2.5", "CO2", "VOC"],
    "humidity_warehouse": ["Humidity", "MoistureWeight", "DewPoint", "AirWeight"]
}


class SimulatorUI(ctk.CTk):
    def __init__(self, sensor_names, host, user, password):
        super().__init__()
        self.title("Warehouse Watcher Simulator UI")
        self.geometry("1050x650")
        self.sensor_configs = {}
        self.setup_UI(sensor_names)
        self.mqtt_handler = MQTTHandler(
            host=host,
            user=user,
            password=password,
           
        )
        self.mqtt_handler.connect_and_start()


    # function name: setup_UI
    # Description: This function generates provide us with a basic UI setup
    # Parameter: void:self
    # return: None 
    def setup_UI(self,sensor_name):
        self.tabview = ctk.CTkTabview(self, width=1000, height=600)
        self.tabview.pack(expand=True, fill="both", padx=10, pady=10)

        self.tabview.add("Messages")
        self.tabview.add("Configuration")

        self.msg_display = ctk.CTkTextbox(self.tabview.tab("Messages"),wrap="word",font=("Arial", 12))
        self.msg_display.pack(expand=True, fill="both", padx=10, pady=10)
        self.configration_tab(sensor_name)
    # function name: configration_tab
    # Description: This function generates provide us with the Ui for the configration tab
    # Parameter: void:self
    # return: float - Simulated humidity value  
    def configration_tab(self, sensor_name):
        config_tab = self.tabview.tab("Configuration")

        main_frame = ctk.CTkFrame(config_tab)
        main_frame.pack(expand=True, fill="both", padx=10, pady=10)

        main_frame.grid_columnconfigure(0, weight=2)  # left side 
        main_frame.grid_columnconfigure(1, weight=3)  # right side

        left_scrollbar_frame = ctk.CTkScrollableFrame(main_frame, width=600, height=600)
        left_scrollbar_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        #right scrollbar
        right_scrollbar_frame=ctk.CTkScrollableFrame(main_frame)
        right_scrollbar_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        self.Sensor_configration(left_scrollbar_frame, sensor_name)
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

    # function name:adjust_data
    # Description: This function basically call the adjust_data_one
    # Parameter: void:self
    # return:None
    def adjust_data(self,sensor_name,field_name,direction="up"):
        adjust_data_one(sensor_name=sensor_name,field_name=field_name,direction=direction,mqtt_handler=self.mqtt_handler)

    # function name:on_battery_switch_toggled
    # Description: This function basically call the battery update function
    # Parameter: void:self
    # return:None
    def on_battery_switch_toggled(self, sensor_name):
      
        is_on = self.sensor_configs[sensor_name]["battery_var"].get()
        on_off_battery_switch(sensor_name=sensor_name,is_on=is_on,mqtt_handler=self.mqtt_handler,sensor_data_manager=self.sensor_data_manager,msg_display=self.msg_display)

        