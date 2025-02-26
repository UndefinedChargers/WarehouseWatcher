<script setup>
import { RouterLink, RouterView } from 'vue-router';
import AppBar from './components/AppBar.vue';
import { onMounted } from 'vue';
import { subscribeMQTT } from'./helper/subscriber';
import { publishMQTT } from'./helper/publisher';
import { warehouseSceneConfig } from './configs/ww-config';


onMounted(() => {
  subscribeMQTT()
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