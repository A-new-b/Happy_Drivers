<template>
  <v-snackbar :value="showmessage" :top="1 === 1" :color="type">
    {{ message }}
    <v-btn dark text @click="close()">
      <v-icon>close</v-icon>
    </v-btn>
  </v-snackbar>
</template>

<script>
export default {
  name: "notification",
  created() {},
  computed: {
    type() {
      return this.$store.state.type;
    },
    showmessage() {
      return this.$store.state.showmessage;
    },
    message() {
      let { message } = this.$store.state;
      if (message.length > 25) {
        message = `${message.substring(0, 25)}..`;
      }
      return message;
    }
  },
  methods: {
    close() {
      this.$store.commit("removeAlert");
    }
  }
};
</script>

<style scoped></style>
