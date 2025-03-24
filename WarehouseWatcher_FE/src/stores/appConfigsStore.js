// FILE: appConfigsStore.js
// PROJECT: Warehouse Watcher
// PROGRAMMER: Undefined Chargers - Yujung Park, Aryan Passi
// FIRST VERSION: 2025-03-23
// https://stackoverflow.com/questions/6439915/how-to-set-a-javascript-object-values-dynamically

import { defineStore } from 'pinia';

export const useAppConfigsStore = defineStore('appConfigsStore', {
  state: () => ({
    sensorObjConfigs: new Map(),
    notifications: new Map(),
  }),
  
  getters: {
    // Get the entire config object for a specific sensor
    individualObjectConfig: (state) => (objid) => {
      return state.sensorObjConfigs.get(objid);
    },
    
    // Get specific config values (min_threshold, max_threshold) for a sensor
    getConfigObject: (state) => (topic) => {
      return state.sensorObjConfigs.get(topic);
    },
  },

  actions: {
    // Set object configurations for a given sensor
    setObjectConfigs (objid, configs) {
      this.sensorObjConfigs.set(objid, configs);
    },
    
    // Update a specific member of a sensor config (e.g., min_threshold or max_threshold)
    setObjectMemberValue (objid, membername, value) {
      let object = this.sensorObjConfigs.get(objid);
      if (object) {
        object[membername] = value;
      }
    },
    
    // Set notification settings for a specific UUID
    setNotifications (uuid, notification) {
      this.notifications.set(uuid, notification);
    },
    
    // Clear all notifications
    resetNotifications () {
      this.notifications.clear();
    },
  },

  // Sync with local storage for persisting config data
  persist: true, // This assumes a Pinia plugin is used for persistence
});
