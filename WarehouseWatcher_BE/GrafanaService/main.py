# FILE : main.py
# PROGRAMMER : William Anderson
# FIRST VERSION : 2025-03-23
# DESCRIPTION : Communicates the current threshold data to the grafana api to update panel thresholds.

import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

CORS(app, origins=["http://localhost:5173"])

# Authorization token in header
headers = {
    "Authorization": f'Bearer {os.getenv("GRAFANA_TOKEN")}',
    "Content-Type": "application/json"
}

PORT = int(os.getenv("PORT"))
#   Set grafana dashboard urls
DASHBOARD_ENERGY_2DAYS = os.getenv("DASHBOARD_ENERGY_2DAYS")
DASHBOARD_ENERGY_30DAYS = os.getenv("DASHBOARD_ENERGY_30DAYS")
DASHBOARD_ENV_REALTIME = os.getenv("DASHBOARD_ENV_REALTIME")
DASHBOARD_ENV_1HOUR = os.getenv("DASHBOARD_ENV_1HOUR")
DASHBOARD_ENV_30DAYS = os.getenv("DASHBOARD_ENV_30DAYS")
DASHBOARD_POST_URL = os.getenv("DASHBOARD_POST_URL")
#   Set sensor ids
SENSOR1_TEMP = os.getenv("SENSOR1_TEMP")
SENSOR2_TEMP = os.getenv("SENSOR2_TEMP")
SENSOR3_TEMP = os.getenv("SENSOR3_TEMP")
SENSOR1_AIR = os.getenv("SENSOR1_AIR")
SENSOR1_HUMIDITY = os.getenv("SENSOR1_HUMIDITY")
#   Set dashboard panel ids
PANEL_SENSOR1_TEMP_ENV_REALTIME = int(os.getenv("PANEL_SENSOR1_TEMP_ENV_REALTIME"))
PANEL_SENSOR1_TEMP_ENV_1HOUR = int(os.getenv("PANEL_SENSOR1_TEMP_ENV_1HOUR"))
PANEL_SENSOR1_TEMP_ENV_30DAYS = int(os.getenv("PANEL_SENSOR1_TEMP_ENV_30DAYS"))
PANEL_SENSOR2_TEMP_ENV_REALTIME = int(os.getenv("PANEL_SENSOR2_TEMP_ENV_REALTIME"))
PANEL_SENSOR2_TEMP_ENV_1HOUR = int(os.getenv("PANEL_SENSOR2_TEMP_ENV_1HOUR"))
PANEL_SENSOR2_TEMP_ENV_30DAYS = int(os.getenv("PANEL_SENSOR2_TEMP_ENV_30DAYS"))
PANEL_SENSOR3_TEMP_ENV_REALTIME = int(os.getenv("PANEL_SENSOR3_TEMP_ENV_REALTIME"))
PANEL_SENSOR3_TEMP_ENV_1HOUR = int(os.getenv("PANEL_SENSOR3_TEMP_ENV_1HOUR"))
PANEL_SENSOR3_TEMP_ENV_30DAYS = int(os.getenv("PANEL_SENSOR3_TEMP_ENV_30DAYS"))
PANEL_SENSOR1_AIR_ENV_REALTIME = int(os.getenv("PANEL_SENSOR1_AIR_ENV_REALTIME"))
PANEL_SENSOR1_AIR_ENV_1HOUR = int(os.getenv("PANEL_SENSOR1_AIR_ENV_1HOUR"))
PANEL_SENSOR1_AIR_ENV_30DAYS = int(os.getenv("PANEL_SENSOR1_AIR_ENV_30DAYS"))
PANEL_SENSOR1_HUMIDITY_REALTIME = int(os.getenv("PANEL_SENSOR1_HUMIDITY_REALTIME"))
PANEL_SENSOR1_HUMIDITY_1HOUR = int(os.getenv("PANEL_SENSOR1_HUMIDITY_1HOUR"))
PANEL_SENSOR1_HUMIDITY_30DAYS = int(os.getenv("PANEL_SENSOR1_HUMIDITY_30DAYS"))

