# FILE :BaseSensor.py
# PROJECT :Wharehouse Watcher
# PROGRAMMER : Amel korandippillil Sunil
# FIRST VERSION : 
# DESCRIPTION :This basically is the base sensor which has the common function of the sensors like battery ,sensor_id etc 
import random
import uuid
import time
import json
import datetime
from abc import ABC,  abstractmethod

class BaseSensor(ABC):
    def __init__(self,sensor_name,drain_cycle=100):
        self.sensor_name=sensor_name
        self.sensor_id=str(uuid.uuid4())
        self.battery=100
        self.volatage=4.0
        self.base_signal_strength=100
        self.min_voltage=2.5
        self.lowPower_threshold=20
        self.battery_drain_cycle = drain_cycle
        self.drain_per_cycle = 100 / self.battery_drain_cycle
        self.cycle_count = 0

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
      
     # function name:restart_sensor(self)
    # Description:This function is used to provide us with the restart functionality in the case of battery being dead of a sensor
    # Parameter:void:self
    # return:Boolean

    def restart_sensor(self):
        if self.battery <= 0 or self.update_voltage() < self.min_voltage:
           
            # Reset sensor attributes
            self.battery = 100
            self.base_voltage = 4.0
            self.base_signal_strength = 100
            self.cycle_count = 0
            self.sensor_id = str(uuid.uuid4())  # Generate a new sensor ID (simulating reboot)

            print(f"{self.sensor_name} has restarted and is now operational again.")
        else:
            print(f"{self.sensor_name} is already running. No restart needed.")


    @abstractmethod
    def generate_sensor_data(self):
        pass




    