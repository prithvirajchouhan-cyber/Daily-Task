from fastapi import (
    APIRouter,
    HTTPException,
    status,
    Depends
)

from app import models
from app.schemas import ExpenseCreate, ExpenseUpdate
from app.dependencies import get_current_user


router = APIRouter(
    prefix="/api/v1/expenses",
    tags=["Expenses"]
)


# 1. CREATE EXPENSE
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_expense(
    expense: ExpenseCreate,
    current_user: dict = Depends(get_current_user)
):

    new_id = models.next_id

    new_expense = expense.model_dump(mode="json")

    new_expense["id"] = new_id
    new_expense["user_id"] = current_user["id"]

    models.expenses[new_id] = new_expense

    models.next_id += 1

    return {
        "message": "Expense created successfully",
        "data": new_expense
    }


# 2. GET ALL EXPENSES
@router.get("/")
def get_all_expenses(
    current_user: dict = Depends(get_current_user)
):

    user_expenses = [
        expense
        for expense in models.expenses.values()
        if expense["user_id"] == current_user["id"]
    ]

    return {
        "message": "All expenses",
        "data": user_expenses
    }


# 3. GET ONE EXPENSE
@router.get("/{expense_id}")
def get_expense(
    expense_id: int,
    current_user: dict = Depends(get_current_user)
):

    expense = models.expenses.get(expense_id)

    if (
        expense is None
        or expense["user_id"] != current_user["id"]
    ):
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    return {
        "message": "Expense found",
        "data": expense
    }


# 4. UPDATE EXPENSE
@router.put("/{expense_id}")
def update_expense(
    expense_id: int,
    expense: ExpenseUpdate,
    current_user: dict = Depends(get_current_user)
):

    existing_expense = models.expenses.get(expense_id)

    if (
        existing_expense is None
        or existing_expense["user_id"] != current_user["id"]
    ):
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    updated_expense = expense.model_dump(mode="json")

    updated_expense["id"] = expense_id
    updated_expense["user_id"] = current_user["id"]

    models.expenses[expense_id] = updated_expense

    return {
        "message": "Expense updated successfully",
        "data": updated_expense
    }


# 5. DELETE EXPENSE
@router.delete("/{expense_id}")
def delete_expense(
    expense_id: int,
    current_user: dict = Depends(get_current_user)
):

    existing_expense = models.expenses.get(expense_id)

    if (
        existing_expense is None
        or existing_expense["user_id"] != current_user["id"]
    ):
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    del models.expenses[expense_id]

    return {
        "message": "Expense deleted successfully"
    }