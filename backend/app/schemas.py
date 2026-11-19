
from datetime import date
from pydantic import BaseModel, Field


# Used when creating a new expense
class ExpenseCreate(BaseModel):
    title: str = Field(min_length=2)
    amount: float = Field(gt=0)
    category: str
    expense_date: date


# Used when updating an existing expense
class ExpenseUpdate(BaseModel):
    title: str = Field(min_length=2)
    amount: float = Field(gt=0)
    category: str
    expense_date: date
