# FILE : main.py
# PROGRAMMER : William Anderson
# FIRST VERSION : 2025-03-23
# DESCRIPTION : Communicates the current threshold data to the grafana api to update panel thresholds.

import os
from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)


# Authorization token in header
headers = {
    "Authorization": f'Bearer {os.getenv("GRAFANA_TOKEN")}',
    "Content-Type": "application/json"
}

#   Set grafana dashboard urls
DASHBOARD_ENERGY_2DAYS = os.getenv("DASHBOARD_ENERGY_2DAYS")
DASHBOARD_ENERGY_30DAYS = os.getenv("DASHBOARD_ENERGY_30DAYS")
DASHBOARD_ENV_REALTIME = os.getenv("DASHBOARD_ENV_REALTIME")
DASHBOARD_ENV_1HOUR = os.getenv("DASHBOARD_ENV_1HOUR")
DASHBOARD_ENV_30DAYS = os.getenv("DASHBOARD_ENV_30DAYS")
DASHBOARD_PUT_URL = os.getenv("DASHBOARD_PUT_URL")
#   Set sensor ids
SENSOR1_TEMP = os.getenv("SENSOR1_TEMP")
SENSOR2_TEMP = os.getenv("SENSOR2_TEMP")
SENSOR3_TEMP = os.getenv("SENSOR3_TEMP")
SENSOR1_AIR = os.getenv("SENSOR1_AIR")
SENSOR1_HUMIDITY = os.getenv("SENSOR1_HUMIDITY")
#   Set dashboard panel ids
PANEL_SENSOR1_TEMP_ENV_REALTIME = os.getenv("PANEL_SENSOR1_TEMP_ENV_REALTIME")
PANEL_SENSOR2_TEMP_ENV_REALTIME = os.getenv("PANEL_SENSOR2_TEMP_ENV_REALTIME")
PANEL_SENSOR3_TEMP_ENV_REALTIME = os.getenv("PANEL_SENSOR3_TEMP_ENV_REALTIME")
PANEL_SENSOR1_AIR_ENV_REALTIME = os.getenv("PANEL_SENSOR1_AIR_ENV_REALTIME")
PANEL_SENSOR1_AIR_ENV_1HOUR = os.getenv("PANEL_SENSOR1_AIR_ENV_1HOUR")
PANEL_SENSOR1_AIR_ENV_30DAYS = os.getenv("PANEL_SENSOR1_AIR_ENV_30DAYS")
PANEL_SENSOR1_HUMIDITY_REALTIME = os.getenv("PANEL_SENSOR1_HUMIDITY_REALTIME")
PANEL_SENSOR1_HUMIDITY_1HOUR = os.getenv("PANEL_SENSOR1_HUMIDITY_1HOUR")
PANEL_SENSOR1_HUMIDITY_30DAYS = os.getenv("PANEL_SENSOR1_HUMIDITY_30DAYS")


#   Function:       updateThresholds
#   Description:    Gets new threshold data on a single sensor from the front end.
#                   Sends the data to the right post method
#
#   This is the route for the front-end to use to update thresholds
@app.route('/grafana_threshold_update', methods=['POST'])
def determineThresholds():
    #   Get threshold data from the frontend
    threshold_data = request.json
    print(f"Data from frontend: {threshold_data}")

    sensor_id = threshold_data.get("sensor_id")
    range_min = threshold_data.get("range_min")
    range_max = threshold_data.get("range_max")

    #   Determine which thresholds to change in POST and execute
    if sensor_id == SENSOR1_TEMP:
        post_response = postSensor1Temp(range_min, range_max)
    elif sensor_id == SENSOR2_TEMP:
        post_response = postSensor2Temp(range_min, range_max)
    elif sensor_id == SENSOR3_TEMP:
        post_response = postSensor3Temp(range_min, range_max)
    elif sensor_id == SENSOR1_AIR:
        post_response = postSensor1Air(range_min, range_max)
    elif sensor_id == SENSOR1_HUMIDITY:
        post_response = postSensor1Humidity(range_min, range_max)
    else:
        post_response = None

    #   Just debugging info
    if post_response == None:
        print("sensor_id incorrect.")
    else:
        print(f"Status Code: {post_response.status_code}, Response Text: {post_response.text}")


