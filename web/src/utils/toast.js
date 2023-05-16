import app from "@/app";
const getToast = () => {
  return app.config.globalProperties.$toast;
};
const toast = {
  error: (title, message='', delay=3000) => {
    getToast().add({
      severity: "error",
      summary: title,
      detail: message,
      life: delay,
    });
  },
  warn: (title, message='', delay=3000) => {
    getToast().add({
      severity: "warn",
      summary: title,
      detail: message,
      life: delay,
    });
  },
  success: (title, message='', delay=3000) => {
    getToast().add({
      severity: "success",
      summary: title,
      detail: message,
      life: delay,
    });
  },
  info: (title, message='', delay=3000) => {
    getToast().add({
      severity: "info",
      summary: title,
      detail: message,
      life: delay,
    });
  }
};
export default toast;
