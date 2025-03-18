
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
# room=25
# refre=-3.3
# freezer=-18
# __init__(self,sensor_name,drain_cycle,set_temp)
sensors= {
    "Room": thermostat("Warehouse_thermostat_Sensor",10,25),
    "Refrigerator": thermostat("Refrigerator",150,-3.3),
    "Freezer": thermostat("Freezer",200,-18),
    "AirQuality_warehouse": AirQualitySensor("Warehouse_Air_Sensor", (1,100), (300, 1000), (0, 500),20),
    "humidity_warehouse":HumiditySensor("Warehouse_Humidity_Sensor", thermostat("Room",25,10), (35,55),2)

}
def on_publish(client, userdata, mid, reason_code, properties):
    #print(f"Message published. MID: {mid}, Reason Code: {reason_code}")
    logger.info(f"Message published. MID: {mid}, Reason Code: {reason_code}",file="./Logs/Publisher_Logs.log")

def on_message(client, userdata, msg):
    logger.info(f"[MQTT] Return message on {msg.topic}: {msg.payload.decode('utf-8')}")

# function name:on_control_message(client,userdata,msg)
# Description:This function  is for the control calls from the UI
# Parameter:void:self
# return:none
def on_control_message(client, userdata, msg):
   
    try:
        payload_str = msg.payload.decode("utf-8")
        payload = json.loads(payload_str)
        sensor_name = payload.get("sensor_name")
        action = payload.get("action")

        if sensor_name in sensors:
            sensor = sensors[sensor_name]
            logger.info(f"[CONTROL] Received action '{action}' for sensor '{sensor_name}'")

            
            if action == "set_battery":
              battery_enabled = payload.get("battery_enabled", True)
              if not battery_enabled:
                  sensor.battery = 0
                  sensor.set_battery_UI=True
              else:
                  sensor.battery = 100
                  sensor.set_battery_UI=False

              logger.info(f"[CONTROL] Battery for {sensor_name} set to {sensor.battery}")

            #  increase data functions
            elif action == "increase_data":
                field = payload.get("field")

                if field == "Temperature" and hasattr(sensor, "set_increment_temp_one"):
                    
                    sensor.set_increment_temp_one()
                    logger.info(f"[CONTROL] Increased Temperature for {sensor_name} to {sensor.manual_temperature}")
                elif field=="PM2.5" and hasattr(sensor,"set_increment_pm_five"):
                    sensor.set_increment_pm_five()
                    logger.info(f"[CONTROL] Increased PM for {sensor_name} to {sensor.setPm25}")
                elif field=="CO2" and hasattr(sensor,"set_increment_co2_100"):
                    sensor.set_increment_co2_100()
                    logger.info(f"[CONTROL] Increased C02 for {sensor_name} to {sensor.setCO2}")
                elif field=="VOC" and hasattr(sensor,"set_increment_VOC_50"):
                    sensor.set_increment_VOC_50()
                    logger.info(f"[CONTROL] Increased VOC for {sensor_name} to {sensor.setVOC}")

                elif field=="Humidity" and hasattr(sensor,"set_increment_humidity_5"):
                    sensor.set_increment_humidity_5()
                    logger.info(f"[CONTROL] Incremented  Humidity for {sensor_name} to {sensor.setHumid}")
                else:
                    logger.warning(f"[CONTROL] Increase action not supported for field '{field}' for {sensor_name}")
            # these include decrease data functions
            elif action == "decrease_data":
                
                field = payload.get("field")
                if field == "Temperature" and hasattr(sensor, "set_decrement_temp_one"):
                    sensor.set_decrement_temp_one()
                    logger.info(f"[CONTROL] Decreased Temperature for {sensor_name} to {sensor.manual_temperature}")
                
                elif field=="PM2.5" and hasattr(sensor,"set_decrement_pm_five"):
                    sensor.set_decrement_pm_five()
                    logger.info(f"[CONTROL] Decremented PM for {sensor_name} to {sensor.setpm25}")

                elif field=="CO2" and hasattr(sensor,"set_decrement_co2_100"):
                    sensor.set_decrement_co2_100()
                    logger.info(f"[CONTROL] Decremented C02 for {sensor_name} to {sensor.setPm25}")

                elif field=="VOC" and hasattr(sensor,"set_decrement_VOC_50"):
                    sensor.set_decrement_VOC_50()
                    logger.info(f"[CONTROL] Decremented VOC for {sensor_name} to {sensor.setVOC}")

                elif field=="Humidity" and hasattr(sensor,"set_decrement_humidity_5"):
                    sensor.set_decrement_humidity_5()
                    logger.info(f"[CONTROL] Decremented Humidity for {sensor_name} to {sensor.setHumid}")
                else:
                    logger.warning(f"[CONTROL] Decrease action not supported for field '{field}' for {sensor_name}")
            else:
                logger.warning(f"[CONTROL] Unknown action '{action}' for {sensor_name}")
        else:
            logger.warning(f"[CONTROL] Sensor '{sensor_name}' not found among known sensors.")
    except Exception as e:
        logger.error("Error processing control message: " + str(e))


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
    client.on_message=on_message

    client.message_callback_add("Waterloo/Warehouse/Control/#",on_control_message)
    client.connect(host, 8883)
    client.subscribe("Waterloo/Warehouse/#") #subscriber
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