import { createRouter, createWebHistory } from 'vue-router'
import { getAuth } from "firebase/auth";
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
      meta: { requiresAuth: true },
    },
  ],
})

router.beforeEach((to, from, next) => {
  const auth = getAuth(); 
  const requiresAuth = to.matched.some((record) => record.meta.requiresAuth);

  if (requiresAuth && !auth.currentUser) {
    next("/login"); 
  } else {
    next(); 
  }
});

export default router
