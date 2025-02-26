<script setup>
import TheDrawer from '@/components/TheDrawer.vue';
import ReportArea from '@/components/ReportArea.vue';
</script>

<template>
  <div class="compliance-main">
    <div class="side-bar">
      <TheDrawer />
    </div>
    <div class="report-page">
      <ReportArea />
    </div>
  </div>
</template>

<style>
  .compliance-main {
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
  .report-page {
    height: 100%;
    padding-left: 300px;
    padding-right: 25px;
    padding-top: 20px;
    padding-bottom: 32px;
  }
</style>