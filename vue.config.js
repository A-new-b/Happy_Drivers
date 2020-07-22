module.exports = {
  transpileDependencies: ["vuetify"],
  devServer: {
    // development server port 8000
    port: 8080,
    proxy: {
      "/api": {
        target: "http://49.234.219.43:800",
        ws: false,
        secure: false,
        changeOrigin: true
      }
    },
    disableHostCheck: true
  }
};
