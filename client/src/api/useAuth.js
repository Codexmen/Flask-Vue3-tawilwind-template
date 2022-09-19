import {ref, watch} from "vue";
import useApi from "@/api/useApi";
const isAuthenticated = ref(false)
export default function useAuth() {
    const {post, fetchData, isLoading, error, data} = useApi();
    function login(login, password) {
            post('auth/login',{login, password});
            watch(data, () => {
              isAuthenticated.value = data.value.isAuthenticated
            })
    }
    function getUserInfo() {
        fetchData('auth/me')
    }
    function logout() {
         post('auth/logout');
    }
    return {login, isLoading, error, data, getUserInfo}
}