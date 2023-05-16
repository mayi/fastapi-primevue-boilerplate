import router from "@/router/index";
import { whiteList } from "@/utils/settings";

/**
 * 重定向到登录页面
 * 判断当前是否登录页面
 * 重定向之前把原页面完整路径记录到登录页面的 query 中
 * 如果是在路由钩子函数中应该有参数 next，否则需要引入 router 来跳转
 * @param {*} next 在路由钩子中的 next
 */
export function redirectToLogin(next, toName, toFullPath) {
  const targetRoute = { name: "login" };

  if (next.name === targetRoute.name) {
    return next && next();
  }

  if (!whiteList.includes(toName)) {
    Object.assign(targetRoute, { query: { redirect: toFullPath } });
  }

  next ? next(targetRoute) : router.push(targetRoute);
}

// 登录成功后，进行页面跳转
export function handleRouteHopAfterLogin(defaultRoute = { name: "home" }) {
  const { redirect, ...otherQuery } = router.currentRoute.value.query;
  // 根据 redirect 来决定跳转目标
  return router.push(redirect ? { path: redirect, query: otherQuery } : defaultRoute);
}
