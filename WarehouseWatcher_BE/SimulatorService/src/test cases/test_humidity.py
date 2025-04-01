# FILE:test_humidity.py
# PROJECT :Wharehouse Watcher
# PROGRAMMER : Amel korandippillil Sunil
# FIRST VERSION : 
# DESCRIPTION :This class basically contain the test case for the humidity sensor


import sys
import os
import json
import pytest
import datetime
import uuid

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Sensors.humidity import HumiditySensor


class DummyThermostat:
    def temperataure_generater(self):
        return 25.0

@pytest.fixture
def thermostat_sensor():
    return DummyThermostat()

@pytest.fixture
def humidity_sensor(thermostat_sensor):
    # Instantiate the HumiditySensor with a valid humidity range.
    sensor = HumiditySensor("TestHumiditySensor", thermostat_sensor, humidity_range=(20, 90), drain_cycle=100)
    sensor.battery = 100
    sensor.min_voltage = 3.0
    sensor.battery_updates = lambda: 100   
    sensor.update_voltage = lambda: 3.5      
    sensor.state = lambda: "active"          
    sensor.generate_signal_strength = lambda: 70  
    sensor.notification_settings = lambda: False  
    return sensor

#Default Humidity Value
def test_generate_humidity_default(humidity_sensor):
    # Default setHumid is 45.0, so generate_humidity() should return 45.0.
    assert humidity_sensor.generate_humidity() == 45.0

# Test 2: Humidity Increment
def test_set_increment_humidity(humidity_sensor):
    humidity_sensor.setHumid = 45.0
    humidity_sensor.set_increment_humidity_5()
    # After increment, humidity should be 50.0.
    assert humidity_sensor.generate_humidity() == 50.0

# Test 3: Humidity Decrement
def test_set_decrement_humidity(humidity_sensor):
    humidity_sensor.setHumid = 45.0
    humidity_sensor.set_decrement_humidity_5()
    # After decrement, humidity should be 40.0.
    assert humidity_sensor.generate_humidity() == 40.0

# Test 4: Dew Point Calculation
def test_calculate_dew_point(humidity_sensor):
    # For a thermostat temperature of 25°C and humidity of 45:
    # Expected dew point = 25 - ((100 - 45) / 5) = 25 - 11 = 14.0°C
    dew_point = humidity_sensor.calculate_dew_point(45.0)
    assert dew_point == 14.0

# Test 5: Air Weight Calculation
def test_calculate_air_weight(humidity_sensor):
    # For humidity = 45.0, humidity_factor = (45/100)*0.01 = 0.0045
    # Expected air weight = round(1.225 * (1 - 0.0045), 3)
    expected_air_weight = round(1.225 * (1 - 0.0045), 3)
    assert humidity_sensor.calculate_air_weight(45.0) == expected_air_weight

# Test 6: Sensor Data Generation (Normal Operation)
def test_generate_sensor_data_success(humidity_sensor):
    data_json = humidity_sensor.generate_sensor_data()
    assert data_json is not None
    data = json.loads(data_json)
    # Verify top-level keys.
    assert "Method" in data and data["Method"] == "SensorDataMessages"
    assert "Result" in data and isinstance(data["Result"], list) and len(data["Result"]) > 0
    result = data["Result"][0]
    expected_keys = [
        "DataMessageGUID", "SensorID", "MessageDate", "State", "SignalStrength",
        "Voltage", "Battery", "Humidity", "MoistureWeight", "DewPoint", "AirWeight",
        "MetNotificationRequirements", "GatewayID", "DataValues",
        "DataType_Humidity", "DataType_MoistureWeight", "DataType_DewPoint", "DataType_AirWeight",
        "PlotLabel_Humidity", "PlotLabel_MoistureWeight", "PlotLabel_DewPoint", "PlotLabel_AirWeight"
    ]
    for key in expected_keys:
        assert key in result

# Test 7: Sensor Data Generation (Low Voltage)
def test_generate_sensor_data_low_voltage(humidity_sensor):
    # Simulate low voltage by setting update_voltage to return a value below min_voltage.
    humidity_sensor.update_voltage = lambda: 2.0  # 2.0 is below the min_voltage of 3.0.
    data = humidity_sensor.generate_sensor_data()
    assert data is None

# Test 8: Invalid Humidity Range Parameter
def test_invalid_humidity_range(thermostat_sensor):
    # An invalid humidity_range (e.g., only one element) should raise a ValueError.
    with pytest.raises(ValueError):
        HumiditySensor("InvalidHumiditySensor", thermostat_sensor, humidity_range=(20,))
