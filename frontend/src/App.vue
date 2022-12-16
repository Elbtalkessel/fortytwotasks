<script setup>
import {ref, onMounted} from "vue";
const status = ref(null);
onMounted(async () => {
  const response = await fetch("/health");
  status.value = response.status;
});
</script>

<template>
  <div class="flex h-screen items-center justify-center bg-indigo-50">
    <div
      class="rounded-full border p-5 shadow"
      :class="{'bg-gray-500': status === null, 'bg-green-500': status === 200, 'bg-red-500': status !== 200}"
    >
      {{ status }}
    </div>
  </div>
</template>
