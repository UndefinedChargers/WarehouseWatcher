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

class AirQualitySensor:
    def __init__(self, sensor_name, pm_range=(5, 100), co2_range=(300, 1000), voc_range=(0, 500), drain_cycle=100):
        self.sensor_name = sensor_name
        self.sensor_id = str(uuid.uuid4())
        
        # Measurement Ranges
        self.pm_range = pm_range
        self.co2_range = co2_range
        self.voc_range = voc_range

        # Battery and Power
        self.battery = 100
        self.base_voltage = 4.0  
        self.base_signal_strength = 100
        self.min_voltage = 2.5
        self.lowPower_threshold = 20
        self.battery_drain_cycle = drain_cycle
        self.drain_per_cycle = 100 / self.battery_drain_cycle
        self.cycle_count = 0

    def generate_pm(self):
        """Simulates PM2.5 and PM10 readings."""
        return round(random.uniform(*self.pm_range), 1)

    def generate_co2(self):
        """Simulates CO2 levels in ppm."""
        return random.randint(*self.co2_range)

    def generate_voc(self):
        """Simulates VOC levels in ppb."""
        return random.randint(*self.voc_range)

    def battery_updates(self):
        """Simulates battery drain over time."""
        if self.battery <= 0:
            print("Battery depleted. Sensor shutting down.")
            return 0
        self.cycle_count += 1
        self.battery = max(0, self.battery - self.drain_per_cycle)
        return round(self.battery, 2)

    def update_voltage(self):
       
        if self.battery <= 0:
            return 0
        self.base_voltage = max(self.min_voltage, 3.0 + (self.battery / 100 * 0.3))
        return round(self.base_voltage, 2)

    def generate_signal_strength(self):
        
        if self.battery <= 0:
            return 0
        return max(50, random.randint(60, int(self.base_signal_strength)))

    def state(self):
       
        if self.battery <= 0 or self.update_voltage() <= self.min_voltage:
            return 2  # Critical state
        elif self.battery < 20:
            return 1  # Warning state (low battery)
        return 0  # Normal working state

    def notification_settings(self):
        
        return self.state() == 2

    def generate_sensor_data(self):
        
        battery = self.battery_updates()
        voltage = self.update_voltage()

        if voltage < self.min_voltage:
            print(f"{self.sensor_name} has shut down due to low voltage.")
            return None  

        data_packets = {
            "Method": "SensorMessage",
            "Result": [
                {
                    "MessageID": str(uuid.uuid4()),
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
                    "DataTypes": ["PM2.5", "PM10", "CO2", "VOC"],
                    "PlotLabels": ["ug/m3", "ug/m3", "ppm", "ppb"]
                }
            ]
        }
        return json.dumps(data_packets, indent=4)

