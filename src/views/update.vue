<template>
  <v-container fluid>
    <v-row>
      <v-col>
        <uploader
          ref="uploader"
          :options="uploadConf.options"
          :auto-start="uploadConf.autoStart"
          :file-status-text="uploadConf.fileStatusText"
          @file-success="onFileSuccess"
        >
          <uploader-unsupport></uploader-unsupport>
          <uploader-drop :attrs="uploadConf.attrs">
            <p style="color: gray">
              图片信息：拖拽文件至此处上传&nbsp;&nbsp;或&nbsp;&nbsp;

              <uploader-btn :attrs="uploadConf.attrs"
                >选择文件上传</uploader-btn
              >
            </p>
          </uploader-drop>
          <uploader-list></uploader-list>
        </uploader>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { uploadConf } from "../utils";
import { notify } from "../components/notification";

export default {
  name: "update",
  data: () => ({
    uploadConf
  }),
  methods: {
    onFileSuccess(rootFile, file, response) {
      const resData = JSON.parse(response);
      console.log(response);
      if (resData.message === "success") {
        // this.uploadFile += resData.filepath.replace("|", "") + "|";
        this.uploadFile = resData.url;
        notify("success", "文件上传成功！");
      } else {
        notify("error", "文件上传失败！");
      }
    }
  }
};
</script>

<style scoped></style>
