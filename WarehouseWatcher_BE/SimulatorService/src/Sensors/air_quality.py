# FILE :air_quality .py
# PROJECT :Wharehouse Watcher
# PROGRAMMER : Amel korandippillil Sunil
# FIRST VERSION : 
# DESCRIPTION :This basically conisist of a class which simulates a airquality sensor

import random
import uuid
import time
import json
import datetime
from Sensors.BaseSensor import BaseSensor
from loguru import logger 

class AirQualitySensor(BaseSensor):
    def __init__(self, sensor_name, pm_range=(5, 100), co2_range=(300, 1000), voc_range=(0, 500), drain_cycle=100):
        super().__init__(sensor_name, drain_cycle)
        self.setCO2=400 # set the value of the Co2
        self.setPm25=10 # set the value for PM2.5
        self.setVOC=200
        self.pm_range = pm_range
        self.co2_range = co2_range
        self.voc_range = voc_range
        logger.info(f"AirQualitySensor initialized: {self.sensor_name} | ID: {self.sensor_id}",file="./Logs/sensorLogs.log")

    # function name: generate_pm(self)
    # Description: This function generates a simulated PM2.5 or PM10 value.
    # Parameter: void:self
    # return: float - Simulated PM value
    def generate_pm(self):
       
        # return round(random.uniform(*self.pm_range), 1)
        return self.setPm25
    
    # function name: generate_co2(self)
    # Description: This function generates a simulated CO2 concentration.
    # Parameter: void:self
    # return: int - Simulated CO2 concentration in ppm
    def generate_co2(self):
        
        return self.setCO2

     # function name: generate_voc(self)
    # Description: This function generates a simulated VOC level.
    # Parameter: void:self
    # return: int - Simulated VOC concentration in ppb
    def generate_voc(self):
        # return random.randint(*self.voc_range)
        self.setVOC
    
    # function name:generate_sensor_data(self)
    # Description:This function is used to set the data packets to send
    # Parameter:void:self
    # return:int json packet
    def generate_sensor_data(self):
        
        battery = self.battery_updates()
        voltage = self.update_voltage()

        if voltage < self.min_voltage:
            # print(f"{self.sensor_name} has shut down due to low voltage.")
            logger.warning(f"{self.sensor_name} has shut down due to low voltage.",file="./Logs/sensorLogs.log")
            return None  

        data_packets = {
            "Method": "SensorMessage",
            "Result": [
                {
                    "MessageID":str(uuid.uuid4()),
                    "SensorID": self.sensor_id,
                    "MessageDate": datetime.datetime.now().isoformat(),
                    "State": self.state(),
                    "SignalStrength": self.generate_signal_strength(),
                    "Voltage": voltage,
                    "Battery": battery,

                    "PM2.5": self.generate_pm(),
                    "PM10": self.generate_pm(),
                    "CO2": self.generate_co2(),
                    "VOC": self.generate_voc(),
                    
                    "MetNotificationRequirements": self.notification_settings(),
                    "GatewayID": random.randint(100000, 999999),
                    "DataType1": "PM2.5",
                    "DataType2": "PM10",
                    "DataType3": "CO2",
                    "DataType4": "VOC",

                    "PlotLabel1": "ug/m3",
                    "PlotLabel2": "ug/m3",
                    "PlotLabel3": "ppm",
                    "PlotLabel4": "ppb"
                }
            ]
        }
        # logger.info(f"Generated AirQualitySensor data: {json.dumps(data_packets, indent=4)}")
        logger.info(f"Generated AirQualitySensor data:",file="./Logs/sensorLogs.log")
        return json.dumps(data_packets, indent=4)

