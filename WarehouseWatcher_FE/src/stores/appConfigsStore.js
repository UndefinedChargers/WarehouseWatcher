// FILE: appConfigsStore.js
// PROJECT: Warehouse Watcher
// PROGRAMMER: Undefined Chargers - Yujung Park
// FIRST VERSION: 2025-03-05
// https://stackoverflow.com/questions/6439915/how-to-set-a-javascript-object-values-dynamically

import { defineStore, } from 'pinia'

export const useAppConfigsStore = defineStore('appConfigsStore', {
  state: () => ({
      sensorObjConfigs: new Map(),
      notifications: new Map(),
  }),
  
  getters: {
    individualObjectConfig: (obj) => {
      return (objid) => obj.sensorObjConfigs.get(objid);
    },
    getConfigObject: (obj) => {
      return (topic) => obj.sensorObjConfigs.get(topic);
    },
  },

  actions: {
    setObjectConfigs (objid, configs) {
      this.sensorObjConfigs.set(objid, configs);
    },
    setObjectMemberValue (objid, membername, value) {
      let object = this.sensorObjConfigs.get(objid);
      object[membername] = value;
      // console.log(object[membername]);
    }, 
    setNotifications (uuid, notification) {
      this.notifications.set(uuid, notification);
    },
    resetNotifications () {
      this.notifications.clear()
    }
  },
})