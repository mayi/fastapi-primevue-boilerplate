import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from "@/stores/user";
import { redirectToLogin } from "@/utils/jump";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/HomeView.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue')
    },
  ]
})

router.beforeEach((to, from, next) => {
  const userStore = useUserStore();
  if (to.matched.some((record) => record.meta.requiresAuth) && !userStore.isLoggedIn()) {
    redirectToLogin(next, to.name, to.fullPath);
  } else {
    next();
  }
});

export default router
