import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, HTTPException, status

from app import models
from app.auth import (
    hash_password,
    verify_password,
    create_access_token,
    create_refresh_token,
    hash_refresh_token
)
from app.schemas import (
    UserRegister,
    UserLogin,
    RefreshRequest,
    TokenResponse
)


router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"]
)


# 1. REGISTER
@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user: UserRegister):

    # Check whether username already exists
    for existing_user in models.users.values():

        if existing_user["username"] == user.username:
            raise HTTPException(
                status_code=409,
                detail="Username already exists"
            )

    user_id = str(uuid.uuid4())

    new_user = {
        "id": user_id,
        "username": user.username,
        "password": hash_password(user.password)
    }

    models.users[user_id] = new_user

    return {
        "message": "User registered successfully",
        "username": user.username
    }


# 2. LOGIN
@router.post("/login", response_model=TokenResponse)
def login(user: UserLogin):

    # Find user by username
    existing_user = None

    for stored_user in models.users.values():

        if stored_user["username"] == user.username:
            existing_user = stored_user
            break

    # Verify username and password
    if (
        existing_user is None
        or not verify_password(
            user.password,
            existing_user["password"]
        )
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    user_id = existing_user["id"]

    access_token = create_access_token(user_id)
    refresh_token = create_refresh_token(user_id)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }


# 3. REFRESH ACCESS TOKEN
@router.post("/refresh", response_model=TokenResponse)
def refresh_token(request: RefreshRequest):

    token_hash = hash_refresh_token(request.refresh_token)

    stored_token = models.refresh_tokens.get(token_hash)

    if stored_token is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid refresh token"
        )

    if stored_token["expires_at"] <= datetime.now(timezone.utc):

        models.refresh_tokens.pop(token_hash, None)

        raise HTTPException(
            status_code=401,
            detail="Refresh token expired"
        )

    user_id = stored_token["user_id"]

    if user_id not in models.users:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    # Rotate refresh token: invalidate the old one
    models.refresh_tokens.pop(token_hash)

    new_access_token = create_access_token(user_id)
    new_refresh_token = create_refresh_token(user_id)

    return {
        "access_token": new_access_token,
        "refresh_token": new_refresh_token,
        "token_type": "bearer"
    }


# 4. LOGOUT
@router.post("/logout")
def logout(request: RefreshRequest):

    token_hash = hash_refresh_token(request.refresh_token)

    models.refresh_tokens.pop(token_hash, None)

    return {
        "message": "Logged out successfully"
    }