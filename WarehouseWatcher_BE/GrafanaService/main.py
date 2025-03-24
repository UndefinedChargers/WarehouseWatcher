# FILE : main.py
# PROGRAMMER : William Anderson
# FIRST VERSION : 2025-03-23
# DESCRIPTION : Communicates the current threshold data to the grafana api to update panel thresholds.

import os
from flask import Flask
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

header = {
    "Authorization": f'Bearer {os.getenv("GRAFANA_TOKEN")}',
    "Content-Type": "application/json"
}

DASHBOARD_ENV_30DAYS = os.getenv("DASHBOARD_ENV_30DAYS")

@app.route('/grafana_threshold_update', methods=['GET'])

def getPanels():
    response = requests.get(DASHBOARD_ENV_30DAYS, headers=header, verify=False)
    
    if response.status_code == 200:

        try: 
            dashboardData = response.json()
            panels = dashboardData.get('dashboard', {}).get('panels', [])
            print("Show panels.")
            return panels
        except ValueError:
            return response.text

    else:
        return "Failure", 400

if __name__ == '__main__':
    app.run(debug=True)