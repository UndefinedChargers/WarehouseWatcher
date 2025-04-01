<!-- 
 FILE: SignUp.vue
 PROJECT: Warehouse Watcher
 PROGRAMMER: Undefined Chargers - Salma Rageh
 FIRST VERSION: 
 DESCRIPTION: 
 References: Starting code- https://vuetifyjs.com/en/components/text-fields/#password-input
-->
 
<template>
  <div>
    <!-- <img src="/images/wwlogo.jpg" alt="logo"/> -->
    <v-card
      class="mx-auto ma-10 pa-12 pb-8 v-theme--dark"
      elevation="8"
      max-width="448"
      rounded="lg"
    >
      <div class="text-subtitle-1 text-medium-emphasis">Account</div>

      <v-text-field
        v-model="email"
        density="compact"
        placeholder="Email address"
        prepend-inner-icon="mdi-email-outline"
        variant="outlined"
      ></v-text-field>

      <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
        Password
      </div>

      <v-text-field
        v-model="password"
        :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
        :type="visible ? 'text' : 'password'"
        density="compact"
        placeholder="Enter your password"
        prepend-inner-icon="mdi-lock-outline"
        variant="outlined"
        @click:append-inner="visible = !visible"
      ></v-text-field>

      <v-alert v-if="error" type="error" class="mb-3">{{ error }}</v-alert>

      <v-btn
        class="mb-8"
        color="blue"
        size="large"
        variant="tonal"
        block
        @click="signUp"
      >
        Sign Up
      </v-btn>

      <v-card-text class="text-center">
          <router-link to="/login" class="text-blue text-decoration-none">
              Already have an account? Log in <v-icon icon="mdi-chevron-right"></v-icon>
          </router-link>
      </v-card-text>

    </v-card>
  </div>
</template>

<script>
import { ref } from "vue";
import { auth } from "../configs/firebase";
import { createUserWithEmailAndPassword } from "firebase/auth";
import { useRouter } from "vue-router";

export default {
  setup() {
      const email = ref("");
      const password = ref("");
      const visible = ref(false);
      const error = ref(null);
      const router = useRouter();

      const signUp = async () => {
          try {
          await createUserWithEmailAndPassword(auth, email.value, password.value);
          console.log("Successfully Registered");
          router.push("/login");
          } catch (err) {
              error.value = "Failed to create account.";
          }
      };

      return { email, password, visible, error, signUp };
  },
};
</script>

<style scoped> 
img {
display: block;
margin: auto;
width: 30%;
}
</style>