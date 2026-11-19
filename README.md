# Personal Expense Tracker

A beginner-friendly expense management application built using **Python, FastAPI, HTML, CSS, and JavaScript**.

This project demonstrates basic CRUD (Create, Read, Update, Delete) operations through REST APIs. Users can add, view, edit, and delete their daily expenses.

## 1. Project Overview

The Personal Expense Tracker helps users manage their daily expenses by recording:

- Expense title
- Amount
- Category
- Expense date

The frontend communicates with the FastAPI backend using JavaScript Fetch API.

## 2. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | REST API development |
| Pydantic | Data validation |
| HTML | Frontend structure |
| CSS | Frontend styling |
| JavaScript | Frontend functionality and API integration |
| Postman | API testing |
| Uvicorn | Backend development server |

## 3. Project Structure

```text
expense-tracker/
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── routes.py
│   │   ├── models.py
│   │   └── schemas.py
│   │
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── assets/
│
└── README.md
```

## 4. Features

- Add new expenses.
- View all expenses.
- Edit existing expenses.
- Delete expenses.
- Validate expense information.
- Display expenses in a table.
- Communicate with backend APIs using JavaScript Fetch API.

## 5. Backend API Endpoints

Base URL:

```text
http://127.0.0.1:8000
```

| Operation | HTTP Method | Endpoint |
|---|---|---|
| Create expense | POST | `/api/v1/expenses/` |
| Get all expenses | GET | `/api/v1/expenses/` |
| Get expense by ID | GET | `/api/v1/expenses/{expense_id}` |
| Update expense | PUT | `/api/v1/expenses/{expense_id}` |
| Delete expense | DELETE | `/api/v1/expenses/{expense_id}` |

## 6. Sample API Request

Example: Create an expense.

**POST**

```text
http://127.0.0.1:8000/api/v1/expenses/
```

Request body:

```json
{
    "title": "Lunch",
    "amount": 150,
    "category": "Food",
    "expense_date": "2026-11-18"
}
```

## 7. Installation and Setup

### Prerequisites

- Python 3.10 or above
- VS Code
- Postman
- A web browser

### Step 1: Clone or download the project

Open the project directory in your terminal.

### Step 2: Create and activate virtual environment

From the project root:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install dependencies

```bash
pip install -r backend/requirements.txt
```

### Step 4: Start the backend server

```bash
cd backend
python -m uvicorn app.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

### Step 5: Start the frontend server

Open a second terminal from the project root:

```bash
python3 -m http.server 5500 --directory frontend
```

Frontend URL:

```text
http://127.0.0.1:5500
```

## 8. API Testing with Postman

The following operations were tested using Postman:

1. POST – Create an expense.
2. GET – Retrieve all expenses.
3. GET – Retrieve an expense by ID.
4. PUT – Update an existing expense.
5. DELETE – Delete an expense.

All CRUD operations were tested successfully.

## 9. Important Note

This project currently uses temporary in-memory storage with a Python dictionary.

- No database is connected yet.
- Expense records are lost when the backend server restarts.
- SQLite or another database can be integrated in a future version.

## 10. Learning Outcomes

Through this project, I learned:

- Basics of client-server architecture.
- How REST APIs work.
- HTTP methods and status codes.
- Creating API endpoints using FastAPI.
- Request validation using Pydantic.
- Implementing CRUD operations.
- Testing APIs using Postman.
- Connecting frontend and backend using JavaScript Fetch API.
- Handling JSON data between frontend and backend.

## 11. Future Improvements

- Integrate SQLite database.
- Add user authentication.
- Add expense summary and monthly reports.
- Add category-based filtering.
- Improve dashboard design.

---

**Project:** Personal Expense Tracker  
**Type:** Backend Training Project – Day 1  
**Backend:** Python + FastAPI  
**Frontend:** HTML + CSS + JavaScript  
**API Testing:** Postman
