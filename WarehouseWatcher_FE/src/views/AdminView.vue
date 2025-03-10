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
      <!-- Sidebar content (e.g., navigation, filters) can go here -->
      <p>Admin Panel</p>
    </aside>

    <main class="report-page">
      <h1>Threshold Settings</h1>
      <AdminThreshold />
    </main>
  </div>
</template>

<style scoped>
.admin-container {
  display: flex;
  height: 100vh;
  background-color: #f4f4f4;
}

.side-bar {
  position: fixed;
  left: 0;
  height: calc(100% - 64px);
  top: 64px;
  width: 280px;
  background: #2c3e50;
  color: white;
  padding: 20px;
}

.report-page {
  flex: 1;
  margin-left: 280px; /* Matches sidebar width */
  padding: 20px;
  overflow-y: auto;
}

h1 {
  margin-bottom: 15px;
}
</style>
