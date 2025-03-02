<script setup>
    import Dashboards from '@/components/Dashboards.vue'
</script>

<template>
    <main>
        <Dashboards />
    </main>
</template>
  
<style>
@media (min-width: 1024px) {
    .dashboard {
        min-height: 100vh;
        display: flex;
        align-items: center;
    }
}
</style>