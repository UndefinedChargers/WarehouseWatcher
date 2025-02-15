# FILE : influxClient.py
# PROGRAMMER : William Anderson
# FIRST VERSION : 2025-02-08
# DESCRIPTION : Connects to the influxDB database and can parse and store incoming 
#               sensor data.

# NOTES
# - Should I add a default value to .get() calls 

import os, time
from influxdb_client_3 import InfluxDBClient3, Point
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("INFLUXDB_TOKEN")
org = os.getenv("INFLUXDB_ORG")
host = os.getenv("INFLUXDB_HOST")
database = "setup_test"

client = InfluxDBClient3(host=host, token=token, org=org)

# Function:     store_data
# Description:  Separates the sensor_name and the JSON data. 
#               Determines which topic it is and calls the topic-specific write function.
def store_data(topic, data):
  print("Parsing JSON data.")

  sensor_name = data.get('sensor_name') 
  sensor_data = data.get('data', {})

  if topic == os.getenv("TOPIC_ROOM"):
    write_temperature_data(topic, sensor_data, sensor_name)
    
  elif topic == os.getenv("TOPIC_AIR_QUALITY"):
    write_air_quality_data(topic, sensor_data, sensor_name)

# Function:     write_temperature_data
# Description:  Parses sensor_data, creates an influxDB point, and writes to the database.
#               Parsing and point construction is specific to temperature data.
def write_temperature_data(topic, sensor_data, sensor_name):
  point = (
      Point(topic) 
        .tag("sensor_name", sensor_name)  
        .tag("sensor_id", sensor_data.get('SensorID'))
        .field("data_message_guid", sensor_data.get('MessageID'))
        .field("message_date", sensor_data.get('MessageDate'))
        .field("state", sensor_data.get('State'))
        .field("signal_strength", sensor_data.get('SignalStrength'))
        .field("voltage", sensor_data.get('Voltage'))
        .field("battery", sensor_data.get('Battery'))
        .field("temperature", sensor_data.get('Data'))
        .field("display_temperature", sensor_data.get('DisplayData')) 
        .field("plot_temperature", sensor_data.get('PlotValue'))
        .field("met_notification_requirements", sensor_data.get('MetNotificationRequirements'))
        .field("gateway_id", sensor_data.get('GatewayID')) 
        .field("data_values", sensor_data.get('DataValues'))
        .field("data_types", sensor_data.get('DataTypes'))
        .field("plot_values", sensor_data.get('PlotValues'))
        .field("plot_labels", sensor_data.get('PlotLabels'))
    )
  client.write(database=database, record=point)

# Function:     write_air_quality_data
# Description:  Parses sensor_data, creates an influxDB point, and writes to the database.
#               Parsing and point construction is specific to air quality data.
def write_air_quality_data(topic, sensor_data, sensor_name):
  point = (
      Point(topic) 
        .tag("sensor_name", sensor_name)  
        .tag("sensor_id", sensor_data.get('SensorID'))
        .field("data_message_guid", sensor_data.get('MessageID'))
        .field("message_date", sensor_data.get('MessageDate'))
        .field("state", sensor_data.get('State'))
        .field("signal_strength", sensor_data.get('SignalStrength'))
        .field("voltage", sensor_data.get('Voltage'))
        .field("battery", sensor_data.get('Battery'))
        .field("pm2.5", sensor_data.get('PM2.5'))
        .field("pm10", sensor_data.get('PM10'))
        .field("co2", sensor_data.get('CO2'))
        .field("voc", sensor_data.get('VOC'))
        .field("met_notification_requirements", sensor_data.get('MetNotificationRequirements'))
        .field("gateway_id", sensor_data.get('GatewayID')) 
        .field("data_type_1", sensor_data.get('DataType1'))
        .field("data_type_2", sensor_data.get('DataType2'))
        .field("data_type_3", sensor_data.get('DataType3'))
        .field("data_type_4", sensor_data.get('DataType4'))
        .field("plot_label_1", sensor_data.get('PlotLabel1'))
        .field("plot_label_2", sensor_data.get('PlotLabel2'))
        .field("plot_label_3", sensor_data.get('PlotLabel3'))
        .field("plot_label_4", sensor_data.get('PlotLabel4'))
    )
  client.write(database=database, record=point)
    

