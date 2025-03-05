// FILE: appConfigsStore.js
// PROJECT: Warehouse Watcher
// PROGRAMMER: Undefined Chargers - Yujung Park
// FIRST VERSION: 2025-03-05
// https://stackoverflow.com/questions/6439915/how-to-set-a-javascript-object-values-dynamically

import { defineStore } from 'pinia'

export const useAppConfigsStore = defineStore('appConfigsStore', {
  state: () => ({
      sensorObjConfigs: new Map(),
  }),
  
  getters: {
    individualObjectConfig: (obj) => {
      return (objid) => obj.sensorObjConfigs.get(objid);
    },
  },

  actions: {
    setObjectConfigs (objid, configs) {
      this.sensorObjConfigs.set(objid, configs);
    },
    setObjectMemberValue (objid, membername, value) {
      let object = this.sensorObjConfigs.get(objid);
      object[membername] = value;
      console.log(object[membername]);
    }
  },
})