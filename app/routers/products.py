from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix="/products", tags=["products"])

# Получить список всех товаров или поиск по названию
@router.get("/", response_model=List[schemas.ProductResponse])
def get_products(
    db: Session = Depends(get_db),
    name: Optional[str] = Query(None)  # Параметр не обязателен
):
    query = db.query(models.Product)
    
    # Если name передан, фильтруем товары
    if name:
        query = query.filter(models.Product.name.ilike(f"%{name}%"))
    
    return query.all()
    

# Добавить новый товар
@router.post("/", response_model=schemas.ProductResponse)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    # Проверка на отрицательность `price`
    if product.price < 0:
        raise HTTPException(
            status_code=400,
            detail="Цена не может быть отрицательной."
        )
        
    new_product = models.Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product
