<!-- 
 FILE: AppBar.vue
 PROJECT: Warehouse Watcher
 PROGRAMMER: Undefined Chargers - Yujung Park
 FIRST VERSION: 2025-01-10
 DESCRIPTION: 
 References: Starting code- https://vuetifyjs.com/en/components/app-bars/#images
 -->
<template>   
  <v-layout>
    <v-app-bar color="#021324" class="v-toolbar v-toolbar--flat">
      <!-- <template v-slot:prepend>
        <v-app-bar-nav-icon></v-app-bar-nav-icon>
      </template> -->
      <img class="ww-logo" src="/favicon.ico"> 
      <v-app-bar-title @click="$router.push({path:'/'})">WAREHOUSE WATCHER</v-app-bar-title>
      <v-spacer></v-spacer>
      <v-btn @click="$router.push({path:'/about'})">
        About
      </v-btn>
      <v-btn @click="$router.push({path:'/dashboard'})"> 
        Dashboard
      </v-btn>
      <v-btn @click="$router.push({path:'/space'})">
        Space
      </v-btn>
      <v-btn @click="$router.push({path:'/compliance'})">
        Report
      </v-btn>
      <v-btn @click="$router.push({path:'/admin'})">
        Admin
      </v-btn>
      
      <v-btn class="text-none" stacked>
        <v-badge color="error" :content="alert" @click="overlay = !overlay">
        <!-- <v-badge color="error" :content="alert"> -->
          <v-icon>mdi-bell-outline</v-icon>
        </v-badge>
      </v-btn>
    
    </v-app-bar>
  </v-layout>

  <v-container id="alert-container" >
    <v-overlay v-model="overlay" scroll-strategy="block">
      <v-card class="mx-auto alert-card"
      width="270" height="470"
      theme="dark" location="top end" prepend-icon="mdi-bell">
        <template v-slot:title>
          <span class="font-weight-black">Alerts</span>
      </template>
      <v-card-text class="bg-surface-light pt-4">
        <ul>
          <li v-for = "alert in alerts">
            {{ alert[1].timestamp }} : {{ alert[1].alert_object }} - {{ alert[1].alert_type }}
            <!-- {{ key.timestamp }} : {{ key.alert_object }} - {{ key.alert_type }} -->
          </li>
        </ul>
      </v-card-text>
      </v-card>
    </v-overlay>
  </v-container>
</template>

<script setup>
import { useAppConfigsStore } from "@/stores/appConfigsStore";
import { mapState } from "pinia";
import { computed } from "vue";
import { ref } from 'vue'

const overlay = ref(false)

const appNotification = useAppConfigsStore()
const alerts = appNotification.notifications
const alert = computed(() => appNotification.notifications.size) 
console.log(alerts)

</script>

<style scoped>
.app-bar {
  top: 0px;
  z-index: 1010;
  transform: translateY(0px);
  position: fixed;
  left: 0px;
  width: calc(100% - 0px);
}

.btn-alert {
  color: white;
}

.ww-logo {
  width:60px;
  height:50px;
  padding-left: 10px;
}

#alert-container {
  width: 100px;
  height: 100px;
  position: absolute;
  bottom: 10px;
}

.alert-card {
  right: 20px;
  width: 270px;
  height: 470px;
  margin: 70px;
  padding: 10px;
}
</style>