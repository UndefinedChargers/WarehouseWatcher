# FILE : inventory.py
# PROGRAMMER : Yujung Park
# FIRST VERSION : 2024-02-10
# DESCRIPTION : this program makes Odoo external api call to get the inventory onhand.

import os
import sys
import xmlrpc.client
import paho.mqtt.client as paho
import json
from loguru import logger # type: ignore
from paho.mqtt.enums import CallbackAPIVersion
from dataclasses import dataclass
from collections import defaultdict
from dotenv import load_dotenv

load_dotenv()
MQTT_USER =os.getenv("HIVEMQ_USER")
MQTT_PASSWORD = os.getenv("HIVEMQ_PASS")
MQTT_HOST = os.getenv("HIVEMQ_HOST")
ERP_URL = os.getenv("ERP_URL")
ERP_DB = os.getenv("ERP_DB")
EPR_USERNAME = os.getenv("ERP_USERNAME")
ERP_PASSWORD = os.getenv("ERP_PASSWORD")

inventory_topic = 'WW/Waterloo/Warehouse/Inventory/'
status_topic = 'WW/App/Front/Status'
inventorydata = defaultdict(list)
client = paho.Client(callback_api_version=CallbackAPIVersion.VERSION2)
logger.add(sys.stdout, format="{time} {level} --- {message}")
logger.add('wwlog.log', rotation='100 MB', retention=1, level="INFO")

@dataclass
class Product:
    location: str
    product: str
    description: str
    batch: str
    quantity: str
    ghs: str

# https://www.odoo.com/documentation/18.0/developer/reference/external_api.html

@logger.catch
def get_inventory():
  common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(ERP_URL))
  uid = common.authenticate(ERP_DB, EPR_USERNAME, ERP_PASSWORD, {})

  models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(ERP_URL))
  search_result = models.execute_kw(ERP_DB, uid, ERP_PASSWORD, 'stock.quant', 'search_read', [[['on_hand', '=', True]]], {'fields': ['product_id', 'quantity', ], 'limit': 100})
  # print(type(search_result))
 
  for res in search_result:
    item = res.get('product_id')
    quantity = res.get('quantity')
    ref, prod = item[1].split('] ', maxsplit=1)
    reference = ref.replace('[', '')
    desc, lot, ghsclass, loc = reference.split('_', maxsplit = 3)
    inv_obj = Product(loc, prod, desc, lot, quantity, ghsclass)
    inventorydata[loc].append(inv_obj)


# https://github.com/hivemq-cloud/paho-mqtt-client-example/blob/master/simple_example.py
def on_connect(client, userdata, flags, rc, properties=None):
  logger.info(f"CONNACK received with code {rc}")

def on_publish(client, userdata, mid, properties=None):
  logger.info("mid: " + str(mid))

def on_subscribe(client, userdata, mid, granted_qos, properties=None):
  logger.info(f"Subscribed: {mid} {granted_qos} {properties}")

def on_message(client, userdata, msg):
  if (msg.topic == status_topic):
    get_inventory()
    update_inventory(client=theclient, tpc=inventory_topic)
    # logger.info(f"{msg.topic} {str(msg.qos)} {str(msg.payload)}")

@logger.catch
def sub_client(tpc: str):
  client.tls_set()
  client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
  client.on_subscribe = on_subscribe
  client.on_message = on_message
  client.connect(MQTT_HOST, 8883)
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

@logger.catch
def update_inventory(client: paho.Client, tpc: str):
  # max packet is 256 mb 
  for key, val in inventorydata.items():
    topic = tpc + key
    payload = json.dumps([obj.__dict__ for obj in val]) #https://stackoverflow.com/questions/26033239/list-of-objects-to-json-with-python
    client.publish(topic, payload, qos=1, retain=True)
  inventorydata.clear()


if __name__ == '__main__':
  thetopic = 'WW/App/Front/Status'
  sub_client(thetopic)