from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Строка подключения к базе данных PostgreSQL
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/store_db"

# Создание подключения к базе данных
engine = create_engine(DATABASE_URL)

# SessionLocal для создания сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для всех моделей
Base = declarative_base()

# Зависимость для получения сессии в эндпоинтах
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()