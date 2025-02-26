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
        <v-app-bar
          color="#021324"
          class="v-toolbar v-toolbar--flat"
        >
          <!-- <template v-slot:prepend>
            <v-app-bar-nav-icon></v-app-bar-nav-icon>
          </template> -->
  
          <v-app-bar-title @click="$router.push({path:'/'})">WAREHOUSE WATCHER</v-app-bar-title>
  
          <v-spacer></v-spacer>
          <v-btn @click="$router.push({path:'/dashboard'})"> 
            Dashboard
          </v-btn>
          <v-btn @click="$router.push({path:'/space'})"> 
            Space
          </v-btn>
          <v-btn @click="$router.push({path:'/compliance'})">
            Compliance
          </v-btn>
          <v-btn @click="$router.push({path:'/about'})">
            About
          </v-btn>
        </v-app-bar>
      </v-layout>
    
  </template>

<style scoped>

.app-bar {
  top: 0px;
  z-index: 1010;
  transform: translateY(0px);
  position: fixed;
  left: 0px;
  width: calc(100% - 0px);
}
</style>