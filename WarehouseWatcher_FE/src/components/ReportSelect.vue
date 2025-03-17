<template>
  <div class="report-container">
    <h1>Report</h1>
    <div>
      <v-container class="bg-surface-variant mt-6 rounded">
        <v-row>
          <v-col cols="12">
            <v-row align="start" style="height: 24px;" no-gutters>
              <v-col class="mt-0 pt-0">
                <v-label class="pa-0 ml-2">Sensor</v-label>
              </v-col>
              <v-col>
                <v-label class="pa-0 ml-2">Start</v-label>
              </v-col>
              <v-col>
               <v-label class="pa-0 ml-2">End</v-label>
              </v-col>
            </v-row>
            <v-row align="start" style="height: 80px;" no-gutters>
              <v-col>
                <v-select 
                class="pa-2 ma-2 " width="250px" label="Select" :items="['Thermo-Room', 'Thermo-Fridge', 'Thermo-Freezer','Air Quality', 'Humidity']" variant="solo-filled"
                v-model="sensor"></v-select>
              </v-col>
              <v-col>
                <input class="bg-white rounded pa-2 ma-2" type="datetime-local" id="meeting-time" name="meeting-time" value="" min="2025-03-01T00:00" max="2025-06-30T00:00" 
                v-model="start" />
              </v-col>
              <v-col>
                <input class="bg-white rounded pa-2 ma-2" type="datetime-local" id="meeting-time" name="meeting-time" value="" min="2025-03-01T00:00" max="2025-06-30T00:00" 
                v-model="end" />
              </v-col>
            </v-row>
          </v-col>
          <v-col align="center">
            <v-btn tonal> Search </v-btn>
          </v-col>
        </v-row>
      </v-container>
    </div>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

</script>

<style scoped>
/* .report-container {
  width: 100%;
} */

input,
textarea {
  align-items: center;
  /* field-sizing: content; */
  min-width: 50px;
  max-width: 324px;
  height: 58px;
}
</style>