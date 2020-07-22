export var uploadConf = {
  options: {
    target: "/api/update", // 目标上传 URL
    testChunks: false,
    parseTimeRemaining: function(timeRemaining, parsedTimeRemaining) {
      return parsedTimeRemaining
        .replace(/\syears?/, "年")
        .replace(/\days?/, "天")
        .replace(/\shours?/, "小时")
        .replace(/\sminutes?/, "分钟")
        .replace(/\sseconds?/, "秒");
    }
  },
  attrs: {
    accept: ".dat"
  },
  fileStatusText(status, response) {
    const statusTextMap = {
      success: "上传成功",
      error: "上传失败",
      uploading: "正在上传",
      paused: "暂停",
      waiting: "上传等待中"
    };
    if (response === null) {
      return statusTextMap[status];
    } else {
      if (response.message === "success") {
        return statusTextMap["success"];
      } else {
        return statusTextMap["error"];
      }
    }
  },
  autoStart: false
};
