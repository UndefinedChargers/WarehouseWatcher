<script setup>
import { useAppConfigsStore } from "@/stores/appConfigsStore";
let obj = "sensor1_temp";
let member = "min_threshold";
let value = 22;
const objectConfig = useAppConfigsStore();
const updateConfigs = () => {
	objectConfig.setObjectMemberValue(obj, member, value)
};

</script>

<template>
  <div>Threshhold</div>
  <button @click="updateConfigs()">submit</button>
</template>

<style scoped>
</style>