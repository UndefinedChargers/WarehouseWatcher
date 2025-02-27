
import paho.mqtt.client as paho
import time
from paho.mqtt.enums import CallbackAPIVersion
from Sensors.thermostat import thermostat
import json
from dotenv import load_dotenv
from Sensors.air_quality import AirQualitySensor
from Sensors.humidity import HumiditySensor
from loguru import logger
import os
 
logger.add("./Logs/Publisher_Logs.log", rotation="100 MB", retention="2 days", compression="zip", level="INFO")
load_dotenv() # used for setting up the environment variable for the project


user =os.getenv("HIVEMQ_USER")
password = os.getenv("HIVEMQ_PASS")
host = os.getenv("HIVEMQ_HOST")

# TOPICS={
#     "thermostat": "Waterloo/Warehouse/Thermostat/",
#     "AirQualitySensor":"Waterloo/Warehouse/AirQualitySensor/"

# }

# format for sensors
# location :thermostat(sensor_name,temp_range,drain_cycle)
# location: AirQualitySensor(sensor_name, pm_range=(5, 100), co2_range=(300, 1000), voc_range=(0, 500), drain_cycle=100)
sensors= {
    "Room": thermostat("Warehouse_thermostat_Sensor", (20.0, 25.0),10),
    "Refrigerator": thermostat("Refrigerator", (2.0, 5.0),150),
    "Freezer": thermostat("Freezer", (-18.0, -15.0),200),
    "AirQuality_warehouse": AirQualitySensor("Warehouse_Air_Sensor", (1,100), (300, 1000), (0, 500),20),
    "humidity_warehouse":HumiditySensor("Warehouse_Humidity_Sensor", thermostat("Room", (20.0, 25.0),10), (35,55),2)

}
def on_publish(client, userdata, mid, reason_code, properties):
    #print(f"Message published. MID: {mid}, Reason Code: {reason_code}")
    logger.info(f"Message published. MID: {mid}, Reason Code: {reason_code}",file="./Logs/Publisher_Logs.log")

# function name:publish_data(client)
# Description:This function  is used to publish all the sensor data(maybe in  the future if we add motion sensor then it will include that too)
# Parameter:void:self
# return:none
def publish_data(client):
   for sensor_name,sensor_instance in sensors.items():
      data=sensor_instance.generate_sensor_data()
      if data is None:
         sensor_instance.restart_sensor()
         continue

      final_result=json.loads(data)["Result"][0]
      sensor_Data={
         "sensor_name":sensor_name,
         "data":final_result
      }

    #   theTopic=TOPICS["Thermostat"] + sensor_name
    #   theTopic=TOPICS.get(sensor_name,f"Waterloo/Warehouse/{sensor_name}")
    #   payload=json.dumps(sensor_Data)
    #   client.publish(theTopic, payload, qos=1)


      sensor_type = sensor_instance.__class__.__name__ 
      theTopic = f"Waterloo/Warehouse/{sensor_type}/{sensor_name}"
      payload = json.dumps(sensor_Data)
      client.publish(theTopic, payload, qos=1)
    #   print(f"Published >> {theTopic}:{payload}")
      logger.info(f"Published >>{theTopic}",file="./Logs/Publisher_Logs.log")
      



if __name__ == "__main__":
    client = paho.Client(callback_api_version= CallbackAPIVersion.VERSION2, client_id="", clean_session=True)
    client.tls_set() 
    client.username_pw_set(user, password)

    client.on_publish = on_publish
    client.connect(host, 8883)
    client.loop_start()
    try:
        # for i in range(1,4): # test code
        while True:
            publish_data(client)
            time.sleep(3)
    except KeyboardInterrupt:
    #  print("Exiting...")
     logger.info("Exiting the service",file="./Logs/Publisher_Logs.log")
    finally:
     client.loop_stop()  
     client.disconnect()  # Disconnect the client