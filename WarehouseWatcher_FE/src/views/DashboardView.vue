<script setup>
    import Dashboards from '@/components/Dashboards.vue'
</script>

<template>
    <div class="dashboard">
        <Dashboards />
    </div>
</template>
  
<style scoped>
/* Default Styles for Mobile and Small Screens */
.dashboard {
    display: flex;
    overflow: auto;
    width: 100%;
    height: 100%;
    flex-direction: column; /* Stack elements */
    align-items: center; /* Center content */
    justify-content: center;
    min-height: 100vh;
    text-align: center; /* Align text */
    /* padding: 1rem;  */
    /* Optional: Add some padding for smaller screens */
}

/* Styles for Larger Screens (Desktop) */
@media (min-width: 1024px) {
    .dashboard {
        /* Center content and make sure it remains centered on larger screens */
        display: flex;
        overflow: auto;
        width: 100%;
        height: 100%;
        overflow: scroll;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        min-height: 100%;
    }
}

@media (max-width: 600px) {
    .dashboard {
        display: flex;
        overflow: auto;
        width: 100%;
        height: 100%;
        overflow: scroll;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        min-height: 100%;
    }
}

</style>
