# FILE :test_air_quality .py
# PROJECT :Wharehouse Watcher
# PROGRAMMER : Amel korandippillil Sunil
# FIRST VERSION : 
# DESCRIPTION :This class basically has some unit test cases for the airquality sensors.


import sys
import os
import json
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Sensors.air_quality import AirQualitySensor

@pytest.fixture
#these intializer basically has many dummy values
def air_quality_sensor():
    # Instantiate the AirQualitySensor with test ranges.
    sensor = AirQualitySensor("TestAirQuality", pm_range=(5, 100), co2_range=(300, 1000), voc_range=(0, 500), drain_cycle=100)
    sensor.battery = 100
    sensor.min_voltage = 3.0
    sensor.battery_updates = lambda: 100   
    sensor.update_voltage = lambda: 3.5      
    sensor.state = lambda: "active"          
    sensor.generate_signal_strength = lambda: 70  
    sensor.notification_settings = lambda: False    
    return sensor

# Test that generate_pm returns the default PM2.5 value.
def test_generate_pm(air_quality_sensor):
    # Default setPm25 is 10.
    assert air_quality_sensor.generate_pm() == 10

# Test incrementing PM2.5 by 5.
def test_increment_pm(air_quality_sensor):
    air_quality_sensor.setPm25 = 10
    air_quality_sensor.set_increment_pm_five()
    assert air_quality_sensor.setPm25 == 15

# Test decrementing PM2.5 by 5.
def test_decrement_pm(air_quality_sensor):
    air_quality_sensor.setPm25 = 10
    air_quality_sensor.set_decrement_pm_five()
    assert air_quality_sensor.setPm25 == 5

# Test incrementing CO2 by 100.
def test_increment_co2(air_quality_sensor):
    air_quality_sensor.setCO2 = 400
    air_quality_sensor.set_increment_co2_100()
    assert air_quality_sensor.setCO2 == 500

# Test decrementing CO2 by 100
def test_decrement_co2(air_quality_sensor):
    air_quality_sensor.setCO2 = 400
    air_quality_sensor.set_decrement_co2_100()
    assert air_quality_sensor.setCO2 == 300

# Test incrementing VOC by 50
def test_increment_voc(air_quality_sensor):
    air_quality_sensor.setVOC = 200
    air_quality_sensor.set_increment_VOC_50()
    assert air_quality_sensor.setVOC == 250

# Test decrementing VOC by 50
def test_decrement_voc(air_quality_sensor):
    air_quality_sensor.setVOC = 200
    air_quality_sensor.set_decrement_VOC_50()
    assert air_quality_sensor.setVOC == 150

# Test that generate_co2 returns the current CO2 value.
def test_generate_co2(air_quality_sensor):
    air_quality_sensor.setCO2 = 450
    assert air_quality_sensor.generate_co2() == 450

# Test that generate_voc returns the current VOC value.
def test_generate_voc(air_quality_sensor):
    air_quality_sensor.setVOC = 220
    assert air_quality_sensor.generate_voc() == 220

# testing successfull data generation
def test_generate_sensor_data_success(air_quality_sensor):
    data_json = air_quality_sensor.generate_sensor_data()
    assert data_json is not None
    data = json.loads(data_json)
    assert "Method" in data
    assert data["Method"] == "SensorMessage"
    assert "Result" in data
    result = data["Result"][0]
    # Check expected keys in the sensor data packet.
    for key in ["PM2.5", "PM10", "CO2", "VOC"]:
        assert key in result

# Test that sensor data generation returns None when voltage is below the minimum.
def test_generate_sensor_data_low_voltage(air_quality_sensor):
    # Simulate low voltage scenario.
    air_quality_sensor.update_voltage = lambda: 2.0  # below min_voltage of 3.0
    data = air_quality_sensor.generate_sensor_data()
    assert data is None
