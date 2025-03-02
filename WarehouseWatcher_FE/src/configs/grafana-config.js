// FILE:            grafana-config.js
// PROJECT:         Warehouse Watcher
// PROGRAMMER:      Undefined Chargers - William Anderson
// FIRST VERSION:   2025-02-02

export const grafana_dashboards = {
    humidity: [
        {   name: "Humidity Last Hour", 
            link: "http://localhost:3000/d/aeefvn1mryhhce/humidity-last-hour?orgId=2&from=2025-03-02T15:28:41.043Z&to=2025-03-02T16:28:41.043Z&timezone=browser&viewPanel=panel-1" 
        },
        {   name: "Humidity Last 2 Days", 
            link: "http://localhost:3000/d/ceefvqd4nl7ggb/humidity-last-2-days?orgId=2&from=now-2d&to=now&timezone=browser&viewPanel=panel-1" 
        }
    ],
    airQuality: [
        {   name: "CO2 Last Hour", 
            link: "http://localhost:3000/d/feefleimtlqtca/c02-last-hour?orgId=2&from=2025-03-02T15:28:03.974Z&to=2025-03-02T16:28:03.974Z&timezone=browser&viewPanel=panel-1" 
        },
        {   name: "CO2 Last 2 Days", 
            link: "http://localhost:3000/d/eeeftzn77slq8c/co2-last-2-days?orgId=2&from=now-2d&to=now&timezone=browser&viewPanel=panel-1" 
        }
    ]
  };