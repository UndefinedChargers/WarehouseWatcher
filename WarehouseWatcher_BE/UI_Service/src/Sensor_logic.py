# FILE :Sensor_logic.py
# PROJECT :Warehouse Watcher
# PROGRAMMER : Amel Korandippillil Sunil
# DESCRIPTION :This file basically contain the functions of the simulatorUI which contains the UI functionality

import json


# function name: on_off_battery_switch
# Description: This function basically sends the control message of the battery updates to the subscriber of the UI controls
# Parameter: void:self
# return: sensor_name,is_on,mqtt_handler,sensor_datamanager,msg_display 
def on_off_battery_switch(sensor_name,is_on,mqtt_handler,sensor_datamanager,msg_display):

    control_message={"sensor_name":sensor_name,"action":"set_battery","battery_enabled":is_on}
    payload=json.dumps(control_message)
    topic=f"Waterloo/Warehouse/Control/{sensor_name}"

    if is_on:
        new_battery=100
    else:
        new_battery=0
    
    if msg_display:
        log_line = f"[Battery] {sensor_name} -> {new_battery}\n"
        msg_display.insert("end", log_line)
        msg_display.see("end")

# function name:adjust_data_one
# Description: This function send the control message to increment the value by 1
# Parameter: void:self
# return: None 
def adjust_data_one(sensor_name, field_name, direction, mqtt_handler, msg_display):
   
    if direction not in ["up", "down"]:
        return

    action = "increase_data" if direction == "up" else "decrease_data"
    control_msg = {"sensor_name": sensor_name,"action": action,"field": field_name}
    payload = json.dumps(control_msg)
    topic = f"Waterloo/Warehouse/Control/{sensor_name}"
    if msg_display:
        log_line = f"[Adjust Data] {action.upper()} '{field_name}' -> {topic}: {payload}\n"
        msg_display.insert("end", log_line)
        msg_display.see("end")

    





