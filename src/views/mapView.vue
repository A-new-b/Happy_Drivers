<template>
  <div>
    <v-container fluid>
      <Table :ifSelect="true"></Table>
    </v-container>
  </div>
</template>

<script>
import Table from "../components/table";
export default {
  name: "Map",
  components: { Table }
};
</script>

<style scoped></style>
