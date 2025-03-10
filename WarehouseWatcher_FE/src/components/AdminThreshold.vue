<script setup>
import { ref } from "vue";
import { useAppConfigsStore } from "@/stores/appConfigsStore";

const objectConfig = useAppConfigsStore();

// Warehouse Watcher sensors with min/max thresholds
const thresholds = ref([
  { id: "temperature", name: "Temperature", min_member: "min_threshold", max_member: "max_threshold", min_value: 10, max_value: 50, min: 15, max: 40 },
  { id: "humidity", name: "Humidity", min_member: "min_threshold", max_member: "max_threshold", min_value: 20, max_value: 80, min: 30, max: 70 },
  { id: "air_quality", name: "Air Quality", min_member: "min_threshold", max_member: "max_threshold", min_value: 50, max_value: 300, min: 60, max: 250 },
]);

// Update function for both min and max thresholds
const updateConfigs = (sensor, type) => {
  const value = type === "min" ? sensor.min_value : sensor.max_value;
  const member = type === "min" ? sensor.min_member : sensor.max_member;

  // Ensure values stay within limits
  if (sensor.min_value >= sensor.max_value) {
    alert("Min value cannot be greater than or equal to Max value!");
    return;
  }

  objectConfig.setObjectMemberValue(sensor.id, member, value);
};
</script>

<template>
  <div class="threshold-container">
    <h2>Threshold Sensor Configurations</h2>
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
</style>
