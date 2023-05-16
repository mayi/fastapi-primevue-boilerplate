import axios from "axios";
import qs from "qs";
import toast from "@/utils/toast";
import router from "@/router/index";
import { whiteList } from "@/utils/settings";
import { redirectToLogin } from "@/utils/jump";

const productionUrl = "/api";
const developmentUrl = "/api";

const request = axios.create({
  baseURL: process.env.NODE_ENV === "development" ? developmentUrl : productionUrl,
  timeout: 60000,
  headers: {
    "Content-Type": "application/json",
  },
  paramsSerializer: (params) => {
    let str = qs.stringify(params, { encode: true, skipNulls: true, arrayFormat: "repeat" });
    for (const i in params) {
      if (Array.isArray(params[i]) && params[i].length === 0) {
        str = str ? `${str}&${i}=` : `${i}=`;
      }
    }
    return str;
  },
});

request.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");

  // 重定向到登录页
  const name = router.currentRoute.value.name;
  if (!token && !whiteList.includes(name)) {
    redirectToLogin();
  }

  config.headers["Authorization"] = "Bearer " + token;
  return config;
});

request.interceptors.response.use(
  (response) => {
    const res = response.data;
    if (res.code === 400) {
      toast.error(res.message);
      return Promise.reject(response.data);
    } else {
      if (res.page) {
        toast.success(`查询到${res.page.total_result}条记录`);
      }
      return response;
    }
  },
  (error) => {
    if (error.response) {
      if (error.response.status === 401) {
        toast.error("登录已过期，请重新登录");
        router.push("/login");
      }
      if (error.response.status === 422) {
        return {"status": 422, "data": error.response.data.detail};
      }
      return Promise.reject(error.response.data);
    }
  }
);

export default request;
