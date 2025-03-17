<!-- 
 FILE: AdminView.vue
 PROJECT: Warehouse Watcher
 PROGRAMMER: Undefined Chargers - Aryan Passi
 FIRST VERSION: 2025-03-15
 DESCRIPTION: About Page for WMS
-->
<template>
  <div class="about-container">
    <!-- Main Title -->
    <h1 class="main-title">About</h1>

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
        <h2>Overview</h2>
        <p>
          Warehouse Watcher is a real-time monitoring system designed to enhance warehouse efficiency and safety. 
          It integrates with existing WMS and QMS to provide analytics, tracking, and alert mechanisms.
        </p>

        <h2>Features</h2>
        <ul>
          <li><strong>Dashboard</strong> Your Data to Valuable Business Insights</li>
          <li><strong>Space</strong> Optimzation of Warehouse Operation in 3D Space</li>
          <li><strong>Compliance</strong> Daily Facility Reports for Your Regulatory Compliance</li>
        </ul>

        <h2>The Team</h2>
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
.about-container {
  font-family: 'Poppins', sans-serif;
  color: white;
  /* background: #121212; */
  text-align: center;
  padding: 2rem;
}

.hero {
  background: url('https://source.unsplash.com/1600x900/?warehouse,technology') center/cover;
  height: 60vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.7);
}

.hero h1 {
  font-size: 3rem;
  font-weight: 600;
  margin: 0;
}

.hero p {
  font-size: 1.2rem;
  margin-bottom: 1rem;
}

.cta-button {
  background: linear-gradient(45deg, #ff00ff, #6600ff);
  padding: 10px 20px;
  border: none;
  font-size: 1rem;
  cursor: pointer;
  border-radius: 5px;
  color: white;
  transition: 0.3s;
}

.cta-button:hover {
  background: linear-gradient(45deg, #ff1493, #4b0082);
}

.expanded-content {
  background: rgba(255, 255, 255, 0.1);
  padding: 2rem;
  margin: 1rem 0;
  border-radius: 10px;
  text-align: left;
  max-width: 800px;
  margin: 2rem auto;
}

.expanded-content h2 {
  text-align: center;
  color: #ff00ff;
}

.expanded-content ul {
  list-style-type: none;
  padding: 0;
  text-align: center;
}

.expanded-content li {
  padding: 5px;
}

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