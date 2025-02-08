<template>
  <div class="cvs">
    <canvas />
  </div>
</template>
  
<script lang="ts">
import { defineComponent } from 'vue';
import {WarehouseScene} from "@/scenes/WarehouseScene"

export default defineComponent({
  name: 'BabylonExamples',
  mounted(){
    const canvas = document.querySelector("canvas")!;
    new WarehouseScene(canvas);
  }
  
});
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto+Condensed&family=Roboto:wght@100;700&display=swap');

#cvs {
  width:100%;
  height:100%;
  margin-top: 40px;
  display:block;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background:none;
}

p {
  color:white;
  background:none;
  margin-bottom:1rem;
  font-family: 'Roboto Condensed';
  font-weight: 400;
  font-size:2rem;
}

canvas {
  width: 100%;
  height: 100%;
  background: none;
  border-radius: 4px;
  border: none;
  outline: none;
  box-shadow:8px 8px 10px -6px #000000;
}



</style>