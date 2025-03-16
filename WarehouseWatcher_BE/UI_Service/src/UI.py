# FILE :main.py
# PROJECT :Warehouse Watcher
# PROGRAMMER : Amel Korandippillil Sunil
# DESCRIPTION :This file basically contain the intial setup of the UI


import json
import customtkinter as ctk
import threading

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
        self.setup_UI(sensor_names)

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
    def configration_tab(self,sensor_name):
        
        config_tab = self.tabview.tab("Configuration")
        
        main_frame = ctk.CTkFrame(config_tab)
        main_frame.pack(expand=True, fill="both", padx=10, pady=10)

        main_frame.grid_columnconfigure(0, weight=2)  # left side
        main_frame.grid_columnconfigure(1, weight=3)  # right side


        left_frame = ctk.CTkFrame(main_frame)
        left_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        right_frame = ctk.CTkFrame(main_frame, corner_radius=8)
        right_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        #self.sensor_configration(left_frame, sensor_name)
       
    