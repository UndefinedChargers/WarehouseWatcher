// FILE: sensorDataStore.js
// PROJECT: Warehouse Watcher
// PROGRAMMER: Undefined Chargers - Yujung Park
// FIRST VERSION: 2025-03-19
// DESCRIPTION:

import { defineStore } from 'pinia'

export const useSensorDataStore = defineStore('sensorDataStore', {
  state: () => ({
      sensorData: new Map(),
      sensorName: '',
  }),
  
  getters: {
    getSensorData: (state) => {
      return (sensor) => state.sensorData.get(sensor)
    },
    getSensorName: (state) => {
      return this.sensorName;
    }
  },

  actions: {
    setSensorData (sensor, timeseriesdata) {
      this.sensorData.set(sensor, timeseriesdata)
    },
    setSensorName (sensor) {
      this.sensorName = sensor
    },
    cleanSensorData () {
      this.sensorData.clear()
    }
  },
})