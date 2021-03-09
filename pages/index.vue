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
      <label class="custom-file" for="file">
        {{
          files.length ? `(${files.length}) files are selected` : "Choose files"
        }}
        <input
          @change="handleSelectedFiles"
          id="file"
          multiple
          name="file"
          ref="fileInput"
          type="file"
        />
      </label>

      <!--Show Selected Files-->
      <div class="large-12 medium-12 small-12 cell">
        <div class="file-listing" v-for="(file, key) in files" :key="key">
          {{ file.name }}
          <span class="remove-file" v-on:click="removeFile(key)">Remove</span>
        </div>
      </div>

      <!--Submit Button && Progress Bar-->
      <div>
        <button @click="upload">Start Upload</button>
        - Upload progress : {{ this.progress }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "index",

  data() {
    return {
      lang: null,
      files: [],
      progress: 0,
    };
  },

  computed: {
    /*The FormData : Here We Make A Form With Images Data To Submit.*/
    form() {
      let form = new FormData();

      this.files.forEach((file, index) => {
        form.append("files[" + index + "]", file);
      });

      return form;
    },
  },

  methods: {
    setLang(lang) {
      this.lang = lang;
    },

    handleSelectedFiles() {
      let selectedFiles = this.$refs.fileInput.files;

      for (let i = 0; i < selectedFiles.length; i++) {
        /*Check Already Has Been Selected Or Not ...*/
        let isFileExists = this.files.find(
          (file) =>
            file.type === selectedFiles[i].type &&
            file.name === selectedFiles[i].name &&
            file.size === selectedFiles[i].size &&
            file.lastModified === selectedFiles[i].lastModified
        );

        if (!isFileExists) this.files.push(selectedFiles[i]);
      }
    },
    removeFile(key) {
      this.files.splice(key, 1);
    },
    upload() {
      const config = {
        onUploadProgress: (progressEvent) =>
          (this.progress = Math.round(
            (progressEvent.loaded * 100) / progressEvent.total
          )),
      };

      this.$axios
        .post("host-url/upload-image", this.form, config)
        .then((res) => {
          this.progress = 0;
          this.files = [];

          console.log(res);
        })
        .catch((err) => console.log(err));
    },
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
.custom-file {
  padding: 1.2rem;
  border-radius: 0.8rem;
  display: inline-block;
  border: 2px dashed #a0a0a0;
}

.custom-file input {
  display: none;
}
</style>
