<template>
  <h1 class="prose" v-if="size === 'lg'" :class="sizeClasses">
    <slot></slot>
  </h1>
  <h2 class="prose" v-if="size === 'md'"  :class="sizeClasses">
    <slot></slot>
  </h2>
  <h3 class="prose" v-if="size === 'sm'"  :class="sizeClasses">
    <slot></slot>
  </h3>
</template>

<script>
export default {
  name: "Heading",
  props: {
    size: {
      type: String,
      default: 'md',
    },
  },
  setup(props) {
    const sizes = {
      sm: 'text-2xl leading-normal font-bold',
      md: 'text-3xl leading-normal font-bold',
      lg: 'text-4xl leading-normal font-bold',
    }
    return {
      sizeClasses: sizes[props.size],
    }
  }
}
</script>

<style scoped>

</style>