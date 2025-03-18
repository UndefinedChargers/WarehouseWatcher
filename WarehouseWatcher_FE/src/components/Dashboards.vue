<template>
  <div class="dashboard-container">
    <h1 class="main-title">Grafana Dashboard Display</h1>

    <div class="content-wrapper">
      <!-- Side Panel -->
      <section class="side-section">
        <h2>Select Dashboard</h2>
        <label>Select Category:</label>
        <select v-model="selectedCategory">
          <option v-for="(dashboards, category) in grafanaDashboards" :key="category" :value="category">
            {{ formatCategoryName(category) }}
          </option>
        </select>

        <div v-if="selectedCategory">
          <label>Select Dashboard:</label>
          <select v-model="selectedDashboard">
            <option v-for="dashboard in grafanaDashboards[selectedCategory]" :key="dashboard.name" :value="dashboard.link">
              {{ dashboard.name }}
            </option>
          </select>
        </div>
      </section>

      <!-- Dashboard Display -->
      <section v-if="selectedDashboard" class="dashboard-display">
        <iframe :src="selectedDashboard" frameborder="0" allowfullscreen></iframe>
      </section>
    </div>
  </div>
</template>

<script>
export default {
  name: "GrafanaDashboardDisplay",
  data() {
    return {
      grafanaDashboards: {
        "Energy Consumption": [
          {
            name: "Energy Consumption Last 2 Days",
            link: "https://172.206.30.225:3000/d/beerjk87fqw3kc/energy-consumption-last-2-days?orgId=2&from=now-2d&to=now&timezone=browser&refresh=30m"
          },
          {
            name: "Energy Consumption Last 30 Days",
            link: "https://172.206.30.225:3000/d/eeff59kj7oav4c/energy-consumption-last-30-days?orgId=2&from=now-30d&to=now&timezone=browser&refresh=30m"
          }
        ],
        "Environment": [
          {
            name: "Environment Last 30 Days",
            link: "https://172.206.30.225:3000/d/aeffh96iz7bb4b/environment-last-30-days?orgId=2&from=now-30d&to=now&timezone=browser&refresh=30m"
          },
          {
            name: "Environment Last Hour",
            link: "https://172.206.30.225:3000/d/deffalkw79slcb/environment-last-hour?orgId=2&from=now-1h&to=now&timezone=browser&refresh=30m"
          },
          {
            name: "Environment Real-Time",
            link: "https://172.206.30.225:3000/d/eeffszsys7pc0d/environment-real-time?orgId=2&from=now-5m&to=now&timezone=browser&refresh=5m"
          }
        ]
      },
      selectedCategory: Object.keys(this.grafanaDashboards)[0] || "",
      selectedDashboard: "",
    };
  },
  watch: {
    selectedCategory(newCategory) {
      // Automatically set the selectedDashboard to the first dashboard in the selected category
      this.selectedDashboard = this.grafanaDashboards[newCategory]?.[0]?.link || "";
    }
  },
  mounted() {
    // Set default dashboard when the component mounts
    if (this.selectedCategory) {
      this.selectedDashboard = this.grafanaDashboards[this.selectedCategory][0].link;
    }
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
  font-family: "Poppins", sans-serif;
  color: white;
  text-align: center;
  padding: 2rem;
}

.main-title {
  font-size: 3rem;
  margin-bottom: 1.5rem;
}

.content-wrapper {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  gap: 2rem;
  flex-wrap: wrap;
}

.side-section {
  text-align: center;
  max-width: 400px;
  background: rgba(255, 255, 255, 0.1);
  padding: 1.5rem;
  border-radius: 10px;
}

h2 {
  color: #ff00ff;
}

label {
  display: block;
  font-size: 1.2rem;
  margin-top: 1rem;
}

select {
  font-size: 1rem;
  padding: 0.5rem;
  border-radius: 5px;
  background: #1e1e1e;
  color: white;
  border: none;
  width: 100%;
}

.dashboard-display {
  max-width: 800px;
  width: 100%;
  height: 500px;
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
