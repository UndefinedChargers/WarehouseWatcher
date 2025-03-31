import { createRouter, createWebHistory } from 'vue-router'
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
      path: '/dashboard',
      name: 'dashboard',
      component: DashboardView,
    },
    {
      path: '/space',
      name: 'space',
      component: SpaceView,
    },
    {
      path: '/compliance',
      name: 'compliance',
      component: ReportView,
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
