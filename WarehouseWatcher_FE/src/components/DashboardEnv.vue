<script>
import { dashboards } from "@/configs/grafana-config";
export default {
  data() {
    return {
      dashboards,
    }
  },
};
</script>

<template>
  <h3>Environment Sensors</h3>
  <!-- <div v-for="(dashboard) in dashboards.envsensor">
    <iframe class="chart-panel" :src="dashboard.iframelink" :width="dashboard.width" :height="dashboard.height"></iframe>
  </div> -->
</template>

<style scoped>
.chart-panel {
  border: 0;
}
</style>