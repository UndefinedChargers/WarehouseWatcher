// FILE: thresholdchecker.js
// PROJECT: Warehouse Watcher
// PROGRAMMER: Undefined Chargers - Yujung Park
// FIRST VERSION: 2025-03-11
// DESCRIPTION: 
// REFERENCES: https://www.npmjs.com/package/uuid

import { useAppConfigsStore } from "@/stores/appConfigsStore";
import { sensor_object } from "@/configs/ww-config";
import { v1 as uuidv1 } from 'uuid';

export const notificationHandler = (tpc, payload) => {
  const objectConfig = useAppConfigsStore()
  
  const sensor = sensor_object.find(obj => obj.topic === tpc)
  const target_object = objectConfig.getConfigObject(sensor.meshname)
  
  let key = undefined
  var notification = { alert_object: "", alert_type: "", timestamp: "" }
  
  if (target_object !== undefined)
  {
    let notificationsize = objectConfig.notifications.size
    // console.log(target_object)
    // console.log(payload[sensor.targetval][sensor.targetvalmem])
    let val = payload[sensor.targetval][sensor.targetvalmem]
    let date = new Date();
    key = uuidv1()
    notification.alert_object = target_object.meshname
    notification.timestamp = date.toISOString();
    if (val <= target_object.min_threshold) {
      notification.alert_type = "Minimum Threshold" 
      objectConfig.setNotifications(key, notification)
    } 
    if (val >= target_object.max_threshold) {
      notification.alert_type = "Maximum Threshold"
      objectConfig.setNotifications(key, notification)
    } 
    if (notificationsize >=30 ) {
      // console.log(`notificationsize ${notificationsize}`);
      objectConfig.resetNotifications();
    }
    // console.log(`notifications ${objectConfig.notifications.size}`);
    // console.log(target_object.meshname)
  }
}

