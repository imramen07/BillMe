from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from models import Product

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.post("/")
def create_product(
    name: str,
    category: str,
    price: int,
    stock: int,
    db: Session = Depends(get_db)
):
    product = Product(
        name = name,
        category = category,
        price = price,
        stock = stock
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

@router.get("/")
def get_products(
    db: Session = Depends(get_db)
):
    return db.query(Product).all()