// FILE: appStateStore.js
// PROJECT: Warehouse Watcher
// PROGRAMMER: Undefined Chargers - Yujung Park
// FIRST VERSION: 2025-01-10
// DESCRIPTION:


import { defineStore } from 'pinia'

export const useAppStateStore = defineStore('appDataStore', {
  state: () => ({
      targetObject: undefined,
  }),
  
  getters: {
    
  },

  actions: {
    setTargetObject (meshname) {
      this.targetObject = meshname;
    },
  },
})