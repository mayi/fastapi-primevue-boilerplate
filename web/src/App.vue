<template>
  <div class="container">
    <div class="header ml-3 mr-3">
      <Menubar :model="items" style="width: 100%">
        <template #start>
          <img src="@/assets/logo.png" class="w-3rem h-3rem mr-2" alt="Logo" />
        </template>
        <template #end>
          <Button v-show="!userStore.isLoggedIn()" label="登录" @click="toLogin" icon="pi pi-sign-in" class="p-button-raised p-button-success" />
          <Button v-show="userStore.isLoggedIn()" label="退出" @click="userStore.logout()" icon="pi pi-sign-out" class="p-button-raised p-button-danger" />
        </template>
      </Menubar>
    </div>
    <div class="content p-3 pt-0">
      <Toast />
      <RouterView />
    </div>
    <div class="footer">
      <i class="pi pi-sun mr-1"></i>
      <p>XXX Management System</p>
    </div>
    <ScrollTop />
  </div>
</template>
<script setup>
import router from "@/router/index";
import { useUserStore } from "@/stores/user";

const userStore = useUserStore();

const items = [
  {
    label: "首页",
    icon: "pi pi-home",
    to: "/",
  },
];

const toLogin = () => {
  router.push("login");
};

</script>
<style scoped>
.container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.header {
  display: flex;
  align-items: center;
  justify-content: left;
}

.content {
  flex: 1;
}

.footer {
  background-color: #f5f5f5;
  color: #333;
  display: flex;
  justify-content: right;
  align-items: center;
  padding: 0.5rem;
  height: 3rem;
}
</style>
