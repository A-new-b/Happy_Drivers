<template>
  <v-container fluid>
    <v-row align="center">
      <v-col class="d-flex" cols="12" sm="4">
        <v-select :items="search_method" label="搜索方式" outlined></v-select>
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
        <p>
          耗时：
        </p>
      </v-col>
    </v-row>
    <Table :desserts="desserts"></Table>
  </v-container>
</template>

<script>
import Table from "../components/table";
export default {
  name: "search",
  components: {
    Table
  },
  data: () => ({
    desserts: [],
    search_method: [],
    search: ""
  }),
  created() {
    this.search_init();
  },
  methods: {
    search_init() {
      this.search_method = ["折半查询"];
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
