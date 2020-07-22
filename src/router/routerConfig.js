import BasicLayout from "../Layouts/BasicLayout";
import LoginLayout from "../Layouts/LoginLayout";

export const asyncRouterMap = [
  {
    path: "/",
    name: "Basic",
    component: BasicLayout,
    redirect: "/home",
    children: [
      {
        path: "/home",
        name: "数据展示",
        component: () => import("../views/Home"),
        meta: {
          permission: ["1", "2", "3", "4", "5"],
          icon: "home",
          group: false
        }
      },
      {
        path: "/sort",
        name: "数据排序",
        component: () => import("../views/sort"),
        meta: {
          permission: ["1", "2", "3", "4", "5"],
          icon: "category",
          group: false
        }
      },
      {
        path: "/search",
        name: "数据搜索",
        component: () => import("../views/search"),
        meta: {
          permission: ["1", "2", "3", "4", "5"],
          icon: "mdi-magnify",
          group: false
        }
      },
      {
        path: "/update",
        name: "更新",
        component: () => import("../views/update"),
        meta: {
          permission: ["1", "2", "3", "4", "5"],
          icon: "vertical_align_top",
          group: false
        }
      },
      {
        path: "/map",
        name: "地图",
        component: () => import("../views/mapView"),
        meta: {
          permission: ["1", "2", "3", "4", "5"],
          icon: "map",
          group: false
        }
      }
    ]
  }
];

export const constantRouterMap = [
  {
    path: "/error",
    component: BasicLayout,
    children: [
      {
        path: "/error/404",
        component: () => import("../views/error/404"),
        meta: {
          permission: "all"
        }
      },
      {
        path: "/error/403",
        component: () => import("../views/error/403"),
        meta: {
          permission: "all"
        }
      }
    ]
  },
  {
    path: "/",
    redirect: "/home"
  },
  {
    path: "/login",
    component: LoginLayout,
    meta: {
      permission: "all"
    }
  }
];
