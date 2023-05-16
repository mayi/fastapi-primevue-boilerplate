import request from "@/utils/request";

export function userLogin(params) {
  const bodyFormData = new FormData();
  bodyFormData.append('username', params.username);
  bodyFormData.append('password', params.password);
  return request({
    url: "/user/login",
    method: "post",
    data: bodyFormData,
    headers: { "Content-Type": "multipart/form-data" },
  });
}

export function meLogout() {
  return request({
    url: "/user/me/logout",
    method: "post",
  });
}
