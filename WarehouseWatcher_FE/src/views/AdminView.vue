<!-- 
 FILE: AdminView.vue
 PROJECT: Warehouse Watcher
 PROGRAMMER: Undefined Chargers - Yujung Park, Aryan Passi
 FIRST VERSION: 2025-03-05
 DESCRIPTION: Admin panel for threshold configuration
-->
<script setup>
import AdminThreshold from '@/components/AdminThreshold.vue';
</script>

<template>
  <div class="admin-container">
    <aside class="side-bar">
      <h2>Admin Panel</h2>
      <nav>
        <ul>
          <li><a href="#">Dashboard</a></li>
          <li><a href="#">Reports</a></li>
          <li><a href="#">Threshold Settings</a></li>
          <li><a href="#">Logs</a></li>
        </ul>
      </nav>
    </aside>

    <main class="report-page">
      <AdminThreshold />
    </main>
  </div>
</template>

<style scoped>
.admin-container {
  display: flex;
  height: 100vh;
  background-color: #f4f4f4;
  color: black;
  /* text-align: center; */
}

/* Sidebar Styling */
.side-bar {
  position: fixed;
  left: 0;
  top: 0;
  width: 280px;
  height: 100%;
  background: #2c3e50;
  color: white;
  padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.side-bar h2 {
  margin-bottom: 20px;
  font-size: 18px;
}

nav ul {
  list-style: none;
  padding: 0;
  width: 100%;
}

nav ul li {
  margin: 10px 0;
}

nav ul li a {
  text-decoration: none;
  color: white;
  font-size: 16px;
  display: block;
  padding: 8px 12px;
  border-radius: 4px;
  transition: background 0.3s;
}

nav ul li a:hover {
  background: #34495e;
}

/* Main Content */
.report-page {
  flex: 1;
  margin-left: 280px; /* Matches sidebar width */
  padding: 20px;
  overflow-y: auto;
}

h1 {
  margin-bottom: 15px;
}

/* Responsive Fix */
@media (max-width: 768px) {
  .side-bar {
    width: 220px;
  }

  .report-page {
    margin-left: 220px;
  }
}

@media (max-width: 480px) {
  .side-bar {
    width: 100%;
    height: auto;
    position: relative;
  }

  .report-page {
    margin-left: 0;
  }
}

.main-title {
  font-size: 2rem;
  margin-bottom: 1.5rem;
}
</style>
