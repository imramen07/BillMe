#BillMe

---

BillMe is a lightweight retail billing backend build with FastAPI and SQLAlchemy. It provides APIs for managing customers, products and invoices.

---

##Features

---

- Customer Management
	- Create customers
	- View customer list
	- Retrieve customer details
	- Delete customers
- Product Management
	- Create product
	- View product
- Invoice Management
	- Create invoices
	- View invoices
	- Retrieve invoice details
- Invoice Item Management
	- Add products to invoices
	- Store quantity and pricing info

---

##Tech Stack

---

- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn

---

##Project Tree

---

│   README.md
│   requirements.txt
│
└───backend
        customers.py
        db.py
        invoices.py
        invoice_items.py
        main.py
        models.py
        products.py

---

##Design

---

###Customer
Stores customer information (name, contact info, customer-id)

###Product
Stores product details (name, proce, categor, stock)

###Invoice
Representation of the bill

###Invoice Item
Represents products included in an invoice

##Flow
Customer	->	Invoice		->	InvoiceItem	->	Product

---

##API Endpoints

---

###Customers
- POST /customers/
- GET /customers/
- GET /customers/{customer_id}
- DELETE /customers/{customer_id}

###Products
- POST /products/
- GET /products/

###Invoices
- POST /invoices/
- GET /invoices/
- GET /invoices/{invoice_id}

###Invoice Items
- POST /invoice-items/
- GET /invoice-items/

---

##Running the project

---

Installation:
```bash
git clone https://github.com/imramen07/BillMe.git
cd BillMe
pip install -r requirements.txt
```

Start server:
```bash
uvicorn main:app --reload
```

Open Swagger UI:
http://127.0.0.1:8000/docs

---

##Future Improvements

---

- Authentication and authorization
- PDF invoice generation
- Inventory and stock checking
- Good frontend (hopefully)

---

This project was built as a medium to learn backend, REST APIs, database modelling and workflow using FastAPI

---

Author - Ramen
Github - imramen07