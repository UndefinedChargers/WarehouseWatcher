<script setup>
import TheDrawer from '@/components/TheDrawer.vue';
import ReportSelect from '@/components/ReportSelect.vue';
import ReportList from '@/components/ReportList.vue';
</script>

<template>
  <div class="compliance-main">
    <!-- <div class="side-bar">
      <TheDrawer />
    </div> -->
    <div class="report-page">
      <ReportSelect />
      <ReportList />
    </div>
  </div>
</template>

<style>
  .compliance-main {
    height: 100%;
    /* display: grid; */

  }
  /* .side-bar {
    left: 0pxz;
    position: fixed;
    height: calc(100% -64px);
    top: 64px;
    bottom: 0;
    width: 300px;
  } */
  .report-page {
    height: 100%;
    padding-left: 52px;
    padding-right: 52px;
    padding-top: 24px;
    padding-bottom: 24px;
  }
</style>