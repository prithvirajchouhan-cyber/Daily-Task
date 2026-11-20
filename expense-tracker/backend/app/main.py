from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import router as expense_router
from app.auth_routes import router as auth_router


app = FastAPI(
    title="Personal Expense Tracker",
    description="Expense Tracker API with JWT Authentication",
    version="2.0.0"
)


# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Register routers
app.include_router(auth_router)
app.include_router(expense_router)


@app.get("/")
def home():

    return {
        "message": "Welcome to Personal Expense Tracker API"
    }