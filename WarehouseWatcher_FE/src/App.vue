<script setup>
import { RouterLink, RouterView } from 'vue-router'
import AppBar from './components/AppBar.vue';
import { onMounted } from 'vue'
import { subscribeMQTT } from'./helper/subscriber';
import { publishMQTT } from'./helper/publisher';
import { warehouseSceneConfig } from './configs/ww-config';

onMounted(() => {
  subscribeMQTT()
})

</script>

<template>
  <div class="appview">
    <div class="appbar">
      <AppBar />
    </div>
    <div class="routerview">
      <RouterView />
    </div>
  </div>
</template>

<style>
.appview {
  width: 100vw;
  height: 100vh;
}
.appbar {
  height: 7%;
}
.routerview {
  height: 93%;
}

canvas {
  width: 100%;
  height: 85%;
  margin: 0;
  padding: 0;
}
</style>