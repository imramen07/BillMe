from sqlalchemy import Column, Integer, String
from db import Base

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, nullable = False)
    phone = Column(String, nullable = False)

class Invoice(Base):
    __tablename__ = "invoices"
    id = Column(Integer, primary_key = True)
    customer_id = Column(Integer)
    total_amount = Column(Integer)
    created_at = Column(String)

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, nullable=False)
    category = Column(String)
    price = Column(Integer)
    stock = Column(Integer)

class InvoiceItem(Base):
    __tablename__ = "invoice_items"
    id = Column(Integer, primary_key = True, index = True)
    invoice_id = Column(Integer)
    product_id = Column(Integer)
    quantity = Column(Integer)
    unit_price = Column(Integer)