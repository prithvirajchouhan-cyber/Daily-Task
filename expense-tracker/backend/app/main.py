
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import router

# Create FastAPI application
app = FastAPI(
    title="Personal Expense Tracker",
    description="A beginner-friendly CRUD API",
    version="1.0.0"
)

# Allow frontend to communicate with backend
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

# Connect API routes
app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Personal Expense Tracker API"
    }
