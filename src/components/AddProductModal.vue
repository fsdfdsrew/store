<template>
    <div class="modal-overlay">
        <div class="modal">

            <h2>Добавить новый товар</h2>

            <form class="form-group" @submit.prevent="handleSubmit">
                <div>
                    <label for="name">Название:</label>
                    <input id="name" placeholder="Введите название товара" v-model="form.name" required />
                </div>

                <div>
                    <label for="price">Цена:</label>
                    <input id="price" placeholder="Введите цену товара" type="number" v-model="form.price" required />
                </div>

                <div>
                    <label for="description">Описание:</label>
                    <textarea id="description" placeholder="Введите описание товара" v-model="form.description"></textarea>
                </div>

                <div class="availability">
                    <label>В наличии:</label>
                    <input class="checkbox" type="checkbox" v-model="form.in_stock" />
                </div>

                <div class="button-container">
                    <button type="submit">Добавить</button>
                    <button type="button" @click="closeModal">Отмена</button>
                </div>

                <p v-if="error" class="error">{{ error }}</p>
            </form>
        </div>
    </div>
</template>
  
<script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        form: {
          name: '',
          price: null,
          description: '',
          in_stock: true,
        },
        error: null,
      };
    },
    props: {
      onSuccess: {
        type: Function,
        required: true,
      },
    },
    methods: {
        validateForm() {
            // Проверяем, что все обязательные поля заполнены
            if (!this.form.name.trim()) {
                this.error = 'Название не может быть пустым.';
                return false;
            }
            if (this.form.price === null || this.form.price <= 0) {
                this.error = 'Цена должна быть положительным числом.';
                return false;
            }
            return true;
        },
        async handleSubmit() {
            this.error = null;

            // Проверяем форму перед отправкой
            if (!this.validateForm()) {
                return;
            }

            try {
                await axios.post('http://127.0.0.1:8000/products', this.form);
                this.onSuccess(); // Вызываем метод обновления данных
                this.closeModal(); // Закрываем окно
            } catch (error) {
                this.error = 'Не удалось добавить товар. Попробуйте ещё раз.';
            }
        },
        closeModal() {
            this.$emit('close');
            this.resetForm();
        },
        resetForm() {
            this.form = {
                name: '',
                price: null,
                description: '',
                in_stock: true,
            };
            this.error = null;
        },
    },
};
</script>
  
  
<style scoped>
    .modal-overlay {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        color: var(--secondary-color);
        background: rgba(0, 0, 0, 0.5);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 1000;
    }
  
    .modal {
        background: var(--primary-color);
        padding: 20px;
        border-radius: 8px;
        width: 400px;
        box-shadow: 0 0 15px rgba(0, 0, 0, 0.3);
        text-align: start;
    }

    .form-group {
        display: flex;
        flex-direction: column;
        gap: 15px;
    }
    
    .form-group label {
        display: block;
        margin-bottom: 5px;
    }

    .availability {
        display: flex;
        flex-direction: row;
        align-items: center;

        input {
            width: auto;
        }
    }
    
    .button-container {
        display: flex;
        gap: 15px;
    }

    .error {
        padding: 5px 10px;
        border-radius: 50px;
        color: var(--primary-color);
        background-color: var(--secondary-color);
    }

    .checkbox {
        accent-color: var(--secondary-color);
    }
</style>
  