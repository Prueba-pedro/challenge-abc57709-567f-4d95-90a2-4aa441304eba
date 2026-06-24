class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, index=True)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String, index=True)

Base.metadata.create_all(bind=engine)