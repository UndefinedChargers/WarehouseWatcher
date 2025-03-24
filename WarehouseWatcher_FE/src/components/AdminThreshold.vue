<!-- 
 FILE: AdminThreshold.vue
 PROJECT: Warehouse Watcher
 PROGRAMMER: Undefined Chargers - Aryan Passi
 FIRST VERSION: 2025-03-09
 -->
 
 <script setup>
 import { ref, onMounted } from "vue";
 import { useAppConfigsStore } from "@/stores/appConfigsStore";
 
 let obj = "sensor1_temp"; // Remote change
 let member = "min_threshold"; // Remote change
 let value = 18; // Remote change
  
 // Warehouse Watcher sensors with default min/max thresholds
 const thresholds = ref([
   { id: "sensor1_temp", name: "Room Thermostat", min_member: "min_threshold", max_member: "max_threshold", current_min: 0, current_max: 0, new_min: 0, new_max: 0, min: 10, max: 35 },
   { id: "sensor2_temp", name: "Refrigerator Thermostat", min_member: "min_threshold", max_member: "max_threshold", current_min: 0, current_max: 0, new_min: 0, new_max: 0, min: 0, max: 10 },
   { id: "sensor3_temp", name: "Freezer Thermostat", min_member: "min_threshold", max_member: "max_threshold", current_min: 0, current_max: 0, new_min: 0, new_max: 0, min: 0, max: -35 },
   { id: "sensor1_humidity", name: "Humidity Sensor", min_member: "min_threshold", max_member: "max_threshold", current_min: 0, current_max: 0, new_min: 0, new_max: 0, min: 10, max: 50 },
   { id: "sensor1_air", name: "Air Quality Sensor", min_member: "min_threshold", max_member: "max_threshold", current_min: 0, current_max: 0, new_min: 0, new_max: 0, min: 10, max: 50 },
 ]);
<<<<<<< HEAD
 
 // Load saved thresholds from store 
=======

 const objectConfig = useAppConfigsStore();
 objectConfig.$subscribe((mutation, state) => {
  // console.log(objectConfig)
  thresholds.value.map(sensor => {
    // iterate thresholds and complete current min, max value
    const sensordata_object = objectConfig.getConfigObject(sensor.id);
    sensor.current_min = sensordata_object.min_threshold;
    sensor.current_max = sensordata_object.max_threshold;
  })
})

 // Load saved thresholds from store (or API)
