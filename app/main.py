from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routers import products

# Создание таблиц в базе данных (если они ещё не существуют)
Base.metadata.create_all(bind=engine)

# Инициализация приложения FastAPI
app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    #allow_origins=["http://localhost:4173"],  # Разрешённые источники
    allow_origins=["*"], # Разрешаются запросы с любых источников
    allow_credentials=True, # Поддержка куки/авторизации
    allow_methods=["*"],  # Разрешённые HTTP-методы
    allow_headers=["*"],  # Разрешённые заголовки
)

# Подключаем маршруты для работы с товарами
app.include_router(products.router)

@app.get("/")
def read_root():
    return {"message": "Добро пожаловать в FastAPI интернет-магазин!"}