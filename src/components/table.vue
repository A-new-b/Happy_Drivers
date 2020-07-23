<template>
  <div>
    <v-dialog v-model="dialog" max-width="500px">
      <v-card>
        <v-card-title>
          <span class="headline">提示</span>
        </v-card-title>
        <v-card-text>
          <p>数据总条数:{{ nums }}</p>
          <p>
            因考虑用户端的体验，数据表格默认返回前1-20条数据，若想查看更多数据请输入您想要查看的数据范围
          </p>
          <p>警告：不要输入负数数据以及除数据外其他字符</p>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="dialog_change(false)">
            关闭
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <div
      style="display: flex;flex-direction: row;justify-content: center;align-items: center"
      v-if="img_flag"
    >
      <v-img
        :src="img_src"
        max-width="500"
        max-height="300"
        aspect-ratio="1.4"
        contain
      >
      </v-img>
    </div>
    <v-data-table
      v-model="selected"
      :headers="headers"
      :items="desserts"
      item-key="linkId"
      :footer-props="{
        showCurrentPage: true,
        itemsPerPageText: '每页记录数',
        showFirstLastPage: true
      }"
      class="elevation-1"
      :loading="loading_status"
      loading-text="正在加载..."
      no-results-text="无匹配数据"
      no-data-text="暂无数据"
      :show-select="ifSelect"
      :single-select="false"
    >
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>数据表格</v-toolbar-title>
          <v-icon @click="dialog_change(true)">help</v-icon>
          <v-spacer></v-spacer>
          <div style="width: 60px;height: 40px">
            <v-text-field
              v-model="start"
              label="条数"
              single-line
              outlined
              dense
            ></v-text-field>
          </div>
          <v-icon>trending_flat</v-icon>
          <div style="width: 60px;height: 40px">
            <v-text-field
              v-model="end"
              label="条数"
              single-line
              outlined
              dense
            ></v-text-field>
          </div>
          <v-spacer></v-spacer>
          <v-btn color="primary" @click="table_init">确定</v-btn>
          <div v-if="ifSelect" style="margin-left: 1%">
            <v-btn color="accent" @click="map_build">生成地图</v-btn>
          </div>
        </v-toolbar>
      </template>
    </v-data-table>
  </div>
</template>

<script>
import { getData, mapCreate } from "../api/normal/normal";
import { notify } from "./notification";
export default {
  name: "Table",
  props: ["ifSelect"],
  data: () => ({
    headers: [
      { text: "标号", sortable: false, value: "linkId" },
      { text: "岔路数", value: "brunch", sortable: false },
      { text: "分类番号", value: "dispClass", sortable: false },
      { text: "名称", value: "roadName", sortable: false }
    ],
    desserts: [],
    loading_status: false,
    start: 1,
    end: 20,
    nums: "",
    dialog: "",
    selected: [],
    img_flag: false,
    img_src: ""
  }),
  created() {
    this.table_init();
  },
  methods: {
    table_init() {
      if (isNaN(Number(this.start)) || isNaN(Number(this.end))) {
        notify("error", "请输入数字");
      } else {
        this.loading_status = true;
        let time = {
          start: Number(this.start) - 1,
          end: Number(this.end)
        };

        getData(time)
          .then(res => {
            if (res.status === 200) {
              this.desserts = JSON.parse(res.data.info);
              this.nums = res.data.nums;
              for (let i = 0; i < this.desserts.length; i++) {
                if (this.desserts[i].roadName === "") {
                  this.desserts[i].roadName = "无";
                }
              }
            }
          })
          .catch()
          .finally(() => {
            this.loading_status = false;
          });
      }
    },
    loading(i) {
      this.loading_status = i === true;
    },
    renew(data) {
      this.desserts = data;
      for (let i = 0; i < this.desserts.length; i++) {
        if (this.desserts[i].roadName === "") {
          this.desserts[i].roadName = "无";
        }
      }
    },
    dialog_change(i) {
      this.dialog = i === true;
    },
    map_build() {
      console.log(this.selected);
      this.loading_status = true;
      mapCreate(this.selected)
        .then(res => {
          // this.img_src = "https://picsum.photos/510/300?random";
          const num = Math.ceil(Math.random() * 100); // 生成一个随机数（防止缓存）
          this.img_src = "/api/img?imgUrl=" + res.data.path + "&&random=" + num;
          console.log(res);
          this.img_flag = true;
        })
        .catch()
        .finally(() => {
          this.loading_status = false;
        });
    }
  }
};
</script>

<style scoped></style>
