# FILE :main.py
# PROJECT :Warehouse Watcher
# PROGRAMMER : Amel Korandippillil Sunil
# DESCRIPTION :This is the main file which is used to run the main GUI



import os
import json
from dotenv import load_dotenv
import customtkinter as ctk
#from src.UI import SimulatorUI
from src.UI import SimulatorUI



def main():
    load_dotenv()
    host = os.getenv("HIVEMQ_HOST")
    user = os.getenv("HIVEMQ_USER")
    password = os.getenv("HIVEMQ_PASS")

    config_path = "config.json"
    if os.path.exists(config_path):
        with open(config_path, "r") as f:
            config = json.load(f)
    else:
        # this is the default configration for the config
        config = {
            "appearance_mode": "System",
            "color_theme": "blue",
            "sensor_names": [
                "Room",
                "Refrigerator",
                "Freezer",
                "AirQuality_warehouse",
                "humidity_warehouse"
            ]
        }
    ctk.set_appearance_mode(config.get("appearance_mode", "System"))
    ctk.set_default_color_theme(config.get("color_theme", "blue"))

    sensor_names = config.get("sensor_names", [])
    
    app = SimulatorUI(sensor_names, host, user, password)
    app.mainloop()

if __name__ == "__main__":
    main()
