# FILE : main.py
# PROGRAMMER : William Anderson
# FIRST VERSION : 2025-03-23
# DESCRIPTION : Communicates the current threshold data to the grafana api to update panel thresholds.

# Currently using test threshold data, but it successfully changes the grafana dashboards.

import os
from flask import Flask
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Authorization token in header
headers = {
    "Authorization": f'Bearer {os.getenv("GRAFANA_TOKEN")}',
    "Content-Type": "application/json"
}

#   Test Data 
#   ***Need to get from front end instead.***
new_thresholds = {
    "thresholds": {
        "mode": "absolute",
        "steps": [
            {
                "color": "red", 
                "value": None
            },
            {
                "color": "green", 
                "value": -19
            },
            {
                "color": "red", 
                "value": -17
            }
        ],
    }
}

#   Grabbing grafana dashboard urls
DASHBOARD_ENV_REALTIME = os.getenv("DASHBOARD_ENV_REALTIME")
DASHBOARD_PUT_URL = os.getenv("DASHBOARD_PUT_URL")

#   This is the route for the front-end to use
@app.route('/grafana_threshold_update', methods=['GET'])

#   Function:       updateThresholds
#   Description:    
def updateThresholds():
    #   Get Dashboard data 
    #   ***Needs to update all dashboards at once, or split into specific calls***
    get_response = requests.get(DASHBOARD_ENV_REALTIME, headers=headers, verify=False)
    
    if get_response.status_code == 200:

        try: 
            #   Send GET
            dashboardData = get_response.json()
            panelData = dashboardData.get('dashboard', {}).get('panels', [])

            #   Drill down to thresholds on a specific panel
            #   ***Need to connect specific panels to specific threshold changes***
            for panel in panelData:
                if panel.get("id") == 2:
                    if 'fieldConfig' in panel and 'defaults' in panel['fieldConfig']:
                        panel['fieldConfig']['defaults']['thresholds'] = new_thresholds['thresholds']

            #   Need to update the version and set to overwrite for the api to work
            dashboardData["dashboard"]["version"] += 1
            data = {
                "dashboard": dashboardData["dashboard"],
                "overwrite": True
            }

            #   Send POST
            post_response = requests.post(DASHBOARD_PUT_URL, headers=headers, json=data, verify=False)

            #   Just debugging info
            if post_response.status_code == 200:
                print("Success")
            else:
                print(f"Status Code: {post_response.status_code}, Response Text: {post_response.text}")

            return dashboardData
        except ValueError:
            return get_response.text

    else:
        return "Failure", 400

if __name__ == '__main__':
    app.run(debug=True)