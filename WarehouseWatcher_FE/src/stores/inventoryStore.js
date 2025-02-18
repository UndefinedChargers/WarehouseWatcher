// FILE: inventoryStore.js
// PROJECT: Warehouse Watcher
// PROGRAMMER: Undefined Chargers - Yujung Park
// FIRST VERSION: 2025-02-14

import { defineStore } from 'pinia'

export const useInventoryStore = defineStore('inventoryDataStore', {
  state: () => ({
      inventoryData: new Map(),
  }),
  
  getters: {
    getLocationInventory: (state) => {
      return (topic) => state.inventoryData.get(topic);
    },
  },

  actions: {
    setInvTopicData (topic, payload) {
      this.inventoryData.set(topic, payload);
    },
  },
})