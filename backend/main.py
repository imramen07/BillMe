from fastapi import FastAPI
from db import Base, engine
from customers import router as customer_router
from invoices import router as invoice_router
from products import router as product_router
from invoice_items import router as invoice_item_router
from models import Customer

Base.metadata.create_all(bind = engine)
app = FastAPI(title = "ReConnect")
app.include_router(customer_router)
app.include_router(invoice_router)
app.include_router(product_router)
app.include_router(invoice_item_router)
@app.get("/")
def root():
    return {"status": "running"}