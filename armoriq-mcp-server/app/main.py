from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from . import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="ArmorIQ MCP Banking Server")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/accounts")
def create_account(account: schemas.AccountCreate, db: Session = Depends(get_db)):
    return crud.create_account(db, account.name)

@app.post("/accounts/{account_id}/deposit")
def deposit(account_id: int, amt: schemas.Amount, db: Session = Depends(get_db)):
    return crud.deposit(db, account_id, amt.amount)

@app.post("/accounts/{account_id}/withdraw")
def withdraw(account_id: int, amt: schemas.Amount, db: Session = Depends(get_db)):
    try:
        return crud.withdraw(db, account_id, amt.amount)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/accounts/{account_id}/balance")
def balance(account_id: int, db: Session = Depends(get_db)):
    account = db.query(models.Account).get(account_id)
    return {"balance": account.balance}

@app.get("/accounts/{account_id}/transactions")
def transactions(account_id: int, db: Session = Depends(get_db)):
    return db.query(models.Transaction).filter_by(account_id=account_id).all()
