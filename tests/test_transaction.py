import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app, get_db
from app.models.transaction import Base, Transaction
from app.schemas.transaction import TransactionCreate, TransactionResponse
from app.crud.transaction import create_transaction, get_transaction, update_transaction, delete_transaction
from fastapi.testclient import TestClient

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_transaction():
    transaction = TransactionCreate(amount=100.0, status="pending")
    response = client.post("/transactions/", json=transaction.dict())
    assert response.status_code == 200
    assert response.json() == {"id": 1, "amount": 100.0, "date": response.json().get("date"), "status": "pending"}

def test_get_transaction():
    response = client.get("/transactions/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "amount": 100.0, "date": response.json().get("date"), "status": "pending"}

def test_update_transaction():
    transaction = TransactionUpdate(status="completed")
    response = client.put("/transactions/1", json=transaction.dict())
    assert response.status_code == 200
    assert response.json() == {"id": 1, "amount": 100.0, "date": response.json().get("date"), "status": "completed"}

def test_delete_transaction():
    response = client.delete("/transactions/1")
    assert response.status_code == 200
    assert response.json() == {"detail": "Transaction deleted"}