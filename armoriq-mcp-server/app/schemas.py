from pydantic import BaseModel

class AccountCreate(BaseModel):
    name: str

class Amount(BaseModel):
    amount: float
