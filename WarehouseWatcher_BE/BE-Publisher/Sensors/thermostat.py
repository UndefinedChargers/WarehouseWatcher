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



class thermostat:
    def __init__(self,sensor_name,temp_range,drain_cycle):
        self.sensor_name=sensor_name
        self.temp_range=temp_range
        self.sensor_id=str(uuid.uuid4)

        self.battery=100     #getting started with full battery
        self.base_voltage=4 # its maximum voltage
        self.base_signal_strength=100           
        self.min_voltage=2.5
        self.lowPower_threshold=20 # making it as a low threashold for battery
        self.battery_drain_cycle=drain_cycle
        self.drain_per_cycle=100 /self.battery_drain_cycle
        self.cycle_count=0
        
    # function name:temperataure_generater(self)
    # Description:This funciton is used to provide us with the temperature
    # Parameter:void:
    # return:int number:battery.


    def temperataure_generater(self):
        return round(random.uniform(*self.temp_range), 1)
    
        
    # function name:battery_updates()
    # Description:This function is used to simulate and  update the battey drain and life
    # Parameter:void:self
    # return:int number:battery

    def battery_updates(self):
        if self.battery <= 0:
            print("Battery depleted. Sensor shutting down.")
            return 0
        self.cycle_count += 1

        adjusted_drain = self.drain_per_cycle  # Keep drain rate unchanged
        self.battery = max(0, self.battery - adjusted_drain)
        print(f"Cycle {self.cycle_count}/{self.battery_drain_cycle}: Battery = {round(self.battery, 2)}%")

        return round(self.battery, 2)

    # function name:update_voltage(self)
    # Description:This function is used to simulate the voltage need for this sensor
    # Parameter:void:self
    # return:int number:voltage value

    def update_voltage(self):
        if self.battery <=0:
            return 0
        self.base_voltage=max(2.5,3.0+(self.battery/100*0.3))
        return round(self.base_voltage,2)
    
    # function name:generate_signal_strength(self)
    # Description:This function is used to sio generate signal strength
    # Parameter:void:self
    # return:int number:base_segnal_strength
    def generate_signal_strength(self):
       
        if self.battery <= 0:
            return 0  # No signal when battery is dead
        # Use `int` instead of `float` for `random.randint`
        self.base_signal_strength = max(50, random.randint(60, int(self.base_signal_strength)))
        return self.base_signal_strength
    
    # function name:state(self)
    # Description:This function is used to set or provide the state of  the sensor
    # Parameter:void:self
    # return:int number:base_segnal_strength
    def state(self):
        
        if self.battery <=0 or self.update_voltage() <=self.min_voltage:
            return 2 # indicating critical state(battery is low)
        elif self.battery < 20:
            return 1 # its basically a warning state (Low battery maybe)
        elif self.battery >=20:
            return 0 # ok working state
        return 3 # unknown state
    
    # function name:notification_settings(self)
    # Description:This function is used to provide us with the notification status enabled
    # Parameter:void:self
    # return:Boolean
    def notification_settings(self):
        state = self.state()
        if state == 0:
           return False
        elif state == 1:
           return False
        elif state == 2:
            return True
        else:
            return True
      

    # function name:generate_sensor_data(self)
    # Description:This function is used to set the data packets to send
    # Parameter:void:self
    # return:int json packet
    def generate_sensor_data(self):
    
        battery = self.battery_updates()

        voltage = self.update_voltage()

        if voltage < self.min_voltage:
            print(f"{self.sensor_name} has shut down due to low voltage.")
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
        return json.dumps(data_packets)
    
   

    


        
    