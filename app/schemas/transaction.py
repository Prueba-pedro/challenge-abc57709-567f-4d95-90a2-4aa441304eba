class TransactionCreate(BaseModel):
    amount: float
    status: str

class TransactionUpdate(BaseModel):
    amount: float = None
    status: str = None

class TransactionResponse(BaseModel):
    id: int
    amount: float
    date: datetime.datetime
    status: str