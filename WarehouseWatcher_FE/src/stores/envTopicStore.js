// FILE: envTopicStore.js
// PROJECT: Warehouse Watcher
// PROGRAMMER: Undefined Chargers - Yujung Park
// FIRST VERSION: 
// DESCRIPTION:

import { defineStore } from 'pinia'

export const useEnvTopicStore = defineStore('envDataStore', {
  state: () => ({
      envTopicData: new Map(),
  }),
  
  getters: {
    individualTopicData: (state) => {
      return (topic) => state.envTopicData.get(topic);
    },
  },

  actions: {
    setTopicData (topic, payload) {
      this.envTopicData.set(topic, payload);
    },
  },
})