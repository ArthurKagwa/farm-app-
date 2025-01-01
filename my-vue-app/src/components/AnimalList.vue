<template>
  <div>
    <h1>Animal List</h1>
    <ul>
      <li v-for="animal in animals" :key="animal.animal_no">
        {{ animal.animal_no }} - {{ animal.breed }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      animals: [],
    };
  },
  mounted() {
    this.fetchAnimals();
  },
  methods: {
    async fetchAnimals() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/animals/');
        this.animals = response.data;
      } catch (error) {
        console.error("Error fetching animals:", error);
      }
    },
  },
};
</script>
