# FILE : influxClient.py
# PROGRAMMER : Yujung Park
# FIRST VERSION : 2024-02-03
# DESCRIPTION : 

import os, time
from influxdb_client_3 import InfluxDBClient3, Point
from dotenv import load_dotenv


def main():

  load_dotenv()

  token = os.getenv("INFLUXDB_TOKEN")
  org = "WW"
  host = "https://us-east-1-1.aws.cloud2.influxdata.com"

  client = InfluxDBClient3(host=host, token=token, org=org)
  database="WW"

  data = {
    "point1": {
      "location": "Klamath",
      "species": "bees",
      "count": 23,
    },
    "point2": {
      "location": "Portland",
      "species": "ants",
      "count": 30,
    },
    "point3": {
      "location": "Klamath",
      "species": "bees",
      "count": 28,
    },
    "point4": {
      "location": "Portland",
      "species": "ants",
      "count": 32,
    },
    "point5": {
      "location": "Klamath",
      "species": "bees",
      "count": 29,
    },
    "point6": {
      "location": "Portland",
      "species": "ants",
      "count": 40,
    },
  }

  for key in data:
    point = (
      Point("census")
      .tag("location", data[key]["location"])
      .field(data[key]["species"], data[key]["count"])
    )
    client.write(database=database, record=point)
    time.sleep(1) # separate points by 1 second

  print("Complete. Return to the InfluxDB UI.")

if __name__ == '__main__':
  main()