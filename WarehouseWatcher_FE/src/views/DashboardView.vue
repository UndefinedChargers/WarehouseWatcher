<script setup>
    import Dashboards from '@/components/Dashboards.vue'
</script>

<template>
    <main class="dashboard">
        <Dashboards />
    </main>
</template>
  
<style>
@media (min-width: 1024px) {
    .dashboard {
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center; /* Center content */
        flex-direction: column; /* Stack elements */
        text-align: center; /* Align text */
    }
}
</style>
