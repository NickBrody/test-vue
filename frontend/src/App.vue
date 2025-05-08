<template>
<div class="container max-w-xl mx-auto px-4 py-8">
  <h1 class="text-5xl font-bold text-center text-white mb-8">Загрузка изображения</h1>

    <form @submit.prevent="uploadImage">
      <div class="mb-5">
      <input
      type="text"
      class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
      v-model="description"
      placeholder="Добавить описание"
      required />
      </div>

      <input
      type="file"
      accept="image/*"
      class="file:mr-4 file:rounded-full file:border-0 file:bg-violet-50 file:px-4 file:py-2 file:text-sm file:font-semibold file:text-violet-700 hover:file:bg-violet-100 dark:file:bg-violet-600 dark:file:text-violet-100 dark:hover:file:bg-violet-500 ..."
      @change="onFileChange" required />

      <button
      class="bg-sky-500 hover:bg-sky-700 py-1 px-3 ml-2"
      type="submit">Загрузить</button>
    </form>

    <div v-if="images.length" class="mt-8">
      <h2 class="text-2xl font-semibold text-center mb-4">Загруженные картинки</h2>
      <div
    v-for="img in images"
    :key="img.id"
    class="flex flex-col items-center gap-2 mb-6"
  >
  <img :src="img.image_base64" alt="картинка" class="w-40 rounded shadow" />
  <p class="text-white text-md text-center max-w-xs">{{ img.description }}</p>
  <button
      @click="deleteImage(img.id)"
      class="bg-red-500 hover:bg-red-600 text-white py-1 px-3 rounded"
    >
      Удалить
    </button>
  </div>
    </div>
</div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      file: null,
      description: '',
      images: [],
    }
  },

  mounted() {
    this.fetchImages()
  },

  methods: {
    onFileChange(e) {
      const reader = new FileReader()
      reader.onload = () => {
        this.file = reader.result
      }
      reader.readAsDataURL(e.target.files[0])
    },
    async uploadImage() {
      try {
      await axios.post('http://localhost:8000/api/images/', {
        image_base64: this.file,
        description: this.description
    })
      this.description = ''
      this.file = null
      this.fetchImages()
    } catch (error) {
      console.error('Ошибка при загрузки изображения:', error)
    }
  },

    async fetchImages() {
      try {
        const res = await axios.get('http://localhost:8000/api/images/')
        this.images = res.data
      } catch (error) {
        console.error('Ошибка при получении изображений:', error)
      }
    },

    async deleteImage(id) {
      try {
      await axios.delete(`http://localhost:8000/api/images/${id}/`,)
      this.fetchImages()
    } catch (error) {
        console.error('Ошибка при удалении:', error)
      }
  }
  }
}

</script>

<style>
.container {
  max-width: 500px;
  margin: 0 auto;
  font-family: sans-serif;
}
</style>
