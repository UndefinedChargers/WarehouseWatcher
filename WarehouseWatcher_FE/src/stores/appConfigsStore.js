// FILE: appConfigsStore.js
// PROJECT: Warehouse Watcher
// PROGRAMMER: Undefined Chargers - Yujung Park, Aryan Passi
// FIRST VERSION: 2025-03-23
// https://stackoverflow.com/questions/6439915/how-to-set-a-javascript-object-values-dynamically

import { defineStore } from 'pinia'

export const useAppConfigsStore = defineStore('appConfigsStore', {
  state: () => ({
    sensorObjConfigs: new Map(),
    notifications: new Map(),
  }),

  getters: {
    // Retrieve the entire configuration object for a given sensor by its ID
    getConfigObject: (obj) => {
      return (topic) => obj.sensorObjConfigs.get(topic);
    },
    // Get the current threshold value of a specific sensor member
    getThreshold: (sensorId, type) => {
      const sensorConfig = obj.sensorObjConfigs.get(sensorId);
      return sensorConfig ? sensorConfig[type] : undefined;
    },
  },

  actions: {
    // Set configuration for a sensor
    setObjectConfigs(objid, configs) {
      this.sensorObjConfigs.set(objid, configs);
    },

    // Set or update a specific member of a sensor configuration
    setObjectMemberValue(objid, membername, value) {
      let object = this.sensorObjConfigs.get(objid);
      if (object) {
        object[membername] = value;
      } else {
        console.error(`Sensor with id ${objid} not found.`);
      }
    },

    // Save threshold values for a sensor
    setThreshold(objid, minThreshold, maxThreshold) {
      let object = this.sensorObjConfigs.get(objid);
      if (object) {
        object.min_threshold = minThreshold;
        object.max_threshold = maxThreshold;
      } else {
        console.error(`Sensor with id ${objid} not found.`);
      }
    },

    // Set notifications, e.g., alerts for thresholds
    setNotifications(uuid, notification) {
      this.notifications.set(uuid, notification);
    },

    // Reset all notifications
    resetNotifications() {
      this.notifications.clear();
    },
  },
});
