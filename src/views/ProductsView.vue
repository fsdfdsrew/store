<template>
    <div class="product-page-container">
        <h1>CLOTHES</h1>

        <!-- Кнопка для добавления нового товара -->
        <button @click="showModal = true" class="add-btn">Добавить товар</button>
  
        <!-- Поле для поиска по названию -->
        <input
            v-model="searchTerm"
            @input="fetchProducts"
            type="text"
            placeholder="Поиск по названию"
            class="search-input"
        />
    
        <div v-if="loading">Загрузка...</div>
        <div v-if="error" class="error">{{error}}</div>
    
        <!-- Список товаров -->
        <div class="product-list">
            <ProductCard
                v-for="product in products"
                :key="product.id"
                :product="product"
            />
        </div>

        <!-- Модальное окно для добавления товара -->
        <AddProductModal
            v-if="showModal"
            :onSuccess="fetchProducts"
            @close="showModal = false"
        />
    </div>
</template>
  
<script>
import axios from 'axios';
import ProductCard from '@/components/ProductCard.vue';
import AddProductModal from '@/components/AddProductModal.vue';
  
  export default {
    data() {
      return {
        products: [],
        searchTerm: '',
        loading: false,
        error: null,
        showModal: false,
      };
    },
    components: {
        ProductCard,
        AddProductModal,
    },
    methods: {
      // Функция для получения списка товаров (с фильтрацией по имени)
      async fetchProducts() {
        this.loading = true;
        this.error = null;

        try {
          const params = {};
  
          // Добавляем филтр поиска, если он не пустой
          if (this.searchTerm) {
            params.name = this.searchTerm;
          }

          const response = await axios.get('http://127.0.0.1:8000/products', { params });

          this.products = response.data;
        } catch (error) {
          this.error = 'Не удалось загрузить товары';
        } finally {
          this.loading = false;
        }
      },
    },
    created() {
      this.fetchProducts();
    },
  };
</script>
  

<style scoped>
    .product-page-container {
        padding: 30px;

        h1 {
            font-weight: 200;
        }
    }

    .product-list {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
    }

    .add-btn {
        position: fixed;
        right: 10px;
        bottom: 10px;
    }
</style>