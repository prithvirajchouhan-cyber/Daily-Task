
from fastapi import APIRouter, HTTPException, status

from app import models
from app.schemas import ExpenseCreate, ExpenseUpdate

router = APIRouter(
    prefix="/api/v1/expenses",
    tags=["Expenses"]
)


# 1. CREATE - Add a new expense
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_expense(expense: ExpenseCreate):

    new_id = models.next_id

    new_expense = expense.model_dump(mode="json")
    new_expense["id"] = new_id

    models.expenses[new_id] = new_expense
    models.next_id += 1

    return {
        "message": "Expense created successfully",
        "data": new_expense
    }


# 2. READ - Get all expenses
@router.get("/")
def get_all_expenses():

    return {
        "message": "All expenses",
        "data": list(models.expenses.values())
    }


# 3. READ - Get one expense by ID
@router.get("/{expense_id}")
def get_expense(expense_id: int):

    if expense_id not in models.expenses:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    return {
        "message": "Expense found",
        "data": models.expenses[expense_id]
    }


# 4. UPDATE - Update an existing expense
@router.put("/{expense_id}")
def update_expense(expense_id: int, expense: ExpenseUpdate):

    if expense_id not in models.expenses:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    updated_expense = expense.model_dump(mode="json")
    updated_expense["id"] = expense_id

    models.expenses[expense_id] = updated_expense

    return {
        "message": "Expense updated successfully",
        "data": updated_expense
    }


# 5. DELETE - Delete an expense
@router.delete("/{expense_id}")
def delete_expense(expense_id: int):

    if expense_id not in models.expenses:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    del models.expenses[expense_id]

    return {
        "message": "Expense deleted successfully"
    }
