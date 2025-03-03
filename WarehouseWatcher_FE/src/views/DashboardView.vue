<script setup>
import DrawerDashboard from '@/components/DrawerDashboard.vue';
import EnvDashboard from '@/components/DashboardEnv.vue';
</script>

<template>
  <div class="dashboard-main">
    <div class="side-bar">
      <DrawerDashboard />
    </div>
    <div class="dashboard-page">
      <EnvDashboard />
    </div>
  </div>
</template>

<style>
  .dashboard-main {
    height: 100%;
    display: grid;

  }
  .side-bar {
    left: 0pxz;
    position: fixed;
    height: calc(100% -64px);
    top: 64px;
    bottom: 0;
    width: 300px;
  }
  .dashboard-page {
    height: 100%;
    padding-left: 300px;
    padding-right: 25px;
    padding-top: 20px;
    padding-bottom: 32px;
  }
</style>