# FILE :humidity.py
# PROJECT :Warehouse Watcher
# PROGRAMMER : Amel korandippillil Sunil
# FIRST VERSION :
# DESCRIPTION :This basically consists of a class which simulates a humidity Sensor

import random
import uuid
import time
import json
import datetime
from Sensors.BaseSensor import BaseSensor

class HumiditySensor(BaseSensor):
    def __init__(self, sensor_name, thermostat_sensor, humidity_range=(20, 90), drain_cycle=100):
        super().__init__(sensor_name, drain_cycle)
        
        # Ensure humidity_range is always a valid two-element tuple
        if isinstance(humidity_range, (list, tuple)) and len(humidity_range) == 2:
            self.humidity_range = (float(humidity_range[0]), float(humidity_range[1]))
        else:
            raise ValueError("humidity_range must be a tuple/list of exactly two numeric values.")

        self.thermostat_sensor = thermostat_sensor  # Link to thermostat sensor

    # function name: generate_humidity(self)
    # Description: This function generates a simulated humidity value within the given range.
    # Parameter: void:self
    # return: float - Simulated humidity value  
    def generate_humidity(self):
       return round(random.uniform(*self.humidity_range), 2)
    
    # function name: calculate_dew_point(self, humidity)
    # Description: This function calculates a simple dew point approximation based on the current temperature from the thermostat sensor.
    # Parameter: float humidity
    # return: float - Dew point in °C
    def calculate_dew_point(self, humidity):
        temperature = self.thermostat_sensor.temperataure_generater()  
        return round(temperature - ((100 - humidity) / 5), 2)
    
    # function name: calculate_air_weight(self, humidity)
    # Description: This function returns an approximate air weight/density factor adjusted by humidity.
    # Parameter: float humidity
    # return: float - Air weight in kg/m^3
    def calculate_air_weight(self, humidity):
        base_density = 1.225  # standard air density at sea level (kg/m^3)
        humidity_factor = (humidity / 100) * 0.01
        return round(base_density * (1 - humidity_factor), 3)
    
    # function name: generate_sensor_data(self)
    # Description: This function generates a JSON packet containing simulated humidity-related data.
    # Parameter: void:self
    # return: str - JSON-formatted sensor data
    def generate_sensor_data(self):
        
        battery = self.battery_updates()
        voltage = self.update_voltage()
        
        if voltage < self.min_voltage:
            print(f"{self.sensor_name} has shut down due to low voltage.")
            return None  

        humidity = self.generate_humidity()
        moisture_weight = round(humidity / 6.22, 2)
        dew_point = self.calculate_dew_point(humidity)
        air_weight = self.calculate_air_weight(humidity)

        data_packets = {
            "Method": "SensorDataMessages",
            "Result": [
                {
                    "DataMessageGUID": str(uuid.uuid4()),
                    "SensorID": self.sensor_id,
                    "MessageDate": datetime.datetime.now().isoformat(),
                    "State": self.state(),
                    "SignalStrength": self.generate_signal_strength(),
                    "Voltage": voltage,
                    "Battery": battery,

                    "Humidity": humidity,
                    "MoistureWeight": moisture_weight,
                    "DewPoint": dew_point,
                    "AirWeight": air_weight,

                    # "DisplayData": f"{humidity}%, Dew Point: {dew_point}°C, Air Weight: {air_weight}kg/m³",

                    # "PlotValue": str(humidity),
                    "MetNotificationRequirements": self.notification_settings(),
                    "GatewayID": random.randint(100000, 999999),
                    "DataValues": f"{humidity}|{moisture_weight}|{dew_point}|{air_weight}",

                    # "DataTypes": "Percentage|MoistureWeight|DewPoint|AirWeight",
                    # "PlotValues": f"{humidity}|{moisture_weight}|{dew_point}|{air_weight}",
                    # "PlotLabels": "Humidity|GramsPerKilogram|DewPoint_Celsius|AirWeight_kg/m³"
                    
                    "DataType_Humidity": "Percentage",
                    "DataType_MoistureWeight": "MoistureWeight",
                    "DataType_DewPoint": "DewPoint",
                    "DataType_AirWeight": "AirWeight",

                    "PlotLabel_Humidity": "Humidity",
                    "PlotLabel_MoistureWeight": "GramsPerKilogram",
                    "PlotLabel_DewPoint": "DewPoint_Celsius",
                    "PlotLabel_AirWeight": "AirWeight_kg/m³",
                }
            ]
        }
        return json.dumps(data_packets, indent=4)
