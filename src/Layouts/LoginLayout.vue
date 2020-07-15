<template>
  <v-container fluid fill-height>
    <notification></notification>
    <v-layout>
      <div style="width: 100%">
        <v-card-title
          style="display: flex;flex-direction: row;align-items: center;
                background: linear-gradient(to right, #25506B, aqua);
                -webkit-background-clip: text;
                color: transparent;                "
          class="text-h4"
        >
          电子地图管理系统
        </v-card-title>

        <v-card-text class="backgroud">
          <template v-if="screenWidth > 700">
            <v-img
              :src="require('../assets/background2.jpg')"
              :width="width"
              style="display: flex;flex-direction: row;justify-content: end;align-items:center;"
              :aspect-ratio="changeImg()"
            >
              <div
                style="display: flex;flex-direction: row;justify-content: center;margin-top: 3%"
              >
                <v-card
                  class="loginpanel"
                  :width="width * 0.612"
                  max-width="350"
                  style="margin-right: 5%"
                >
                  <v-card-title>欢迎登录地图管理系统</v-card-title>

                  <v-card-text>
                    <v-form ref="form" lazy-validation>
                      <v-text-field
                        v-model="username"
                        type="text"
                        placeholder="用户名"
                        prepend-inner-icon="person"
                        :rules="rules"
                      ></v-text-field>

                      <v-text-field
                        v-model="password"
                        placeholder=" 密码 "
                        prepend-inner-icon="lock"
                        :append-icon="show ? 'visibility' : 'visibility_off'"
                        :type="show ? 'text' : 'password'"
                        @click:append="show = !show"
                        autocomplete="new-password"
                        :rules="rules"
                      ></v-text-field>

                      <div
                        style="display: flex;flex-direction: row;flex-wrap: nowrap"
                      >
                        <v-text-field
                          v-model="yzm"
                          placeholder="验证码"
                          type="text"
                          prepend-inner-icon="info"
                          style="margin-right: 5%"
                          :rules="rules"
                        ></v-text-field>
                        <!--                        <v-img-->
                        <!--                                :src="img"-->
                        <!--                                max-width="100"-->
                        <!--                                contain-->
                        <!--                                @click="codechange"-->
                        <!--                        ></v-img>-->
                      </div>
                      <v-btn
                        color="primary"
                        block
                        dark
                        miyn-height="46"
                        @click="Login"
                        >登录</v-btn
                      >
                    </v-form>
                  </v-card-text>
                </v-card>
              </div>
            </v-img>
          </template>

          <template v-else>
            <v-card
              class="loginpanel"
              max-width="350"
              style="background: rgba(255, 255, 255, 0.75);"
            >
              <v-card-title>欢迎登录</v-card-title>

              <v-card-text>
                <v-form ref="form" lazy-validation>
                  <v-text-field
                    v-model="username"
                    type="text"
                    placeholder="用户名"
                    prepend-inner-icon="person"
                    :rules="rules"
                  ></v-text-field>

                  <v-text-field
                    v-model="password"
                    placeholder=" 密码 "
                    prepend-inner-icon="lock"
                    :append-icon="show ? 'visibility' : 'visibility_off'"
                    :type="show ? 'text' : 'password'"
                    @click:append="show = !show"
                    autocomplete="new-password"
                    :rules="rules"
                  ></v-text-field>

                  <div
                    style="display: flex;flex-direction: row;flex-wrap: nowrap"
                  >
                    <v-text-field
                      v-model="yzm"
                      placeholder="验证码"
                      type="text"
                      prepend-inner-icon="info"
                      style="margin-right: 5%"
                      :rules="rules"
                    ></v-text-field>
                    <!--                    <v-img-->
                    <!--                            :src="img"-->
                    <!--                            max-width="100"-->
                    <!--                            contain-->
                    <!--                            @click="codechange"-->
                    <!--                    ></v-img>-->
                  </div>
                  <v-btn
                    color="primary"
                    block
                    dark
                    miyn-height="46"
                    @click="Login"
                    >登录</v-btn
                  >
                </v-form>
              </v-card-text>
            </v-card>
          </template>
        </v-card-text>
      </div>
      <v-footer style="width: 100%;position: fixed;bottom: 0;"
        >Copyright © 2020</v-footer
      >
    </v-layout>
  </v-container>
</template>

<script>
// import { URL } from "../api/baseURL";
import notification from "../components/notification.vue";

export default {
  name: "LoginLayout",
  components: { notification },
  data() {
    return {
      show: false,
      username: "",
      password: "",
      messageshow: true,
      yzm: "",
      type: "",
      // img: `${URL}GetVerifyCode`,
      screenWidth: "",
      screenHeight: "",
      rules: [value => !!value || "不许为空"]
    };
  },
  computed: {
    width: function() {
      return this.screenWidth * 0.82;
    }
  },
  created() {
    this.codechange();
  },
  watch: {
    $route() {
      this.codechange();
    }
  },
  mounted() {
    this.screenWidth = document.body.clientWidth;
    this.screenHeight = document.body.clientHeight;
    window.onresize = () =>
      (() => {
        this.screenWidth = document.body.clientWidth;
        this.screenHeight = document.body.clientHeight;
      })();
  },
  methods: {
    codechange() {
      const num = Math.ceil(Math.random() * 10); // 生成一个随机数（防止缓存）
      this.img = `${this.img}?${num}`;
    },
    Login() {
      // const password = this.password; //md5.digest("hex");
      // const type = 3;
      // const para = {
      //   username: this.username,
      //   password,
      //   type,
      //   yzm: this.yzm
      // };
      localStorage.setItem("Access-Token", "test_token");
      localStorage.setItem("permission", "3");
      this.$router.push("/home");
      // login(para)
      //   .then(res => {
      //     if (res.data.status.toString() === "1000") {
      //       notify("success", "登陆成功");
      //       localStorage.setItem("Access-Token", res.data.token);
      //       localStorage.setItem("permission", "3");
      //       localStorage.setItem("SignId", res.data.SignId);
      //       this.$router.push("/home");
      //     } else if (res.data.status.toString() === "1001") {
      //       notify("error", "账号密码不得为空");
      //       this.codechange();
      //     } else if (res.data.status.toString() === "1003") {
      //       notify("error", "账号密码错误");
      //       this.codechange();
      //     } else if (res.data.status.toString() === "1002") {
      //       notify("error", "验证码错误");
      //       this.codechange();
      //     } else {
      //       notify("error", "网络错误，请重试");
      //       this.codechange();
      //     }
      //   })
      //   .catch();
    },
    changeImg() {
      return this.screenWidth / this.screenHeight + 0.04;
    }
  }
};
</script>

<style scoped>
.backgroud {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.loginpanel {
  display: flex;
  flex-direction: column;
  align-items: center;
  background: rgba(255, 255, 255, 0.75);
}
</style>
