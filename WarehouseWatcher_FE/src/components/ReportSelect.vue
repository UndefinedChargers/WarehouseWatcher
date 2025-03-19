<!-- 
 FILE: ReportSelect.vue
 PROJECT: Warehouse Watcher
 PROGRAMMER: Undefined Chargers - Yujung Park
 FIRST VERSION: 2025-03-17
 DESCRIPTION: 
 References: Starting code - https://vuetifyjs.com/en/components/app-bars/#images
 Prevent reload - https://stackoverflow.com/questions/66271980/cant-prevent-default-on-form-submission-vue-3
 -->

<template>
  <div class="report-container">
    <h1 class="main-title">Report</h1>
    <form @submit.prevent="getData">
      <v-container class="bg-surface-variant rounded pa-5">
        <v-row>
            <div>
              <select class="pa-2 ma-2" v-model="selectedsensor">
                <option v-for="option in options" :value="option.value">
                  {{ option.text }}
                </option>
              </select>
            </div>
            <div>
              <label for="start-date">Start:</label>
              <input class="bg-white rounded pa-2 ma-2" type="datetime-local" id="meeting-time" name="meeting-time" min="2025-03-01T00:00" max="2025-06-30T00:00" 
              v-model="startdt"
              />
            </div>
            <div>
              <label for="end-date">End:</label>
              <input class="bg-white rounded pa-2 ma-2" type="datetime-local" id="meeting-time" name="meeting-time" value="" min="2025-03-01T00:00" max="2025-06-30T00:00" 
              v-model="enddt"
              />
            </div>
            <v-btn class="bg-blue rounded pa-2 ma-2" type="submit"> Search </v-btn>
        </v-row>
      </v-container>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const selectedsensor = ref('')
const startdt = ref('')
const enddt = ref('')
const options = ref([
  {text: 'Select sensor', value: ''},
  {text: 'Room Thermostat', value: 'Room-thermo'},
  {text: 'Fridge Thermostat', value: 'Fridge-thermo'},
  {text: 'Freezer Thermostat', value: 'Freezer-thermo'},
  {text: 'Air quality', value: 'airquality'},
  {text: 'Humidity', value: 'humidity'},
])

async function getData() {
  console.log(selectedsensor.value, startdt.value, enddt.value)
  const response = await axios.get('http://localhost')
}

</script>

<style scoped>
.report-container {
  width: 100%;
  height: 100%;
  font-family: "Poppins", sans-serif;
  color: white;
  text-align: center;
  padding: 1rem 4rem 1rem 4rem;
}

.main-title {
  font-size: 2rem;
  margin-bottom: 1.5rem;
}

select {
  padding: 2px 5px;
  background-color: white;
  border-radius: 5px;
}

input {
  padding-top: 5px;
}

input,
textarea {
  align-items: center;
  min-width: 32px;
  max-width: 324px;
}
</style>