<template>
  <v-card>
    <v-layout>
      <v-navigation-drawer 
        class="bg-dark"
        theme="dark"
        permanent
        style="margin-top: 60px;"
      >
      <v-list color="gray-darken-2" nav>
        <v-list-item title="Environment" value="Energy"></v-list-item>
        <v-list-item title="Energy" value="Energy"></v-list-item>
        <!-- <v-list-group value="Admin">
          <template v-slot:activator="{ props }">
            <v-list-item
              v-bind="props"
              title="Admin"
            ></v-list-item>
          </template>

          <v-list-item
            v-for="([title], i) in admins"
            :key="i"
            :title="title"
            :value="title"
          ></v-list-item>
        </v-list-group> -->

      </v-list>
      </v-navigation-drawer>
      <!-- <v-main style="height: 250px"></v-main> -->
    </v-layout>
  </v-card>
</template>

<script>
  export default {
    data: () => ({
      open: ['Users'],
      admins: [
        ['Management'],
        ['Settings'],
      ],
    }),
  }
</script>