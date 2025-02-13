<template>
  <div class="about-container">
    <!-- Main Title -->
    <h1 class="main-title">About Page</h1>

    <div class="content-wrapper">
      <!-- Side Title & Learn More Section -->
      <section class="side-section">
        <h2>Warehouse Watcher</h2>
        <p>Real-time warehouse monitoring & environmental tracking</p>
        <button class="cta-button" @click="showDetails = !showDetails">
          {{ showDetails ? "Show Less" : "Show More" }}
        </button>
      </section>

      <!-- Expanded Content -->
      <section v-if="showDetails" class="expanded-content">
        <h2>Full Summary</h2>
        <p>
          Warehouse Watcher is a real-time monitoring system designed to enhance warehouse efficiency and safety. 
          It integrates with existing WMS and QMS to provide analytics, tracking, and alert mechanisms.
        </p>

        <h2>Technology & Dashboards</h2>
        <ul>
          <li><strong>Frontend:</strong> Vue.js</li>
          <li><strong>Dashboard:</strong> Grafana</li>
          <li><strong>Database:</strong> InfluxDB</li>
          <li><strong>Communication:</strong> HiveMQ (MQTT broker)</li>
        </ul>

        <h2>Contributors</h2>
        <ul>
          <li>Amel Korandippillil Sunil</li>
          <li>Aryan Pramod Passi</li>
          <li>Salma Rageh</li>
          <li>William Anderson</li>
          <li>Yujung Park</li>
        </ul>
      </section>
    </div>
  </div>
</template>

<script>
export default {
  name: "AboutPage",
  data() {
    return {
      showDetails: false,
    };
  },
};
</script>

<style scoped>
@import './style.css';

.main-title {
  font-size: 3rem;
  text-align: center;
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
}

.expanded-content {
  max-width: 600px;
  text-align: left;
}
</style>
