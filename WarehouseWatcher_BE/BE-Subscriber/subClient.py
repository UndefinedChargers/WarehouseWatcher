# FILE : subClient.py
# PROGRAMMER : Yujung Park and William
# FIRST VERSION : 2024-10-20
# DESCRIPTION : subClient.py connects to the host, subscribes to the topic, and prints the message from the topic on the console.
# https://github.com/eclipse-paho/paho.mqtt.python

import paho.mqtt.client as paho
from paho.mqtt.enums import CallbackAPIVersion
import signal
import sys
import os
from dotenv import load_dotenv
import json
import influxClient

load_dotenv()

user = os.getenv("HIVEMQ_USER")
password = os.getenv("HIVEMQ_PASS")
host = os.getenv("HIVEMQ_HOST")

def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print(f"Subscribed: {mid} {granted_qos} {properties}")
    

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))    

    try:
        json_data = json.loads(msg.payload.decode())
        influxClient.store_data(msg.topic, json_data)
    except json.JSONDecodeError:
        print("Invalid JSON data.")


client = paho.Client(callback_api_version=CallbackAPIVersion.VERSION2)

# Enable TLS/SSL
client.tls_set()  # You can also specify certificates if needed
client.username_pw_set(user, password)

client.on_subscribe = on_subscribe
client.on_message = on_message
try:
    client.connect(host, 8883)
except Exception as e:
    print(f"client error: {e}")

client.subscribe(os.getenv("TOPIC_ROOM"), qos=1)
client.subscribe(os.getenv("TOPIC_AIR_QUALITY"), qos=1)
client.subscribe(os.getenv("TOPIC_HUMIDITY"), qos=1)
client.loop_start()

try:
    while True:
        pass
except KeyboardInterrupt:
    pass
    # print("Exiting...")
finally:
    print("Exiting...")
    client.loop_stop()  # Stop the network loop
    client.disconnect()