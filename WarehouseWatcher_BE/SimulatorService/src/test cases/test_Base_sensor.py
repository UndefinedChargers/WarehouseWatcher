import sys
import os
import pytest


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Sensors.BaseSensor import BaseSensor

class DummySensor(BaseSensor):
    def generate_sensor_data(self):
        return {"dummy": "data"}

@pytest.fixture
def sensor():
    return DummySensor("TestSensor", drain_cycle=100)

def test_battery_updates(sensor):
    initial_battery = sensor.battery
    battery_after_update = sensor.battery_updates()
    # Battery should decrease by 1% per cycle
    assert battery_after_update == pytest.approx(initial_battery - 1.0, rel=1e-2)
    assert sensor.cycle_count == 1

def test_update_voltage(sensor):
    # With full battery,voltage should be calculated as: max(2.5, 3.0 + (100/100*0.3)) = 3.3
    voltage = sensor.update_voltage()
    assert voltage == pytest.approx(3.3, rel=1e-2)
    # When battery is depleted, update_voltage should return 0
    sensor.battery = 0
    assert sensor.update_voltage() == 0

def test_generate_signal_strength(sensor):
    # With battery > 0, signal strength should be at least 50
    strength = sensor.generate_signal_strength()
    assert strength >= 50
    sensor.battery = 0
    # With battery 0, signal strength should be 0
    assert sensor.generate_signal_strength() == 0

def test_state(sensor):
    sensor.battery = 100
    assert sensor.state() == 0  # OK state
    sensor.battery = 10
    assert sensor.state() == 1  # Warning state (low battery)
    sensor.battery = 0
    assert sensor.state() == 2  # Critical state

def test_notification_settings(sensor):
    sensor.battery = 100
    assert sensor.notification_settings() == False
    sensor.battery = 10
    assert sensor.notification_settings() == False
    sensor.battery = 0
    assert sensor.notification_settings() == True

def test_restart_sensor(sensor):
    # Set up the sensor to be in a state where a restart should occur
    sensor.battery = 0
    sensor.set_batteryUI = True
    old_sensor_id = sensor.sensor_id
    sensor.restart_sensor()
    assert sensor.battery == 100
    assert sensor.base_voltage == 4.0
    assert sensor.base_signal_strength == 100
    assert sensor.cycle_count == 0
    assert sensor.sensor_id != old_sensor_id

    # Now check that if conditions for restart are not met, sensor remains unchanged
    sensor.battery = 80
    sensor.set_batteryUI = False
    current_battery = sensor.battery
    sensor.restart_sensor()
    assert sensor.battery == current_battery
