# FILE :mqtt_handler.py
# PROJECT :Warehouse Watcher
# PROGRAMMER : Amel Korandippillil Sunil
# DESCRIPTION :This file basically used for the intial connectivity of the mqtt server

import threading
import paho.mqtt.client as paho
from paho.mqtt.enums import CallbackAPIVersion

class MQTTHandler:
#     def __init__(self, host, user, password, on_message_callback, on_connect_callback=None):
    def __init__(self, host, user, password):
         self.host = host
         self.host = host
         self.user = user
         self.password = password
        #  self.on_message_callback = on_message_callback
        #  self.on_connect_callback = on_connect_callback
         self.client = paho.Client(callback_api_version= CallbackAPIVersion.VERSION2, client_id="", clean_session=True)
         self.on_message_callback = None
         self.client.on_message = self._on_message_internal   
        # Configure TLS & authentication
         self.client.tls_set()
         self.client.username_pw_set(user, password)

        # # Assign callbacks
        #  self.client.on_message = self._internal_on_message
        #  self.client.on_connect = self._internal_on_connect

        
         

    # function name:connect_and_start
    # Description: this function is used to connect and start the service
    # Parameter: void:self
    # return: None
    def connect_and_start(self):
        self.client.connect(self.host, 8883)
        self.thread = threading.Thread(target=self.client.loop_forever, daemon=True)
        self.thread.start()
    # function name:publish
    # Description:This function is used to publish the data
    # Parameter: void:self
    # return: None
    def publish(self, topic, payload, qos=1):
        self.client.publish(topic, payload, qos=qos)

    # function name:subscribe
    # Description: This function is used to subscribe the topic
    # Parameter: void:self
    # return: None
    def subscribe(self, topic):
        self.client.subscribe(topic)

    # function name:disconnect
    # Description: This function is used to disconnect the client
    # Parameter: void:self
    # return: None
    def disconnect(self):
        self.client.disconnect()

    # function name: set_message_callback
    # Description: This function registers a user-defined callback to be triggered when an MQTT message is received.
    # Parameter: void:self, callback:function that takes topic (str) and payload (str) as parameters
    # return:
    def set_message_callback(self, callback):
        self.on_message_callback = callback

     # function name: _on_message_internal
    # Description: This internal function is triggered on message arrival; it calls the registered callback with the topic and decoded message payload.
    # Parameter: void:self, client:MQTT client instance, userdata:user-defined data, msg:MQTTMessage object
    # return:
    def _on_message_internal(self, client, userdata, msg):
        if self.on_message_callback:
            self.on_message_callback(msg.topic, msg.payload.decode('utf-8'))


  