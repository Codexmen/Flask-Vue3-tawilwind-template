<template>
  <span :class="sizeClasses"><slot></slot></span>
</template>

<script>
export default {
  name: "Text",
  props: {
    size: {
      type: String,
      default: 'md',
    },
  },
  setup(props) {
    const sizes = {
      sm: 'text-sm',
      md: 'text-base',
      lg: 'text-lg',
    }
    return {
      sizeClasses: sizes[props.size],
    }
  }
}
</script>

<style scoped>

</style>