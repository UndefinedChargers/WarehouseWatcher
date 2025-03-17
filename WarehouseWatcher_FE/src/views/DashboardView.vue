<script setup>
    import Dashboards from '@/components/Dashboards.vue'
</script>

<template>
    <main class="dashboard">
        <Dashboards />
    </main>
</template>
  
<style scoped>
/* Default Styles for Mobile and Small Screens */
.dashboard {
    display: flex;
    flex-direction: column; /* Stack elements */
    align-items: center; /* Center content */
    justify-content: center;
    min-height: 100vh;
    text-align: center; /* Align text */
    padding: 1rem; /* Optional: Add some padding for smaller screens */
}

/* Styles for Larger Screens (Desktop) */
@media (min-width: 1024px) {
    .dashboard {
        /* Center content and make sure it remains centered on larger screens */
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        min-height: 100vh;
    }
}
</style>
