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
        <img :src="img.image" alt="картинка" width="150" />
        <p>{{ img.description }}</p>
        <button @click="deleteImage(img.id)">Удалить</button>
      </div>
    </div>
  </div>
</template>

<script>
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
      await fetch('http://localhost:8000/api/images/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          image: this.file,
          description: this.description
        })
      })
      this.description = ''
      this.file = null
      this.fetchImages()
    },
    async fetchImages() {
      const res = await fetch('http://localhost:8000/api/images/')
      this.images = await res.json()
    },
    async deleteImage(id) {
      await fetch(`http://localhost:8000/api/images/${id}/`, {
        method: 'DELETE'
      })
      this.fetchImages()
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
