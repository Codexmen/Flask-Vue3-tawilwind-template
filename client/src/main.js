import { createApp } from "vue";
import "./tailwind.css";
import App from "./App.vue";
import { routes } from "./routes.js";
import { createRouter, createWebHistory } from "vue-router";
import useAuth from "@/api/useAuth";
const app = createApp(App);
const { isAuthenticated } = useAuth();
const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach(async (to, from) => {
  console.log(isAuthenticated.value);
  if (!isAuthenticated.value && to.meta.authRequired) {
    return { name: "Login" };
  }

  if (isAuthenticated.value && name === "Login") {
    return { name: to.name };
  }
});

app.use(router);
app.mount("#app");
