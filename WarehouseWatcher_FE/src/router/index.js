import { createRouter, createWebHistory } from 'vue-router'
import { getAuth, onAuthStateChanged } from "firebase/auth";
import { getFirestore, doc, getDoc } from "firebase/firestore";
import { db } from "@/configs/firebase";
import SignUp from "../components/SignUp.vue";
import LogIn from "../components/LogIn.vue";
import HomeView from '../views/HomeView.vue'
import DashboardView from '../views/DashboardView.vue'
import SpaceView from '../views/SpaceView.vue'
import ReportView from '../views/ComplianceView.vue'
import AboutView from '../views/AboutView.vue'
import AdminView from '../views/AdminView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/login',
      name: 'login',
      component: LogIn,
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUp,
    }, 
    {
      path: '/dashboard',
      name: 'dashboard',
      component: DashboardView,
      meta: { requiresAuth: true },
    },
    {
      path: '/space',
      name: 'space',
      component: SpaceView,
      meta: { requiresAuth: true },
    },
    {
      path: '/compliance',
      name: 'compliance',
      component: ReportView,
      meta: { requiresAuth: true },
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView,
      // component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/admin',
      name: 'admin',
      component: AdminView,
      meta: { requiresAuth: true, requiresAdmin: true },
    },
  ],
})

router.beforeEach(async (to, from, next) => {
  const auth = getAuth();

  const user = await new Promise(resolve => {
      onAuthStateChanged(auth, resolve);
  });

  if (to.matched.some(record => record.meta.requiresAuth) && !user) {
      next("/login"); 
  } else if (to.matched.some(record => record.meta.requiresAdmin)) {
      if (!user) {
          next("/login");
      } else {
          const userDoc = await getDoc(doc(db, "users", user.uid));
          if (userDoc.exists()) {
              next(); 
          } else {
              next("/");
          }
      }
  } else {
      next();
  }
});


export default router
