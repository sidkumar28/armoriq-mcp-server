from sqlalchemy.orm import Session
from . import models

def create_account(db: Session, name: str):
    account = models.Account(name=name)
    db.add(account)
    db.commit()
    db.refresh(account)
    return account

def deposit(db: Session, account_id: int, amount: float):
    account = db.query(models.Account).get(account_id)
    account.balance += amount
    txn = models.Transaction(account_id=account_id, amount=amount, type="deposit")
    db.add(txn)
    db.commit()
    return account

def withdraw(db: Session, account_id: int, amount: float):
    account = db.query(models.Account).get(account_id)
    if account.balance < amount:
        raise Exception("Insufficient balance")
    account.balance -= amount
    txn = models.Transaction(account_id=account_id, amount=amount, type="withdrawal")
    db.add(txn)
    db.commit()
    return account
