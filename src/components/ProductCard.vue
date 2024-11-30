<template>
    <div class="product-card">
      <h3>{{ product.name }}</h3>
      <p>{{ truncatedDescription }}</p>
      <p style="font-weight: bold">Цена: {{ product.price }} ₽</p>
      <p v-if="product.in_stock">В наличии</p>
      <p v-else>Нет в наличии</p>
    </div>
  </template>
  
<script>
export default {
    props: {
      product: {
        type: Object,
        required: true,
      },
    },
    computed: {
        // Обрезаем описание если оно  больше 100 символов
        truncatedDescription() {
        if (this.product.description && this.product.description.length > 100) {
            return this.product.description.slice(0, 100) + '...';
        }
        return this.product.description;
        },
    },
};
</script>
  
<style scoped>
    .product-card {
        width: 200px;
        margin: 10px;
        padding: 20px;
        background-color: var(--primary-color);
        border-radius: 8px;
        border: 1px solid var(--secondary-color);
        box-shadow: 5px 5px 0px 0px rgb(0 0 0);
    }
    
    .product-card h3 {
        margin: 0 0 10px;
        font-size: 18px;
    }
    
    .product-card p {
        margin: 5px 0;
    }
</style>
  