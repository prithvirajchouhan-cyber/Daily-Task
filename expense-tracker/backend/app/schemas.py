from datetime import date
from pydantic import BaseModel, Field


# Registration schema
class UserRegister(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=8)


# Login schema
class UserLogin(BaseModel):
    username: str
    password: str


# Refresh token schema
class RefreshRequest(BaseModel):
    refresh_token: str


# Token response schema
class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


# Expense creation schema
class ExpenseCreate(BaseModel):
    title: str = Field(min_length=2)
    amount: float = Field(gt=0)
    category: str
    expense_date: date


# Expense update schema
class ExpenseUpdate(BaseModel):
    title: str = Field(min_length=2)
    amount: float = Field(gt=0)
    category: str
    expense_date: date