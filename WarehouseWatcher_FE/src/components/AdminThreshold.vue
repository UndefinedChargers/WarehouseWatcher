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
 
 const objectConfig = useAppConfigsStore();
 
 // Warehouse Watcher sensors with default min/max thresholds
 const thresholds = ref([
   { id: "temperature", name: "Temperature", min_member: "min_threshold", max_member: "max_threshold", min_value: 15, max_value: 40, min: 10, max: 50 },
   { id: "humidity", name: "Humidity", min_member: "min_threshold", max_member: "max_threshold", min_value: 30, max_value: 70, min: 20, max: 80 },
   { id: "air_quality", name: "Air Quality", min_member: "min_threshold", max_member: "max_threshold", min_value: 60, max_value: 250, min: 50, max: 300 },
 ]);
 
 // Load saved thresholds from store (or API)
 const loadSavedThresholds = () => {
   thresholds.value.forEach(sensor => {
     const savedMin = objectConfig.getObjectMemberValue(sensor.id, sensor.min_member);
     const savedMax = objectConfig.getObjectMemberValue(sensor.id, sensor.max_member);
 
     if (savedMin !== undefined) sensor.min_value = savedMin;
     if (savedMax !== undefined) sensor.max_value = savedMax;
   });
 };
 
 // Update single threshold
 const updateConfigs = (sensor, type) => {
   const value = type === "min" ? sensor.min_value : sensor.max_value;
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
   <div class="threshold-container">
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
   </div>
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