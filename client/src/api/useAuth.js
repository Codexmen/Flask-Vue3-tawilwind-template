import { ref } from "vue";
import useApi from "@/api/useApi";
import { useRouter } from "vue-router";

const isAuthenticated = ref(JSON.parse(localStorage.getItem("isLogin")));

export default function useAuth() {
  const { post, fetchData, isLoading, error, data } = useApi();
  const router = useRouter();

  async function login(login, password) {
    const loginInfo = await post("auth/login", { login, password });

    isAuthenticated.value = loginInfo.isAuthenticated;
    if (loginInfo.isAuthenticated) {
      localStorage.setItem("isLogin", JSON.stringify(true));
      router.push({ name: "Dashboard" });
    }
  }
  function getUserInfo() {
    fetchData("auth/me");
  }
  function logout() {
    post("auth/logout");
    isAuthenticated.value = false;
    localStorage.setItem("isLogin", JSON.stringify(false));
    router.push({ name: "Login" });
  }
  return {
    login,
    isLoading,
    error,
    data,
    getUserInfo,
    logout,
    isAuthenticated,
  };
}
