<template>
  <div>
    <h1 class="text-center text-5xl font-bold text-gray-800 font-mono">
      Select Language
    </h1>
    <div class="mt-6 flex flex-row justify-center">
      <button @click="setLang('eng')" class="btn btn-green">English</button>
      <button @click="setLang('urdu')" class="btn btn-green mx-8">Urdu</button>
      <button @click="setLang('num')" class="btn btn-green">Numeric</button>
    </div>
    <div class="file-uploader mt-6 flex flex-row justify-center" v-if="lang">
      <dashboard :uppy="uppy" />
    </div>
  </div>
</template>

<script>
import { Dashboard } from "@uppy/vue";

import "@uppy/core/dist/style.css";
import "@uppy/dashboard/dist/style.css";

import Uppy from "@uppy/core";
export default {
  name: "index",
  components: {
    Dashboard,
  },

  data() {
    return {
      lang: null,
    };
  },
  
  computed: {
    uppy: () => new Uppy(),
  },

  methods: {
    setLang(lang) {
      this.lang = lang;
    },
  },

  beforeDestroy() {
    this.uppy.close();
  },
};
</script>

<style lang="postcss">
.btn {
  @apply py-2 px-4 font-semibold rounded-lg shadow-md;
}
.btn-green {
  @apply text-white bg-green-500 hover:bg-green-700;
}
</style>