#   Function:       updateThresholds
#   Description:    Gets new threshold data on a single sensor from the front end.
#                   Sends the data to the right post method
#
#   This is the route for the front-end to use to update thresholds
@app.route('/grafana_threshold_update', methods=['POST'])
def updateThresholds():
    #   Get threshold data from the frontend
    threshold_data = request.json
    sensor_id = threshold_data.get("sensor_id")
    range_min = threshold_data.get("min_value")
    range_max = threshold_data.get("max_value")

    #   Determine which thresholds to change in POST and execute
    post_response = []
    if sensor_id == SENSOR1_TEMP:
        post_response.append(postPanelThresholdChange(DASHBOARD_ENV_REALTIME, 
                                                      PANEL_SENSOR1_TEMP_ENV_REALTIME, 
                                                      range_min, 
                                                      range_max))
        post_response.append(postPanelThresholdChange(DASHBOARD_ENV_1HOUR, 
                                                      PANEL_SENSOR1_TEMP_ENV_1HOUR, 
                                                      range_min, 
                                                      range_max))
        post_response.append(postPanelThresholdChange(DASHBOARD_ENV_30DAYS, 
                                                      PANEL_SENSOR1_TEMP_ENV_30DAYS, 
                                                      range_min, 
                                                      range_max))
    elif sensor_id == SENSOR2_TEMP:
        post_response.append(postPanelThresholdChange(DASHBOARD_ENV_REALTIME, 
                                                      PANEL_SENSOR2_TEMP_ENV_REALTIME, 
                                                      range_min, 
                                                      range_max))
        post_response.append(postPanelThresholdChange(DASHBOARD_ENV_1HOUR, 
                                                      PANEL_SENSOR2_TEMP_ENV_1HOUR, 
                                                      range_min, 
                                                      range_max))
        post_response.append(postPanelThresholdChange(DASHBOARD_ENV_30DAYS, 
                                                      PANEL_SENSOR2_TEMP_ENV_30DAYS, 
                                                      range_min, 
                                                      range_max))
    elif sensor_id == SENSOR3_TEMP:
        post_response.append(postPanelThresholdChange(DASHBOARD_ENV_REALTIME, 
                                                      PANEL_SENSOR3_TEMP_ENV_REALTIME, 
                                                      range_min, 
                                                      range_max))
        post_response.append(postPanelThresholdChange(DASHBOARD_ENV_1HOUR, 
                                                      PANEL_SENSOR3_TEMP_ENV_1HOUR, 
                                                      range_min, 
                                                      range_max))
        post_response.append(postPanelThresholdChange(DASHBOARD_ENV_30DAYS, 
                                                      PANEL_SENSOR3_TEMP_ENV_30DAYS, 
                                                      range_min, 
                                                      range_max))
    elif sensor_id == SENSOR1_AIR:
        post_response.append(postPanelThresholdChange(DASHBOARD_ENV_REALTIME, 
                                                      PANEL_SENSOR1_AIR_ENV_REALTIME, 
                                                      range_min, 
                                                      range_max))
        post_response.append(postPanelThresholdChange(DASHBOARD_ENV_1HOUR, 
                                                      PANEL_SENSOR1_AIR_ENV_1HOUR, 
                                                      range_min, 
                                                      range_max))
        post_response.append(postPanelThresholdChange(DASHBOARD_ENV_30DAYS, 
                                                      PANEL_SENSOR1_AIR_ENV_30DAYS, 
                                                      range_min, 
                                                      range_max))
    elif sensor_id == SENSOR1_HUMIDITY:
        post_response.append(postPanelThresholdChange(DASHBOARD_ENV_REALTIME, 
                                                      PANEL_SENSOR1_HUMIDITY_REALTIME, 
                                                      range_min, 
                                                      range_max))
        post_response.append(postPanelThresholdChange(DASHBOARD_ENV_1HOUR, 
                                                      PANEL_SENSOR1_HUMIDITY_1HOUR, 
                                                      range_min, 
                                                      range_max))
        post_response.append(postPanelThresholdChange(DASHBOARD_ENV_30DAYS, 
                                                      PANEL_SENSOR1_HUMIDITY_30DAYS, 
                                                      range_min, 
                                                      range_max))
    else:
        post_response = []
        print("sensor_id incorrect.")
    
    #   No response from post functions, exit
    if post_response == []:
        print("sensor_id incorrect.")
        return jsonify({"error": "Invalid sensor_id"}), 400 
    
    #   Package all responses into one JSON to send to frontend
    data = [
        {"status_code": response.status_code, "response_text": response.text}
        for response in post_response
    ]

    return jsonify({"data": data}), post_response[0].status_code

#   Function:       postPanelThresholdChange
#   Description:    Sends a POST to the grafana API to update the panel on the 
#                   given dashboard the new min and max threshold values.
def postPanelThresholdChange(dashboardURL, panelID, min, max):
    #   Get Dashboard data 
    get_response = requests.get(dashboardURL, headers=headers, verify=False)

    #   If dashboard request is good, filter to panel data and update threshold data
    if get_response.status_code == 200:
        try: 
            dashboardData = get_response.json()

            panelData = dashboardData.get('dashboard', {}).get('panels', [])
            #   Drill down to thresholds on a specific panel, it's thresholds JSON 
            for panel in panelData:
                if panel.get("id") == panelID:
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
            return requests.post(DASHBOARD_POST_URL, headers=headers, json=payload, verify=False)

        except ValueError:
            return get_response.text
    else:
        return jsonify({"error": "failed to post panel change."}), 400 

#   Main app
if __name__ == '__main__':
    app.run(debug=True, port=PORT)