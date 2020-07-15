// import Vue from "vue";
import NProgress from "nprogress";
import router from "./router";
// 进度条
import "nprogress/nprogress.css";

const whitelist = ["/login", "/error/404", "/error/403"];
router.beforeEach((to, from, next) => {
  NProgress.start();
  const permission = localStorage.getItem("permission");
  const AccessToken = localStorage.getItem("Access-Token");
  if (to.matched.length === 0) {
    next("/error/404");
  } else if (AccessToken === null && whitelist.indexOf(to.path) === -1) {
    next("/login");
  } else if (AccessToken !== null && to.path === "/login") {
    next("/");
  } else if (
    to.meta.permission.indexOf(permission) === -1 &&
    whitelist.indexOf(to.path) === -1
  ) {
    next("/error/403");
  } else {
    next();
  }
});

router.afterEach(() => {
  NProgress.done();
});
