<script setup>
import {ref} from 'vue'
import CloseIcon from "@/components/icons/CloseIcon.vue";
import HamburgerMenuIcon from "@/components/icons/HamburgerMenuIcon.vue";
import DropDownButton from "@/components/DropDownButton.vue";

const isOpen = ref(false);

</script>
<template>
    <header class="p-4 shadow-md">
        <div class="container px-4 mx-auto flex justify-center items-center">
            <div class="block sm:hidden mr-auto" >
                <HamburgerMenuIcon class="text-white" @click="isOpen = true" />
                <nav v-if="isOpen" class="w-full h-full fixed p-8 bg-white top-0 left-0 flex flex-col">
                    <a class="py-2" href="#about">About</a>
                    <a class="py-2" href="#contact">Contact</a>
                    <CloseIcon class="absolute top-2 right-2 cursor-pointer" @click="isOpen = false" />
                </nav>
            </div>
            <a class="text-gray-800 font-bold text-2xl hover:underline cursor-pointer" href="/">Logo</a>
            <nav class="ml-auto hidden sm:flex ">
                <DropDownButton class="mr-4" title="Drowdown props" />
                <a class="p-2 mr-4 hover:bg-cyan-200 hover:text-slate-600 text-gray-800 rounded-md" href="#about">About</a>
                <a class="p-2 mr-4 hover:bg-cyan-200 hover:text-slate-600 text-gray-800 rounded-md" href="/irregular-verbs">Irregular verbs</a>
                <router-link class="p-2 hover:underline hover:text-slate-600 text-gray-800 rounded-md" to="/contacts">Contact</router-link>
            </nav>
            <div class="ml-auto sm:ml-0">
                <router-link to="/login" class="p-2 hover:bg-blue-400 text-gray-800 cursor-pointer hover:text-slate-600 rounded-md">Login</router-link>
            </div>
        </div>

    </header>
</template>
