@app.post("/transactions/", response_model=TransactionResponse)
def create_transaction_endpoint(transaction: TransactionCreate, db: Session = Depends(get_db)):
    return create_transaction(db, transaction)

@app.get("/transactions/{transaction_id}", response_model=TransactionResponse)
def get_transaction_endpoint(transaction_id: int, db: Session = Depends(get_db)):
    transaction = get_transaction(db, transaction_id)
    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction

@app.put("/transactions/{transaction_id}", response_model=TransactionResponse)
def update_transaction_endpoint(transaction_id: int, transaction: TransactionUpdate, db: Session = Depends(get_db)):
    return update_transaction(db, transaction_id, transaction)

@app.delete("/transactions/{transaction_id}")
def delete_transaction_endpoint(transaction_id: int, db: Session = Depends(get_db)):
    delete_transaction(db, transaction_id)
    return {"detail": "Transaction deleted"}