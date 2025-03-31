<template>
  <div class="dashboard-container">
    <h1 class="main-title">Grafana Dashboard Display</h1>

    <div class="content-wrapper">
      <!-- Side Panel -->
      <section class="side-section">
        <!-- <h2>Select Dashboard</h2> -->
        <div class="select-category">
          <label>Select Category:</label>
          <select v-model="selectedCategory">
            <option v-for="(dashboards, category) in grafanaDashboards" :key="category" :value="category">
              {{ formatCategoryName(category) }}
            </option>
          </select>
        </div>

        <div class="select-dashboard" v-if="selectedCategory">
          <label>Select Dashboard:</label>
          <select v-model="selectedDashboard">
            <option v-for="dashboard in grafanaDashboards[selectedCategory]" :key="dashboard.name" :value="dashboard.link">
              {{ dashboard.name }}
            </option>
          </select>
        </div>
      </section>
    </div>
    <!-- Dashboard Display -->
    <section v-if="selectedDashboard" class="dashboard-display">
      <iframe :src="selectedDashboard" frameborder="0" allowfullscreen></iframe>
    </section>

  </div>
</template>

<script>
import { grafana_dashboards } from "@/configs/grafana-config";

export default {
  name: "GrafanaDashboardDisplay",
  data() {
    return {
      grafanaDashboards: grafana_dashboards,
      selectedCategory: Object.keys(grafana_dashboards)[0] || "",
      selectedDashboard: "",
    };
  },
  methods: {
    formatCategoryName(category) {
      return category.replace(/([A-Z])/g, " $1").replace(/^./, str => str.toUpperCase());
    }
  }
};
</script>

<style scoped>
.dashboard-container {
  width: 100%;
  height: 100%;
  font-family: "Poppins", sans-serif;
  color: white;
  text-align: center;
  padding: 1rem 4rem 0 4rem;
}

.main-title {
  font-size: 2rem;
  margin-bottom: 1.5rem;
}

.content-wrapper {
  align-items: center;
  /* margin: 0 15rem; */
  /* display: flex; */
  /* justify-content: center; */
  /* align-items: flex-start; */
  /* gap: 2rem; */
  /* flex-wrap: wrap; */
}

.side-section {
  display: grid;
  grid-column: auto auto;
  align-self: center;
  /* text-align: center; */
  background: rgba(255, 255, 255, 0.1);
  padding: 1rem;
  border-radius: 10px;
}

.select-category {
  display: grid;
  grid-column: 1;
}
.select-dashboard {
  display: grid;
  grid-column: 2;
}

h2 {
  color: #ff00ff;
}

label {
  grid-column: 1;
  font-size: 1rem;
  padding: 0.5rem;
}

select {
  grid-column: 2;
  font-size: 1rem;
  padding: 0.5rem;
  border-radius: 5px;
  background: #1e1e1e;
  color: white;
  border: none;
  /* width: 300px; */
  width: 100%;
}

.dashboard-display {
  /* max-width: 800px; */
  /* height: 500px; */
  margin-top: 1rem;
  /* padding: 1rem; */
  width: 100%;
  height: 100vh;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0px 0px 20px rgba(255, 0, 255, 0.3);
  overflow-y: auto; /* Enable vertical scroll */
}

iframe {
  width: 100%;
  height: 100%;
  border: none;
}


</style>
