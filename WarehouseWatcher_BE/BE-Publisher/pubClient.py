# FILE : pubClient.py
# PROGRAMMER : Yujung Park
# DESCRIPTION : pubClient.py connects to the host, creates a random value between 24 and 30 and makes the mock thermostat temperature message and publishes the message on the topic.
# https://github.com/eclipse-paho/paho.mqtt.python

import paho.mqtt.client as paho
import time
import random
from paho.mqtt.enums import CallbackAPIVersion
import configparser
from Sensors.thermostat import thermostat
import json
from dotenv import load_dotenv
from Sensors.air_quality import AirQualitySensor

import os
 

load_dotenv() # used for setting up the environment variable for the project


user =os.getenv("HIVEMQ_USER")
password = os.getenv("HIVEMQ_PASS")
host = os.getenv("HIVEMQ_HOST")

TOPICS={
    "allsensor_data": "Waterloo/Warehouse/allsensor_data",
    "thermostat": "Waterloo/Warehouse/Thermostat/",
    "AirQualitySensor":"Waterloo/Warehouse/AirQualitySensor/"

}

# format for sensors
# location :thermostat(sensor_name,temp_range,drain_cycle)
# location: AirQualitySensor(sensor_name, pm_range=(5, 100), co2_range=(300, 1000), voc_range=(0, 500), drain_cycle=100)
sensors= {
    "Room": thermostat("Room", (20.0, 25.0),10),
    "Refrigerator": thermostat("Refrigerator", (2.0, 5.0),150),
    "Freezer": thermostat("Freezer", (-18.0, -15.0),200),
    "AirQuality_warehouse": AirQualitySensor("Warehouse_Air_Sensor", (1,100), (300, 1000), (0, 500),20)

}

def on_publish(client, userdata, mid, reason_code, properties):
    print(f"Message published. MID: {mid}, Reason Code: {reason_code}")


# function name:publish_data(client)
# Description:This function  is used to publish all the sensor data(maybe in  the future if we add motion sensor then it will include that too)
# Parameter:void:self
# return:none
def publish_data(client):
   for sensor_name,sensor_instance in sensors.items():
      data=sensor_instance.generate_sensor_data()
      if data is None:
         sensor_instance.restart_sensor()
         if isinstance(sensor_instance, AirQualitySensor):# replace with a new AirQualitySensor
                sensors[sensor_name] = AirQualitySensor(sensor_name)  
         elif isinstance(sensor_instance, thermostat):
                sensors[sensor_name] = thermostat(sensor_name, (2.0, 5.0), 150)  # Replace with new Thermostat instance

      
         continue

      final_result=json.loads(data)["Result"][0]
      sensor_Data={
         "sensor_name":sensor_name,
         "data":final_result
      }

    #   theTopic=TOPICS["Thermostat"] + sensor_name
      theTopic=TOPICS.get(sensor_name,f"Waterloo/Warehouse/{sensor_name}")
      payload=json.dumps(sensor_Data)
      client.publish(theTopic, payload, qos=1)
      print(f"Published >> {theTopic}:{payload}")
      print("=============================================================")



if __name__ == "__main__":
    client = paho.Client(callback_api_version= CallbackAPIVersion.VERSION2, client_id="", clean_session=True)
    client.tls_set() 
    client.username_pw_set(user, password)

    client.on_publish = on_publish
    client.connect(host, 8883)
    client.loop_start()
    try:
        # for i in range(1,4): # test code
        while TOPICS:
            publish_data(client)
            time.sleep(3)
    except KeyboardInterrupt:
     print("Exiting...")
    finally:
     client.loop_stop()  
     client.disconnect()  # Disconnect the client

