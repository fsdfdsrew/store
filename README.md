# Бэкенд инструкция

**Описание**

В проекте разделены фронтенд (Vue.js) и бэкенд (FastAPI)

**Шаг 1: Установка Python и зависимостей**

Для работы с бэкендом необходимо установить Python и pip (если они ещё не установлены).

Перейдите в директорию бэкенда:
```sh
cd путь/к/проекту/backend
```

Создайте виртуальное окружение:
```sh
python -m venv venv
```

Активируйте виртуальное окружение:
```sh
venv\Scripts\activate
```

Установите зависимости с помощью pip:
- Если у вас есть файл requirements.txt, выполните:
```sh
pip install -r requirements.txt
```

- Если файла requirements.txt нет, установите необходимые зависимости вручную:
```sh
pip install fastapi uvicorn sqlalchemy psycopg2 alembic pydantic
```

**Шаг 2: Настройка базы данных PostgreSQL**

Убедитесь, что PostgreSQL установлен и запущен.

Создайте базу данных с именем, указанным в database.py (store_db)

```sh
CREATE DATABASE store_db;
```

**Шаг 3: Запуск бэкенда**

Для запуска FastAPI сервера выполните:
```sh
uvicorn main:app --reload
```
Сервер будет запущен по адресу http://127.0.0.1:8000

Для ознакомления с документацией, перейдите по адресу http://127.0.0.1:8000/docs#/

![screen4](https://github.com/user-attachments/assets/6264f467-3fed-45f7-a47d-c9c8de9d5489)

![screen5](https://github.com/user-attachments/assets/902f6115-b819-4e07-b43f-7013e3b74c5f)
