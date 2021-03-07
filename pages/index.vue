<template>
  <div>
    <h1 class="text-center text-5xl font-bold text-gray-800 font-mono">
      Select Language
    </h1>
    <div class="mt-6 flex flex-row justify-center">
      <button class="btn btn-green">English</button>
      <button class="btn btn-green mx-8">Urdu</button>
      <button class="btn btn-green">Numeric</button>
    </div>
  </div>
</template>

<script>
export default {}
</script>

<style lang="postcss">
.btn {
  @apply py-2 px-4 font-semibold rounded-lg shadow-md;
}
.btn-green {
  @apply text-white bg-green-500 hover:bg-green-700;
} </style>