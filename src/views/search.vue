<template>
  <v-container fluid>
    <v-row align="center">
      <v-col class="d-flex" cols="12" sm="4">
        <v-select
          v-model="selected_search"
          :items="search_method"
          label="搜索方式"
          outlined
        ></v-select>
      </v-col>
      <v-col class="d-flex" cols="12" sm="4">
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="搜索"
          single-line
          outlined
        ></v-text-field>
      </v-col>
      <v-col class="d-flex" cols="12" sm="4">
        <div
          style="display: flex;flex-direction: row;justify-content: center;align-items: center"
        >
          <v-btn color="primary" @click="search_confirm">
            确定
          </v-btn>
        </div>
      </v-col>
      <!--      <v-col class="d-flex" cols="12" sm="4">-->
      <!--        <p>-->
      <!--          耗时：ms-->
      <!--        </p>-->
      <!--      </v-col>-->
    </v-row>
    <Table ref="table"></Table>
  </v-container>
</template>

<script>
import Table from "../components/table";
import { getSearchList, getSearchResult } from "../api/normal/normal";

export default {
  name: "search",
  components: {
    Table
  },
  data: () => ({
    search_method: [],
    search: "",
    selected_search: ""
  }),
  created() {
    this.search_init();
  },
  methods: {
    search_init() {
      getSearchList()
        .then(res => {
          if (res.status === 200) {
            for (let i = 0; i < res.data.length; i++) {
              // console.log(res.data[0].name);
              this.search_method.push(res.data[i].name);
            }
            // this.search_method.push(res.data.name);
          }
        })
        .catch();
    },
    search_confirm() {
      this.$refs.table.loading(true);
      let id = this.search_method.indexOf(this.selected_search) + 1;
      let data = { data: Number(this.search) };
      getSearchResult(id, data)
        .then(res => {
          if (res.status === 200) {
            // let list = [res.data];
            // console.log(list);
            this.$refs.table.renew(res.data);
          }
        })
        .catch()
        .finally(() => {
          this.$refs.table.loading(false);
        });
    }
  }
};
</script>

<style scoped></style>
