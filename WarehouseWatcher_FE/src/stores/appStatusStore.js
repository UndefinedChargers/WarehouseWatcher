// FILE: appStateStore.js
// PROJECT: Warehouse Watcher
// PROGRAMMER: Undefined Chargers - Yujung Park
// FIRST VERSION: 2025-01-10
// DESCRIPTION:


import { defineStore } from 'pinia'

export const useAppStatusStore = defineStore('appStatusDataStore', {
  state: () => ({
      targetObject: String,
      inventory_reload: Boolean,
  }),
  
  getters: {
    getTargetObject: (state) => {
      return targetObject;
    },
  },

  actions: {
    setTargetObject (meshname) {
      this.targetObject = meshname;
    },
    setInventoryReload (status) {
      this.inventory_reload = status;
    },
  },
})