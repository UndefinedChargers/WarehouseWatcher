# FILE :thermostat.py
# PROJECT :Wharehouse Watcher
# PROGRAMMER : Amel korandippillil Sunil
# FIRST VERSION : 
# DESCRIPTION :This basically conisist of a class which simulates a temperature sensor(Thermostat)


import random
import uuid
import time
import json
import datetime
from Sensors.BaseSensor import BaseSensor
from loguru import logger


class thermostat(BaseSensor):
   

    def __init__(self,sensor_name,drain_cycle,set_temp):
        super().__init__(sensor_name,drain_cycle)
        # self.temp_range=temp_rang
        self.default_temperature=set_temp
        self.set_temperature=set_temp
        logger.info(f"ThermostatSensor initialized: {self.sensor_name} | ID: {self.sensor_id}",file="./Logs/sensorLogs.log")
            
    # function name:temperataure_generater(self)
    # Description:This funciton is used to provide us with the temperature
    # Parameter:void:
    # return:int number:battery.

    def temperataure_generater(self):
        # return round(random.uniform(*self.temp_range), 2)
        return self.set_temperature
    
    #functions for the UI updates

    # function name:set_increment_temp_one(self)
    # Description:This funciton is used to increment the set temperture by 1
    # Parameter:void:
    # return:int number:battery.
    def set_increment_temp_one(self):
        # self.set_temperature+=1.0
        self.set_temperature=round(self.set_temperature+1.0,2)
        logger.info(f"Manual temperature incremented for {self.sensor_name} to {self.set_temperature}",file="./Logs/sensorLogs.log")
        
    # function name:set_decrement_temp_one
    # Description:This funciton is used to decrement the set temperture by 1
    # Parameter:void:
    # return:int number:battery.
    def set_decrement_temp_one(self):
        # self.set_temperature-=1.0
        self.set_temperature=round(self.set_temperature-1.0,2)
        logger.info(f"Manual temperature Decremented for {self.sensor_name} to {self.set_temperature}",file="./Logs/sensorLogs.log") 
    
   
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

        temperature = self.temperataure_generater()
        signal_strength = self.generate_signal_strength()
        state = self.state()
        met_requirements = self.notification_settings()

        data_packets={
            "Method": "SensorMessage",
            "Result": [
                {
                    "MessageID": str(uuid.uuid4()),
                    "SensorID": self.sensor_id,
                    "MessageDate": datetime.datetime.now().isoformat(),
                    "State": state,
                    "SignalStrength": signal_strength,
                    "Voltage": voltage,
                    "Battery": battery,
                    "Data":temperature,
                    "DisplayData":"temperature",
                    "PlotValue":temperature,
                    "MetNotificationRequirements":met_requirements,
                    "GatewayID": random.randint(100000, 999999),
                    "DataValues":temperature,
                    "DataTypes": "TemperatureData",
                    "PlotValues":temperature,
                    "PlotLabels": "Celsius",
                }
            ]
        }
        logger.info("Generated Thermostat data",file="./Logs/sensorLogs.log")
        return json.dumps(data_packets)
    
   

    


        
    