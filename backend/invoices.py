from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from models import Invoice

router = APIRouter(
    prefix = "/invoices",
    tags = ["Invoices"]
)
@router.post("/")
def create_invoice(
    customer_id: int,
    total_amount: int,
    db:Session = Depends(get_db)
):
    invoice = Invoice(
        customer_id = customer_id,
        total_amount = total_amount
    )
    db.add(invoice)
    db.commit()
    db.refresh(invoice)
    return invoice
@router.get("/")
def get_invoices(
    db: Session = Depends(get_db)
):
    return db.query(Invoice).all()