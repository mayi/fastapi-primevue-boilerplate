import { defineStore } from 'pinia'
import { userLogin } from '@/api/user'
import toast from "@/utils/toast";
import { handleRouteHopAfterLogin } from "@/utils/jump";
import router from "@/router/index";

export const useUserStore = defineStore('user', {
  state: () => ({
    token: localStorage.getItem("token"),
  }),
  getters: {
  },
  actions: {
    login(username, password) {
      userLogin({ "username": username, "password": password }).then((res) => {
        if (res.status === 200) {
          localStorage.setItem("token", res.data.access_token);
          this.token = res.data.access_token;
          toast.success("登录成功");
          handleRouteHopAfterLogin();
        } else {
          toast.error(res.msg);
        }
      });
    },
    logout() {
      localStorage.removeItem("token");
      this.token = null;
      toast.success("退出成功");
      router.push("login");
    },
    isLoggedIn() {
      this.token = localStorage.getItem("token");
      return !!this.token;
    }
  },
})
