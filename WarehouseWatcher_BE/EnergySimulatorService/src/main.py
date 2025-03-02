import os
import time
import json
from dotenv import load_dotenv
from loguru import logger

import paho.mqtt.client as paho
from paho.mqtt.enums import CallbackAPIVersion


from EnergySimulation.Base_simulation import BaseSimulation
from EnergySimulation.BuildingConfigration import BuildingConfiguration
from EnergySimulation.BuildingEnergySimulation import BuildingEnergySimulation

logger.add("./Logs/EnergySimulator_Publisher_Logs.log",rotation="100 MB",retention="2 days",compression="zip",level="INFO")

load_dotenv()

MQTT_USER = os.getenv("HIVEMQ_USER")
MQTT_PASS = os.getenv("HIVEMQ_PASS")
MQTT_HOST = os.getenv("HIVEMQ_HOST")
MQTT_PORT = 8883

def on_publish(client, userdata, mid, reason_code, properties):
    logger.info(f"Message published. MID: {mid}, Reason: {reason_code}",file="./Logs/EnergySimulator_Publisher_Logs.log")

def publish_energy_data(client, data):
    building_id = data["building_id"]
    occupant_count = data["occupant_count"]

    # IT
    it_topic = f"Waterloo/Warehouse/{building_id}/Energy/IT"
    it_payload = {
        "building_id": building_id,
        "occupant_count": occupant_count,
        "consumption_kW": data["IT_energy"]
    }
    client.publish(it_topic, json.dumps(it_payload), qos=1)
    logger.info(f"Published IT -> {it_topic}: {it_payload}")

    # Lighting
    light_topic = f"Waterloo/Warehouse/{building_id}/Energy/Lighting"
    light_payload = {
        "building_id": building_id,
        "occupant_count": occupant_count,
        "consumption_kW": data["Lighting_energy"]
    }
    client.publish(light_topic, json.dumps(light_payload), qos=1)
    logger.info(f"Published Lighting -> {light_topic}: {light_payload}")

    # Ventilation
    vent_topic = f"Waterloo/Warehouse/{building_id}/Energy/Ventilation"
    vent_payload = {
        "building_id": building_id,
        "occupant_count": occupant_count,
        "consumption_kW": data["Ventilation_energy"]
    }
    client.publish(vent_topic, json.dumps(vent_payload), qos=1)
    logger.info(f"Published Ventilation -> {vent_topic}: {vent_payload}")

    # HVAC
    hvac_topic = f"Waterloo/Warehouse/{building_id}/Energy/HVAC"
    hvac_payload = {
        "building_id": building_id,
        "occupant_count": occupant_count,
        "consumption_kW": data["HVAC_energy"]
    }
    client.publish(hvac_topic, json.dumps(hvac_payload), qos=1)
    logger.info(f"Published HVAC -> {hvac_topic}: {hvac_payload}")

    # Transport
    transport_topic = f"Waterloo/Warehouse/{building_id}/Energy/Transport"
    transport_payload = {
        "building_id": building_id,
        "occupant_count": occupant_count,
        "consumption_kW": data["Transport_energy"]
    }
    client.publish(transport_topic, json.dumps(transport_payload), qos=1)
    logger.info(f"Published Transport -> {transport_topic}: {transport_payload}")

def main():
    # MQTT setup
    client = paho.Client(callback_api_version=CallbackAPIVersion.VERSION2,client_id="",clean_session=True)
    client.tls_set()
    client.username_pw_set(MQTT_USER, MQTT_PASS)
    client.on_publish = on_publish

    client.connect(MQTT_HOST, MQTT_PORT)
    client.loop_start()

    # Create building configurations
    building_configs = [
        BuildingConfiguration(building_id="BuildingA",occupant_capacity=100,hvac_power_multiplier=1.0),
        BuildingConfiguration(building_id="BuildingB",occupant_capacity=200,hvac_power_multiplier=1.2
        )
    ]

    # Create one simulation for each building
    simulations = [BuildingEnergySimulation(cfg) for cfg in building_configs]

    try:
        while True:
            for sim in simulations:
                sim_data = sim.update_simulation()
                publish_energy_data(client, sim_data)
            time.sleep(1200)

    except KeyboardInterrupt:
        logger.info("Exiting multi-building Energysimulation",file="./Logs/EnergySimulator_Publisher_Logs.log")
    finally:
        client.loop_stop()
        client.disconnect()
        logger.warning("disconnected multi-building Energysimulation",file="./Logs/EnergySimulator_Publisher_Logs.log")

if __name__ == "__main__":
    main()
