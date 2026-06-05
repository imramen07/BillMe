from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from models import Customer

router = APIRouter(
    prefix = "/customers",
    tags = ["Customers"]
)
@router.post("/")
def create_customer(
    name: str,
    phone: str,
    db: Session = Depends(get_db)
):
    customer = Customer(
        name = name,
        phone = phone
    )
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer

@router.get("/")
def get_customers(db: Session = Depends(get_db)):
    return db.query(Customer).all()

@router.get("/{customer_id}")
def get_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):
    customer = db.query(Customer).filter(
        Customer.id == customer_id
    ).first()

    if not customer:
        return {"error": "customer not found"}
    return customer

@router.delete("/{customer_id}")
def delete_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):
    customer = db.query(Customer).filter(
        Customer.id == customer_id
    ).first()

    if not customer:
        return {"eror": "customer not found"}
    
    db.delete(customer)
    db.commit()
    return {"message": "customer deleted"}