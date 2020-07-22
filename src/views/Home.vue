<template>
  <div class="home">
    <Table></Table>
  </div>
</template>

<script>
// @ is an alias to /src
import Table from "../components/table";
// import { getData } from "../api/normal/normal";

export default {
  name: "Home",
  components: {
    Table
  },
  data: () => ({}),
  created() {
    this.data_init();
  },
  methods: {
    data_init() {
      // getData()
      //   .then(res => {
      //     if (res.status === 200) {
      //       console.log(JSON.parse(res.data));
      //     }
      //   })
      //   .catch();
    }
  }
};
</script>
