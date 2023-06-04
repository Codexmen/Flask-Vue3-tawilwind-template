<script setup>
import ButtonRepo from '@/components/Button.vue'
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";
import Heading from "@/components/Heading.vue";
import Text from "@/components/Text.vue";
import FormInput from "@/components/FormInput.vue";
</script>

<template>
  <Header />
  <div class="bg-gray-50">
    <div
      class="mx-auto max-w-screen-xl px-4 py-12 sm:px-6 lg:flex lg:items-center lg:justify-between lg:py-16 lg:px-8"
    >
      <div class="mt-8 lg:mt-0 lg:flex-shrink-0 flex flex-col gap-2">
        <div class="flex gap-1">
          <ButtonRepo disabled title="Primary" theme="primary" size="lg" />
          <ButtonRepo disabled title="Secondary" theme="secondary" size="lg"/>
          <ButtonRepo disabled title="Negative" theme="negative" size="lg" />
        </div>
        <div class="flex gap-1">
          <ButtonRepo title="Primary" theme="primary" />
          <ButtonRepo title="Secondary" theme="secondary" />
          <ButtonRepo title="Negative" theme="negative" />
        </div>
        <div class="flex gap-1">
          <ButtonRepo title="Primary" theme="primary" size="sm" />
          <ButtonRepo title="Secondary" theme="secondary" size="sm" />
          <ButtonRepo title="Negative" theme="negative" size="sm" />
          <ButtonRepo title="Transparent" theme="transparent" size="sm" />
        </div>
        <div class="flex gap-1">
          <ButtonRepo icon-before="face" title="Primary" theme="primary" size="sm" icon-after="face" />
          <ButtonRepo icon-before="face" title="Primary" theme="primary" size="sm" />
          <ButtonRepo title="Primary" theme="primary" size="sm" icon-after="face" />
          <ButtonRepo theme="primary" size="sm" icon="face" />
          <ButtonRepo theme="primary" size="sm" title="Without icon" />
          </div>
        <div>
          <Heading size="lg">Large heading</Heading>
          <Heading>Medium heading</Heading>
          <Heading size="sm">Small heading</Heading>
        </div>
        <div>
          <p><Text size="lg">Large heading</Text></p>

          <p><Text>Medium heading</Text></p>
          <p><Text size="sm">Small heading</Text></p>
        </div>
        <div>
          <FormInput name="name" placeholder="Enter your name" />
        </div>
        <div>
          <FormInput label="Email" name="name" placeholder="Enter your name" />
        </div>
      </div>
    </div>
  </div>
  <Footer />
</template>
