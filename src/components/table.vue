<template>
  <div>
    <v-data-table
      :headers="headers"
      :items="desserts"
      item-key="cx"
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
    >
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>数据表格</v-toolbar-title>
          <v-spacer></v-spacer>
        </v-toolbar>
      </template>
    </v-data-table>
  </div>
</template>

<script>
export default {
  name: "table",
  props: ["desserts"],
  data: () => ({
    headers: [
      { text: "标号", sortable: false, value: "linkId" },
      { text: "岔路数", value: "brunch", sortable: false },
      { text: "分类番号", value: "disPClass", sortable: false },
      { text: "名称", value: "roadName", sortable: false }
    ],
    loading_status: false
  }),
  created() {},
  methods: {}
};
</script>

<style scoped></style>
