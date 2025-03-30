import sys
import os
import pytest


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Sensors.thermostat import thermostat

@pytest.fixture
def thermostat_sensor():
    # Initialize the thermostat with an initial temperature of 25.0
    sensor = thermostat("TestThermostat", drain_cycle=10, set_temp=25.0)
    return sensor

def test_increment_temperature(thermostat_sensor):
    # Increase the temperature by 1.0 and verify it is rounded to 2 decimals.
    thermostat_sensor.set_increment_temp_one()
    assert thermostat_sensor.set_temperature == 26.0
    assert thermostat_sensor.temperataure_generater() == 26.0

def test_decrement_temperature(thermostat_sensor):
    # Decrease the temperature by 1.0 and verify it is rounded to 2 decimals.
    thermostat_sensor.set_decrement_temp_one()
    assert thermostat_sensor.set_temperature == 24.0
    assert thermostat_sensor.temperataure_generater() == 24.0

def test_decrement_temperature_below_zero():
    # Initialize sensor with a low temperature so that decrementing goes below zero.
    sensor = thermostat("BelowZeroThermostat", drain_cycle=10, set_temp=0.5)
    
    # Print the initial temperature using sys.stdout.write and flush to ensure it appears.
    sys.stdout.write(f"Initial temperature: {sensor.set_temperature}\n")
    sys.stdout.flush()
    
    # Decrement the temperature by 1.0 (0.5 - 1.0 = -0.5)
    sensor.set_decrement_temp_one()
    sys.stdout.write(f"New temperature: {sensor.set_temperature}\n")
    sys.stdout.flush()
    # Verify that the temperature is correctly updated and rounded.
    assert sensor.set_temperature == -0.5
    assert sensor.temperataure_generater() == -0.5
