<script setup>
import { RouterLink, RouterView } from 'vue-router';
import AppBar from './components/AppBar.vue';
import { onActivated, onMounted } from 'vue';
import { subscribeMQTT } from'./helper/wwmqtt';
import { sensor_object } from './configs/ww-config';
import { useAppConfigsStore } from "@/stores/appConfigsStore";


onMounted(() => {
  subscribeMQTT()
  const configsStore = useAppConfigsStore();
  for (const [key, value] of Object.entries(sensor_object)) {
    configsStore.setObjectConfigs(value.meshname, value);
  }
  // console.log(configsStore.individualObjectConfig("sensor1_temp"));
})

</script>

<template>
  <div class="body-container">
    <div class="app-bar">
      <AppBar />
    </div>
    <div class="router-page">
      <RouterView />
    </div>
  </div>
</template>

<style>
.body-container {
  width: 100%;
  height: 100%;
  padding: 0;
  margin: 0;
  overflow: hidden;
  display: grid;
  grid-template-columns: auto;
  grid-template-rows: 7% 93%;
}
.app-bar {
  width: 100%;
  height: 100%;
  grid-row: 1;
  padding: 0;
  margin: 0;
}
.router-page {
  grid-template-rows: 100%;
  margin: 0;
  padding: 0;
}
</style>