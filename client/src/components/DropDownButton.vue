<template>
   <div class="relative inline-block">
       <div>
           <button @click="isOpen = !isOpen" type="button" class="inline-flex justify-center w-full rounded-md hover:bg-cyan-200 hover:text-slate-600 text-neutral-200 p-2 mr-4" id="menu-button" aria-expanded="true" aria-haspopup="true">
               Dropdown
               <svg class="self-center -mr-1 ml-2 h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                   <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" />
               </svg>
           </button>
           <div class="origin-top-right py-2 absolute right-0 bg-white w-56 shadow-lg rounded-md mt-2" :class="{hidden: !isOpen}">
               <a class="p-2 block hover:bg-gray-100" href="#about">About</a>
               <a class="p-2 block hover:bg-gray-100" href="#contact">Contact</a>
           </div>
       </div>
   </div>
</template>

<script setup>
    import {ref} from "vue";

    defineProps({
                    title: String,
                });
    const isOpen = ref(false);

</script>

<style scoped>

</style>
