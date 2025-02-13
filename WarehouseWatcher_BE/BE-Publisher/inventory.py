# FILE : inventory.py
# PROGRAMMER : Yujung Park
# FIRST VERSION : 2024-02-10
# DESCRIPTION : 

import os, time
import sys
import xmlrpc.client
import paho.mqtt.client as paho
import json
from loguru import logger
from paho.mqtt.enums import CallbackAPIVersion
from collections import defaultdict
from dotenv import load_dotenv

load_dotenv()
mqtt_user =os.getenv("HIVEMQ_USER")
mqtt_password = os.getenv("HIVEMQ_PASS")
mqtt_host = os.getenv("HIVEMQ_HOST")
erp_url = os.getenv("ERP_URL")
erp_db = os.getenv("ERP_DB")
erp_username = os.getenv("ERP_USERNAME")
erp_password = os.getenv("ERP_PASSWORD")

testval = [{'id': 14, 'product_id': [7, '[Bora bipolar disector_152648_ghs07_s1.l01] WW-PD-J86'], 'quantity': 50.0}, 
           {'id': 15, 'product_id': [8, '[JangGoon litesizer_759468_ghs01_s1.l02] WW-PD-X92 '], 'quantity': 47.0}, 
           {'id': 17, 'product_id': [9, '[Jayuro ionQX_798435_ghs01_s1.l03] WW-PD-K78'], 'quantity': 37.0}, 
           {'id': 35, 'product_id': [16, '[Cheollian spectrometer_645829_ghs07_s2.l01] WW-PD-A81'], 'quantity': 57.0}, 
           {'id': 37, 'product_id': [17, '[Gangnam rigetti_799161_ghs01_s2.l05] WW-PD-G98'], 'quantity': 47.0}, 
           {'id': 39, 'product_id': [19, '[Yangjae arqit_415777_ghs01_s2.l09] WW-PD-A72'], 'quantity': 50.0}, 
           {'id': 30, 'product_id': [2, '[Yanghwa litesizerII_570468_ghs01_s2.l02] WW-PD-X31'], 'quantity': 44.0}, 
           {'id': 31, 'product_id': [4, '[Cheongdam ionQX_978435_ghs01_s2.l03] WW-PD-K77'], 'quantity': 73.0}, 
           {'id': 33, 'product_id': [6, '[Yeongdong molecular analyzer_488978_ghs02_s2.l04] WW-PD-B54'], 'quantity': 45.0}, 
           {'id': 35, 'product_id': [16, '[Cheollian spectrometer_645829_ghs07_s2.l01] WW-PD-A81'], 'quantity': 57.0}, 
           {'id': 37, 'product_id': [17, '[Gangnam rigetti_799161_ghs01_s2.l05] WW-PD-G98'], 'quantity': 47.0}, 
           {'id': 39, 'product_id': [19, '[Yangjae arqit_415777_ghs01_s2.l09] WW-PD-A72'], 'quantity': 39.0}, 
           {'id': 41, 'product_id': [20, '[Daecheong fediance_366892_ghs01_s2.l10] WW-PD-D90'], 'quantity': 56.0}, ]

inventorydata = defaultdict(list)
base_topic = 'Waterloo/Warehouse/Inventory/'

class Product:
  def __init__(self, location, product, description, batch, qty, ghs):
    self.location = location
    self.product = product
    self.description = description
    self.batch = batch
    self.quantity = qty
    self.ghs = ghs


# https://www.odoo.com/documentation/18.0/developer/reference/external_api.html
def getInventory():
  common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(erp_url))
  uid = common.authenticate(erp_db, erp_username, erp_password, {})

  if uid:
    print("authentication success")
  else:
    print("authentication failed")

  models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(erp_url))
  search_result = models.execute_kw(erp_db, uid, erp_password, 'stock.quant', 'search_read', [[['on_hand', '=', True]]], {'fields': ['product_id', 'quantity', ], 'limit': 100})
  # print(type(search_result))

  # for res in search_result:  
  for res in testval:
    item = res.get('product_id')
    qty = res.get('quantity')
    ref, prod = item[1].split('] ', maxsplit=1)
    reference = ref.replace('[', '')
    desc, lot, ghsclass, loc = reference.split('_', maxsplit = 3)
    inv_obj = Product(location=loc, product=prod, description=desc, batch=lot, quantity=qty, ghs=ghsclass)
    inventorydata[loc].append(inv_obj)


# https://github.com/hivemq-cloud/paho-mqtt-client-example/blob/master/simple_example.py
# setting callbacks for different events to see if it works, print the message etc.
def on_connect(client, userdata, flags, rc, properties=None):
  print(f"CONNACK received with code {rc}")

# with this callback you can see if your publish was successful
def on_publish(client, userdata, mid, properties=None):
  print("mid: " + str(mid))

def on_subscribe(client, userdata, mid, granted_qos, properties=None):
  print(f"Subscribed: {mid} {granted_qos} {properties}")

def on_message(client, userdata, msg):
  # if topic == WW/App/Front/Status, then 
  # call function updateInventory(msg.topic, msg.payload); 
  print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

def subClient(tpc):
  client = client = paho.Client(callback_api_version=CallbackAPIVersion.VERSION2)
  client.tls_set()
  client.username_pw_set(mqtt_user, mqtt_password)
  client.on_subscribe = on_subscribe
  client.on_message = on_message
  client.connect(mqtt_host, 8883)
  client.subscribe(tpc, qos=1)
  client.loop_start()
  
  try:
    while True:
      pass
  except KeyboardInterrupt:
    pass
  finally:
    client.loop_stop() 
    client.disconnect()

def updateInventory(client, tpc, payload):
  # max packet is 256 mb 
  for key, val in inventorydata.items():
    topic = base_topic + key
    payload = json.dumps([obj.__dict__ for obj in val]) #https://stackoverflow.com/questions/26033239/list-of-objects-to-json-with-python
    client.publish(topic, payload, qos=1, retain=True)

  inventorydata.clear()


if __name__ == '__main__':
  getInventory()
  # subClient(topic)

