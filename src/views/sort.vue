<template>
  <v-container fluid>
    <v-row align="center">
      <v-col class="d-flex" cols="12" sm="4">
        <v-select
          v-model="selected_method"
          :items="sort_method"
          label="排序方式"
          outlined
          @change="methodChange"
        ></v-select>
      </v-col>
      <v-col class="d-flex" cols="12" sm="4">
        <p>耗时:{{ cost }}ms</p>
      </v-col>
    </v-row>
    <Table ref="table"></Table>
  </v-container>
</template>

<script>
import Table from "../components/table";
import { getSortMethod, getSortResult } from "../api/normal/normal";

export default {
  name: "sort",
  components: {
    Table
  },
  data: () => ({
    sort_method: [],
    selected_method: "",
    cost: ""
  }),
  created() {
    this.sort_init();
  },
  methods: {
    sort_init() {
      getSortMethod()
        .then(res => {
          if (res.status === 200) {
            // this.sort_method = res.data;
            for (let i = 0; i < res.data.length; i++) {
              this.sort_method.push(res.data[i].name);
            }
          }
        })
        .catch();
    },
    methodChange() {
      this.$refs.table.loading(true);
      let i = this.sort_method.indexOf(this.selected_method) + 1;
      let time = {
        start: this.$refs.table.start,
        end: this.$refs.table.end
      };
      getSortResult(i, time)
        .then(res => {
          if (res.status === 200) {
            this.cost = res.data.time;
            this.$refs.table.renew(JSON.parse(res.data.info));
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
