from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from models import InvoiceItem, Invoice

router = APIRouter(
    prefix = "/invoice-items",
    tags = ["Invoice Items"]
)

@router.post("/")
def create_invoice_item(
    invoice_id: int,
    product_id: int,
    quantity: int,
    unit_price: int,
    db: Session = Depends(get_db)
):
    item = InvoiceItem(
        invoice_id = invoice_id,
        product_id = product_id,
        quantity = quantity,
        unit_price = unit_price
    )
    db.add(item)
    db.commit()
    db.refresh(item)
    items = db.query(InvoiceItem).filter(
        InvoiceItem.invoice_id == invoice_id
    ).all()
    total = sum(
        i.quantity * i.unit_price
        for i in items
    )
    invoice = db.query(Invoice).filter(
        Invoice.id == invoice_id
    ).first()
    invoice.total_amount = total
    db.commit()
    return item

@router.get("/")
def get_invoice_items(
    db: Session = Depends(get_db)
):
    return db.query(InvoiceItem).all()