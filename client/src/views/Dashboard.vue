<script setup>
import Modal from "@/components/Modal.vue";
</script>

<template>
  <div class="bg-gray-50">
    <div
      class="mx-auto max-w-screen-xl px-4 py-12 sm:px-6 lg:flex lg:items-center lg:justify-between lg:py-16 lg:px-8"
    >
      <h2
        class="text-3xl font-extrabold leading-9 tracking-tight text-gray-900 sm:text-4xl sm:leading-10"
      >
        <span class="text-indigo-600">Dashboard</span>
      </h2>
      <div class="mt-8 flex lg:mt-0 lg:flex-shrink-0">
        Dashboard content
      </div>
    </div>
    <div>
      <Modal show />
    </div>
  </div>
</template>
