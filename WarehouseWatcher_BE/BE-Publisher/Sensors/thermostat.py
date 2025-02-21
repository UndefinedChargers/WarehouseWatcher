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
   

    def __init__(self,sensor_name,temp_range,drain_cycle):
        super().__init__(sensor_name,drain_cycle)
        self.temp_range=temp_range
            
    # function name:temperataure_generater(self)
    # Description:This funciton is used to provide us with the temperature
    # Parameter:void:
    # return:int number:battery.

    def temperataure_generater(self):
        return round(random.uniform(*self.temp_range), 2)
    
        
    
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
                    "Data": str(temperature),
                    "DisplayData": f"{temperature}\u00b0 C",
                    "PlotValue": str(temperature),
                    "MetNotificationRequirements":met_requirements,
                    "GatewayID": random.randint(100000, 999999),
                    "DataValues": str(temperature),
                    "DataTypes": "TemperatureData",
                    "PlotValues": str(temperature),
                    "PlotLabels": "Celsius",
                }
            ]
        }
        logger.info("Generated Thermostat data",file="./Logs/sensorLogs.log")
        return json.dumps(data_packets)
    
   

    


        
    