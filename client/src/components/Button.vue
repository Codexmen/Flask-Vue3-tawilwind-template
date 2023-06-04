<script setup>
const props = defineProps({
  title: {
    type: String,
    required: true,
  },
  link: {
    type: String,
    default: null,
  },
  theme: {
    type: String,
    default: 'secondary',
  },
  size: {
    type: String,
    default: 'md',
  },
  })
const commonClasses = 'shadow inline-flex items-center justify-center border border-transparent rounded-md font-semibold focus:outline-none focus:shadow-outline transition duration-150 ease-in-out'
const themeClasses = {
  primary: 'bg-indigo-600 hover:bg-indigo-500 text-white',
  secondary: 'bg-white hover:bg-gray-100 text-gray-800',
  negative: 'bg-red-600 hover:bg-red-500 text-white',
  transparent: 'bg-transparent hover:bg-gray-100 text-gray-800',
}
const sizes = {
  sm: 'px-3 py-2 text-sm leading-4',
  md: 'px-4 py-2 text-base leading-5',
  lg: 'px-6 py-3 text-lg leading-6',
}
</script>
<template>
    <button type="button" :class="`${commonClasses} ${themeClasses[props.theme]} ${sizes[props.size]}`">{{props.title}}</button>
</template>

