<script setup>
 const footerLinks = [
         {
             sectionTitle: 'Footer feature 1',
             links: [{title: "Footer link 1.1", href: '#'}]
         },
         {
             sectionTitle: 'Footer feature 2',
             links: [{title: "Footer link 2.1", href: '#'}]
         },
         {
             sectionTitle: 'Footer feature 3',
             links: [{title: "Footer link 3.1", href: '#'}]
         },
         {
             links: [{title: "Footer link 4.1", href: '#'}]
         },
     ];
</script>


<template>
    <footer class="bg-slate-600 text-neutral-200 p-4 sm:p-8">
        <div class="container px-4 mx-auto grid md:grid-cols-2 lg:grid-cols-4 gap-4">
            <div v-for="section in footerLinks" :key="section">
                <div v-if="section.sectionTitle" class="text-2xl mb-4">{{ section.sectionTitle }}</div>
                <div>
                    <div v-for="link in section.links">
                        <a class="hover:underline" :href="link.href">{{ link.title }}</a>
                    </div>
                </div>
            </div>
        </div>
    </footer>
</template>
