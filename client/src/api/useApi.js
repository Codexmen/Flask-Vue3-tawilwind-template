import {reactive, ref} from 'vue';
    const PORT = 5000;
    const BASE_URL = 'http://127.0.0.1';
    const API_PATH = '/api/';

    function buildUrl(url) {
        return `${BASE_URL}:${PORT}${API_PATH}${url}`
    }
export default function useApi() {
    const data = ref(null)
    const error = ref(null)
    const isLoading = ref(false)

    async function fetchData(url) {
       isLoading.value = true;
       return fetch(buildUrl(url), {mode: 'cors', credentials: 'include'})
      .then((res) => res.json())
      .then((json) => (data.value = json))
      .catch((err) => (error.value = err))
      .finally(() => isLoading.value = false)
    }
    async function post(url, data) {
       isLoading.value = true;
       fetch(buildUrl(url), {mode: 'cors', credentials: 'include', method: 'POST', body: JSON.stringify(data), headers: {
      'Content-Type': 'application/json'
    }, })
      .then((res) => res.json())
      .then((json) => {
          console.log(json); data.value = json})
      .catch((err) => (error.value = err.message))
      .finally(() => isLoading.value = false)
    }
    return {
        data,
        error,
        isLoading,
        fetchData,
        post
    }
}