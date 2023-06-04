import Home from "./views/Home.vue";
import Login from "./views/Login.vue";
import About from "./views/About.vue";
import NotFound from "./views/NotFound.vue";
import Dashboard from "./views/Dashboard.vue";

/** @type {import('vue-router').RouterOptions['routes']} */
export const routes = [
  { path: "/", name: 'Main', component: Home, meta: { title: "Home" } },
  { path: "/login", name: "Login", component: Login, meta: { title: "Login" } },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: Dashboard,
    meta: { title: "Dashboard", authRequired: true },
  },
  {
    path: "/about",
    meta: { title: "About" },
    component: About,
    // example of route level code-splitting
    // this generates a separate chunk (About.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    // component: () => import('./views/About.vue')
  },
  { path: "/:path(.*)", component: NotFound },
];
