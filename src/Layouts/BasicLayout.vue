<template>
  <div style="width: 100%;height: 100%">
    <v-dialog v-model="dialogContent" max-width="400px">
      <v-card>
        <v-card-title>密码修改</v-card-title>
        <v-card-text>
          <v-flex sm12 md12 xs12>
            <v-text-field
              v-model="oldPassword"
              placeholder=" 原密码 "
              prepend-inner-icon="lock"
              :append-icon="showO ? 'visibility' : 'visibility_off'"
              :type="showO ? 'text' : 'password'"
              @click:append="showO = !showO"
            ></v-text-field>
          </v-flex>
          <v-flex sm12 md12 xs12>
            <v-text-field
              v-model="newPassword"
              placeholder=" 新密码 "
              prepend-inner-icon="lock"
              :append-icon="showN ? 'visibility' : 'visibility_off'"
              :type="showN ? 'text' : 'password'"
              @click:append="showN = !showN"
            ></v-text-field>
          </v-flex>
          <v-flex sm12 md12 xs12>
            <div style="text-align: center;">
              <v-btn color="primary" style="width: 80%" @click="changePass">
                确认修改
              </v-btn>
            </div>
          </v-flex>
          <v-flex>
            <v-spacer></v-spacer>
          </v-flex>
          <v-flex>
            <v-spacer></v-spacer>
          </v-flex>
        </v-card-text>
      </v-card>
    </v-dialog>

    <div style="display: flex;flex-direction: column;align-items: center;">
      <notification></notification>
    </div>
    <v-navigation-drawer
      v-model="drawer"
      app
      :mini-variant="mini"
      :color="colorRGB"
      dark
    >
      <p></p>
      <v-list-item>
        地图管理系统
      </v-list-item>
      <p></p>
      <v-list dense>
        <template v-for="router in routermaps[0].children">
          <v-list-item
            :key="router.name"
            @click="jumpto(router)"
            v-if="
              router.meta.permission.indexOf(permission) !== -1 &&
                router.meta.group === false
            "
          >
            <v-list-item-action>
              <v-icon>{{ router.meta.icon }}</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>{{ router.name }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-list-group
            :key="router.name"
            :prepend-icon="router.meta.icon"
            v-if="
              router.meta.permission.indexOf(permission) !== -1 &&
                router.meta.group === true
            "
            no-action
          >
            <template v-slot:activator>
              <v-list-item-content>
                <v-list-item-title v-text="router.name"></v-list-item-title>
              </v-list-item-content>
            </template>
            <template v-for="children1 in router.children">
              <v-list-item
                v-if="children1.meta.group === false"
                :key="children1.name"
                @click="jumpto(children1)"
              >
                <v-list-item-content>
                  <v-list-item-title
                    v-text="children1.name"
                  ></v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </template>
          </v-list-group>
        </template>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar app height="60px" flat>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title></v-toolbar-title>
      <v-spacer />
      <v-toolbar-items>
        <v-spacer />

        <v-row align="center" class="mx-0">
          <v-btn icon @click="back">
            <v-icon>
              arrow_back
            </v-icon>
          </v-btn>

          <v-btn icon @click="changeTheme">
            <div v-if="this.darkmode">
              <v-icon>
                brightness_4
              </v-icon>
            </div>

            <div v-if="!this.darkmode">
              <v-icon>
                brightness_5
              </v-icon>
            </div>
          </v-btn>

          <v-menu
            bottom
            offset-y
            open-on-hover
            transition="slide-y-reverse-transition"
          >
            <template v-slot:activator="{ on }">
              <v-btn icon v-on="on">
                <v-icon>
                  person
                </v-icon>
              </v-btn>
            </template>
            <v-list>
              <v-list-item @click="dialogContent = true">
                <v-list-item-title>修改密码</v-list-item-title>
              </v-list-item>

              <v-list-item @click="loginout">
                <v-list-item-title>退出登录</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>
        </v-row>
      </v-toolbar-items>
    </v-app-bar>

    <v-content>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex>
            <router-view />
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </div>
</template>

<script>
import { asyncRouterMap } from "../router/routerConfig";
import notification from "../components/notification.vue";

import crypto from "crypto";

export default {
  name: "BasicLayout",
  components: {
    notification
  },
  props: {
    source: String
  },
  data: () => ({
    drawer: true,
    mini: false,
    colorRGB: "",
    routermaps: {
      ...asyncRouterMap
    },
    permission: "",
    oldPassword: "",
    newPassword: "",
    dialogContent: false,
    index: 0,
    showO: false,
    showN: false,
    darkmode: false
  }),
  created() {
    this.permission = localStorage.getItem("permission");
    if (localStorage.getItem("mode") === undefined) {
      this.darkmode = false;
      this.colorRGB = "#25506B";
      localStorage.setItem("mode", 0);
    } else {
      this.darkmode = localStorage.getItem("mode");
      if (this.darkmode === "1") {
        this.colorRGB = "#303030";
        this.$vuetify.theme.dark = true;
      } else {
        this.colorRGB = "#25506B";
        this.$vuetify.theme.dark = false;
      }
    }
  },
  computed: {},
  methods: {
    back() {
      localStorage.setItem("isBackButton", "1");
      if (window.history.length <= 1) {
        this.$router.push({ path: "/" });
        return false;
      } else {
        this.$router.go(-1);
      }
    },
    changeTheme() {
      this.darkmode = !this.darkmode;
      if (this.darkmode === true) {
        this.colorRGB = "#303030";
        localStorage.setItem("mode", 1);
        this.$vuetify.theme.dark = true;
      } else {
        this.colorRGB = "#25506B";
        localStorage.setItem("mode", 0);
        this.$vuetify.theme.dark = false;
      }
    },
    jumpto(e) {
      if (!Object.prototype.hasOwnProperty.call(e.meta, "add")) {
        this.$router.push(e.path);
      } else {
        let subStr = new RegExp("/:.*"); //创建正则表达式对象
        let path = e.path.replace(subStr, "/" + e.meta.add); //替换路由
        this.$router.push(path);
      }
    },
    changePass() {
      const SignId = localStorage.getItem("SignId");
      const type = localStorage.getItem("permission");
      const id = {
        SignId,
        type
      };
      const md5 = crypto.createHash("md5");
      md5.update(this.oldPassword);
      const oldPassword = md5.digest("hex");
      const md52 = crypto.createHash("md5"); // 第二个md5加密
      md52.update(this.newPassword);
      const newPassword = md52.digest("hex");
      id.oldpass = oldPassword;
      id.newpass = newPassword;
    },
    loginout() {
      localStorage.clear();
      sessionStorage.clear();
      this.$router.push("/login");
    }
  }
};
</script>

<style scoped>
.alert {
  position: fixed;
  top: 0;
  z-index: 9999;
}
</style>
