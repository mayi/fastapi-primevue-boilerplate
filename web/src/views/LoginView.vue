<template>
  <div class="grid">
    <div class="col-12">
      <div class="card">
        <div class="flex justify-content-center align-content-center flex-wrap card-container">
          <div>
            <h3>Log In</h3>
            <span class="p-float-label mt-5">
              <InputText id="username" v-model="username" autocomplete="off" />
              <label for="username">用户名</label>
            </span>
            <span class="p-float-label mt-5">
              <Password inputId="password" v-model="password" />
              <label for="password">密码</label>
            </span>
            <div class="flex justify-content-center mt-5">
              <Button label="登录" @click="loginAction" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref } from "vue";
import toast from "@/utils/toast";
import { useUserStore } from "@/stores/user";

const userStore = useUserStore();

const username = ref("");
const password = ref("");

const loginAction = () => {
  if (username.value === "" || password.value === "") {
    toast.error("用户名或密码不能为空");
    return;
  }
  userStore.login(username.value, password.value);
};
</script>