def postSensor1Temp(min, max):
    #   Get Dashboard data 
    get_response = requests.get(DASHBOARD_ENV_REALTIME, headers=headers, verify=False)

    if get_response.status_code == 200:
        try: 
            dashboardData = get_response.json()

            panelData = dashboardData.get('dashboard', {}).get('panels', [])
            #   Drill down to thresholds on a specific panel
            for panel in panelData:
                if panel.get("id") == PANEL_SENSOR1_TEMP_ENV_REALTIME:
                    if 'fieldConfig' in panel and 'defaults' in panel['fieldConfig']:
                        panel['fieldConfig']['defaults']['thresholds'] = {
                            "mode": "absolute",
                            "steps": [
                                {"color": "red", "value": None},
                                {"color": "green", "value": min},
                                {"color": "red", "value": max}
                            ]
                    }  

             #   Need to update the version and set to overwrite for the api to work
            dashboardData["dashboard"]["version"] += 1
            payload = {
                "dashboard": dashboardData["dashboard"],
                "overwrite": True
            }

            #   Send POST
            return requests.post(DASHBOARD_PUT_URL, headers=headers, json=payload, verify=False)

        except ValueError:
            return get_response.text
    else:
        return "Failure", 400

def postSensor2Temp(min, max):
    #   Get Dashboard data 
    get_response = requests.get(DASHBOARD_ENV_REALTIME, headers=headers, verify=False)

    if get_response.status_code == 200:
        try: 
            dashboardData = get_response.json()

            panelData = dashboardData.get('dashboard', {}).get('panels', [])
            #   Drill down to thresholds on a specific panel
            for panel in panelData:
                if panel.get("id") == PANEL_SENSOR2_TEMP_ENV_REALTIME:
                    if 'fieldConfig' in panel and 'defaults' in panel['fieldConfig']:
                        panel['fieldConfig']['defaults']['thresholds'] = {
                            "mode": "absolute",
                            "steps": [
                                {"color": "red", "value": None},
                                {"color": "green", "value": min},
                                {"color": "red", "value": max}
                            ]
                    }  

            #   Need to update the version and set to overwrite for the api to work
            dashboardData["dashboard"]["version"] += 1
            payload = {
                "dashboard": dashboardData["dashboard"],
                "overwrite": True
            }

            #   Send POST
            return requests.post(DASHBOARD_PUT_URL, headers=headers, json=payload, verify=False)

        except ValueError:
            return get_response.text
    else:
        return "Failure", 400

def postSensor3Temp(min, max):
    #   Get Dashboard data 
    get_response = requests.get(DASHBOARD_ENV_REALTIME, headers=headers, verify=False)

    if get_response.status_code == 200:
        try: 
            dashboardData = get_response.json()

            panelData = dashboardData.get('dashboard', {}).get('panels', [])
            #   Drill down to thresholds on a specific panel
            for panel in panelData:
                if panel.get("id") == PANEL_SENSOR3_TEMP_ENV_REALTIME:
                    if 'fieldConfig' in panel and 'defaults' in panel['fieldConfig']:
                        panel['fieldConfig']['defaults']['thresholds'] = {
                            "mode": "absolute",
                            "steps": [
                                {"color": "red", "value": None},
                                {"color": "green", "value": min},
                                {"color": "red", "value": max}
                            ]
                    }  

             #   Need to update the version and set to overwrite for the api to work
            dashboardData["dashboard"]["version"] += 1
            payload = {
                "dashboard": dashboardData["dashboard"],
                "overwrite": True
            }

            #   Send POST
            return requests.post(DASHBOARD_PUT_URL, headers=headers, json=payload, verify=False)

        except ValueError:
            return get_response.text
    else:
        return "Failure", 400

def postSensor1Air(min, max):
    return

def postSensor1Humidity(min, max):
    return

#   Main app
if __name__ == '__main__':
    app.run(debug=True)