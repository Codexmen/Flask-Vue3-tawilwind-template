import {reactive, ref} from 'vue';
export default function useApi() {
    const data = ref(null);
    async function getInfo() {
        const result = await fetch('http://127.0.0.1:5000/api/ping/', {method: 'POST',
    mode: 'cors',}).then((response) => response.json())
        console.log(result)
        data.value = result.data
    }
    return {
        data,
        getInfo
    }
}