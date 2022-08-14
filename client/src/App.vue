<script setup>
import { ref, onMounted } from 'vue'
import useApi from '@/api/useApi';
let counter = ref(0)
const {data,
        getInfo} = useApi();
onMounted(() => getInfo())
</script>

<template>
  <div>
    <header class="bg-white shadow" v-if="$route.meta.title">
      <div class="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">
        <h1
          @click="counter = 0"
          class="text-3xl font-bold leading-tight text-gray-900"
        >
          {{ data }}
        </h1>
      </div>
    </header>
    <main>
      <router-view />
    </main>
  </div>
</template>