>>>>>>> dab2c88f177e547c7964275c8afa2d864b6c93f3
 const loadSavedThresholds = () => {
  // thresholds.value.forEach(sensor => {
  //    const savedMin = objectConfig.getObjectMemberValue(sensor.id, sensor.min_member);
  //    const savedMax = objectConfig.getObjectMemberValue(sensor.id, sensor.max_member);
 
  //    if (savedMin !== undefined) sensor.min_value = savedMin;
  //    if (savedMax !== undefined) sensor.max_value = savedMax;
  //  });

  thresholds.value.map(sensor => {
    const sensordata_object = objectConfig.getConfigObject(sensor.id);
    sensor.current_min = sensordata_object.min_threshold;
    sensor.current_max = sensordata_object.max_threshold;
  })
 };
 
 // Update single threshold
 const updateConfigs = (sensor, type) => {
   const value = type === "min" ? sensor.new_min : sensor.new_max;
   const member = type === "min" ? sensor.min_member : sensor.max_member;
 
   // Ensure min is always less than max
   if (sensor.min_value >= sensor.max_value) {
     alert("Min threshold cannot be greater than or equal to Max threshold!");
     return;
   }

   objectConfig.setObjectMemberValue(sensor.id, member, value);
 };
 
 // Save all thresholds at once
 const saveAllThresholds = () => {
   thresholds.value.forEach(sensor => {
     objectConfig.setObjectMemberValue(sensor.id, sensor.min_member, sensor.min_value);
     objectConfig.setObjectMemberValue(sensor.id, sensor.max_member, sensor.max_value);
   });
   alert("All thresholds have been saved successfully!");
 };

 // Load saved values when component mounts
 onMounted(() => {
   loadSavedThresholds(); 
 });
 </script>
 
 <template>
  <h1 class="text-center">Threshold Settings</h1>
  <v-container class="bg-light-gray pa-3 rounded elevation-2">
    <div class="pa-3 ma-5 rounded">
      <v-row>
        <v-col>Sensor</v-col>
        <v-col>Type</v-col>
        <v-col>Current Value</v-col>
        <v-col>New Value</v-col>
      </v-row>
    </div>
    <div v-for="sensor in thresholds" :key="sensor.id" class="pa-3 ma-5 bg-white rounded  ">
      <v-row no-gutters>
        <v-col class="ma-2">{{ sensor.name }}</v-col>
        <v-col class="ma-2">{{ sensor.min_member }}</v-col>
        <v-col class="ma-2">{{ sensor.current_min}}</v-col>
        <v-col>
          <input 
          type="number" 
          v-model="sensor.new_min" 
          :min="sensor.min" 
          :max="sensor.max"
          class="ma-2"
          />
          <button class="ma-2" @click="updateConfigs(sensor, 'min')">Save</button>
        </v-col>
      </v-row>
      <v-row no-gutters>
        <v-col class="ma-2">{{ sensor.name }}</v-col>
        <v-col class="ma-2">{{ sensor.max_member }}</v-col>
        <v-col class="ma-2">{{ sensor.current_max }}</v-col>
        <v-col>
          <input 
          type="number" 
          v-model="sensor.new_max" 
          :min="sensor.min" 
          :max="sensor.max"
          class="ma-2"
          />
          <button class="ma-2" @click="updateConfigs(sensor, 'max')">Save</button>
        </v-col>
      </v-row>
    </div>

  </v-container>

   <!-- <div class="threshold-container">
     <h2>Sensor Threshold Configuration</h2>
     <div class="threshold-list">
       <div v-for="sensor in thresholds" :key="sensor.id" class="threshold-item">
         <div class="sensor-info">
           <label>{{ sensor.name }}</label>
           <div class="threshold-inputs">
             <div>
               <label>Min</label>
               <input 
                 type="number" 
                 v-model="sensor.min_value" 
                 :min="sensor.min" 
                 :max="sensor.max"
               />
               <button @click="updateConfigs(sensor, 'min')">Set Min</button>
             </div>
             <div>
               <label>Max</label>
               <input 
                 type="number" 
                 v-model="sensor.max_value" 
                 :min="sensor.min" 
                 :max="sensor.max"
               />
               <button @click="updateConfigs(sensor, 'max')">Set Max</button>
             </div>
           </div>
         </div>
       </div>
     </div>
     <button class="save-btn" @click="saveAllThresholds">Save All Thresholds</button>
   </div> -->
  
 </template>
 
 <style scoped>
 .threshold-container {
   display: flex;
   flex-direction: column;
   align-items: center;
   max-width: 700px;
   margin: auto;
   padding: 20px;
   background: #f8f9fa;
   border-radius: 8px;
   box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
 }
 
 h2 {
   text-align: center;
   margin-bottom: 15px;
 }
 
 .threshold-list {
   display: flex;
   flex-direction: column;
   gap: 15px;
   width: 100%;
 }
 
 .threshold-item {
   display: flex;
   flex-direction: column;
   align-items: center;
   background: white;
   border-radius: 8px;
   padding: 15px;
   box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
 }
 
 .sensor-info {
   width: 100%;
 }
 
 .threshold-inputs {
   display: flex;
   justify-content: space-between;
   width: 100%;
   gap: 10px;
 }
 
 .threshold-inputs div {
   display: flex;
   flex-direction: column;
   align-items: center;
 }
 
 label {
   font-size: 14px;
   font-weight: bold;
   margin-bottom: 5px;
 }
 
 input {
   width: 80px;
   padding: 5px;
   text-align: center;
   border: 1px solid #ddd;
   border-radius: 4px;
 }
 
 button {
   background: #007bff;
   color: white;
   border: none;
   padding: 5px 10px;
   cursor: pointer;
   border-radius: 4px;
   margin-top: 5px;
 }
 
 button:hover {
   background: #0056b3;
 }
 
 .save-btn {
   margin-top: 20px;
   background: #28a745;
   padding: 10px 15px;
 }
 
 .save-btn:hover {
   background: #218838;
 }
 </style>