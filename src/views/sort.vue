<template>
  <v-container fluid>
    <v-row align="center">
      <v-col class="d-flex" cols="12" sm="4">
        <v-select :items="sort_method" label="排序方式" outlined></v-select>
      </v-col>
      <v-col class="d-flex" cols="12" sm="4">
        <p>耗时:</p>
      </v-col>
    </v-row>
    <Table :desserts="desserts"></Table>
  </v-container>
</template>

<script>
import Table from "../components/table";
export default {
  name: "sort",
  components: {
    Table
  },
  data: () => ({
    desserts: [],
    sort_method: []
  }),
  created() {
    this.sort_init();
  },
  methods: {
    sort_init() {
      this.sort_method = ["冒泡排序"];
      this.desserts = [
        { linkId: 1234, brunch: 2, disPClass: 3, roadName: "青年大街" },
        { linkId: 1234, brunch: 2, disPClass: 3, roadName: "青年大街" },
        { linkId: 1234, brunch: 2, disPClass: 3, roadName: "青年大街" },
        { linkId: 1234, brunch: 2, disPClass: 3, roadName: "青年大街" },
        { linkId: 1234, brunch: 2, disPClass: 3, roadName: "青年大街" }
      ];
    }
  }
};
</script>

<style scoped></style>
