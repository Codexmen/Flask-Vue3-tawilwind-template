<script setup>
import { ref, onMounted } from 'vue'
import useAuth from "@/api/useAuth";
const { isAuthenticated, logout } = useAuth();

</script>

<template>
  <div>
    <header class="bg-white shadow" v-if="$route.meta.title">
      <div class="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">
        <h1
          class="text-3xl font-bold leading-tight text-gray-900"
        >
          {{ $route.meta.title }}
        </h1>
        <span v-if="isAuthenticated" @click="logout()">Logout</span>
      </div>
    </header>
    <main>
      <router-view />
    </main>
  </div>
</template>
