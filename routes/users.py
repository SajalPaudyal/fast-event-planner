from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSignIn

user_router = APIRouter(
    tags=["User"]
)

users = {}

@user_router.post("/signup")
async def sign_new_user(user: User) -> dict:
    if user.email in users:
        raise HTTPException(
            status_code= status.HTTP_409_CONFLICT,
            detail="User with given username exists."
        )
    users[user.email] = user

    return{
        "message":users
    }


@user_router.post("/signin")
async def sign_in_user(user: UserSignIn) -> dict:
    try:
        if user.email not in users:
            raise KeyError
        if users[user.email].password != user.password:
            raise KeyError
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wrong credentials passed"
        )

    return {
        "message": "User signed in successfully"
    }
