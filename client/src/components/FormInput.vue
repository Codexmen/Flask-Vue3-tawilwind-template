<template xmlns="http://www.w3.org/1999/html">
  <div>
    <label
      class="block text-sm font-medium text-gray-700"
      :for="name" v-if="label">{{label}}</label>
    <input :type="type" @change="$emit('update:modelValue', $event.target.value)" type="text" :name="name" :placeholder="placeholder" :value="modelValue" :class="inputClasses" />
      <slot></slot>
  </div>
</template>

<script>
export default {
  name: "FormInput",
  props: {
    name: {
      type: String,
      required: true,
    },
    label: {
      type: String,
      required: true,
    },
    placeholder: {
      type: String,
      default: null,
    },
    modelValue: {
      type: String,
      default: null,
    },
    type: {
      type: String,
      default: 'text',
    },
  },
  setup() {
    const inputClasses = 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50'
    return {
      inputClasses,
    }
  },
}
</script>
