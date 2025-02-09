# FILE : influxClient.py
# PROGRAMMER : William Anderson
# FIRST VERSION : 2025-02-08
# DESCRIPTION : Connects to the influxDB database and can parse and store incoming 
#               sensor data.

import os, time
from influxdb_client_3 import InfluxDBClient3, Point
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("INFLUXDB_TOKEN")
org = os.getenv("INFLUXDB_ORG")
host = os.getenv("INFLUXDB_HOST")
database = "setup_test"

client = InfluxDBClient3(host=host, token=token, org=org)

def store_data(topic, data):
  print("Parsing JSON data.")

  # - Should I add a default value to .get() calls 
  sensor_name = data.get('sensor_name') 
  sensor_data = data.get('data', {})

  point = (
    Point("sensor_data") 
      .tag("sensor_name", sensor_name)  
      .field("topic", topic)
      .field("data_message_guid", sensor_data.get('MessageID'))
      .field("sensor_id", sensor_data.get('SensorID'))
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
