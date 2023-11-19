from fastapi import FastAPI, HTTPException
from fastapi.params import Depends
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL
from datetime import datetime
from sqlalchemy.orm import Session
from pydantic import BaseModel

SQLALCHEMY_DATABASE_URL = "postgresql://myuser:mypassword@database/mydatabase"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

app = FastAPI()

class CustomerDB(Base):
    __tablename__ = "customers"
    customer_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String)
    address = Column(String)
    phone_number = Column(String)

class Customer(BaseModel):
    customer_id: int
    first_name: str
    last_name: str
    email: str
    address: str
    phone_number: str


class Book(Base):
    __tablename__ = "books"
    book_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author_first_name = Column(String, index=True)
    author_last_name = Column(String, index=True)
    genre = Column(String)
    publication_year = Column(Integer)
    price = Column(Float)

class Order(Base):
    __tablename__ = "orders"
    order_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"))
    order_date = Column(Date)
    total_amount = Column(Float)
    book_id = Column(Integer, ForeignKey("books.book_id"))
    quantity = Column(Integer)
    price = Column(Float)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/customers/")
def create_customer(customer: Customer, db: Session = Depends(get_db)):
    db.add(customer)
    db.commit()
    db.refresh(customer)
    return customer

# @app.post("/books/")
# def create_book(book: Book, db: Session = Depends(get_db)):
#     db.add(book)
#     db.commit()
#     db.refresh(book)
#     return book

# @app.post("/orders/")
# def create_order(order: Order, db: Session = Depends(get_db)):
#     db.add(order)
#     db.commit()
#     db.refresh(order)
#     return order

@app.get("/hello")
def read_root():
    return {"message": "Hello, World!!!!"}

@app.get("/menu")
def read_root():
    return {"message": "Check the MENU"}

@app.get("/exit")
def read_root():
    return {"message": "byee"}