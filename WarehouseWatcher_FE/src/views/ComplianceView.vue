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
    display: flex;
    overflow: auto;
    width: 100%;
    height: 100%;
    justify-content: center;
  }
  .report-page {
    height: 100%;
    padding-left: 52px;
    padding-right: 52px;
    padding-top: 24px;
    padding-bottom: 24px;
  }
</style>