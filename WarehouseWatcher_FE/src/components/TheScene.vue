<template>
  <canvas id="bjs-cvs" />
</template>
  
<script lang="ts">
import { defineComponent } from 'vue';
import { WarehouseScene } from "@/scenes/WarehouseScene"

export default defineComponent({
  name: 'BabylonExamples',
  mounted(){
    const canvas = document.querySelector("canvas")!;
    // const canvas = document.getElementById("bjs-cvs")!;
    new WarehouseScene(canvas);
  }
  
});
</script>

<style>
canvas {
  width: 100%;
  height: 100%;
}
</style>
