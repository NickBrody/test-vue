<template>
  <div class="container">
    <h1>Image Upload</h1>

    <form @submit.prevent="uploadImage">
      <input type="file" @change="onFileChange" required />
      <input type="text" v-model="description" placeholder="Описание" required />
      <button type="submit">Загрузить</button>
    </form>

    <div v-if="images.length">
      <h2>Загруженные картинки</h2>
      <div v-for="img in images" :key="img.id" style="margin-bottom: 20px">
        <img :src="img.image_base64" alt="картинка" width="150" />
        <p>{{ img.description }}</p>
        <button @click="deleteImage(img.id)">Удалить</button>
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
