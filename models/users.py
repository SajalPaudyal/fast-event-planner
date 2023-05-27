from pydantic import BaseModel, EmailStr
from typing import List, Optional
from models.events import Event

class User(BaseModel):
    email:EmailStr
    password:str

    class Config:
        schema_extra ={
            "example" : {
                "email": "fastapi@packt.com",
                "password":"userpassword@123",
            }
        }

class UserSignIn(BaseModel):
    email: EmailStr
    password: str
    class Config:
        schema_extra = {
            "example": {
            "email": "fastapi@packt.com",
            "password": "strong!!!",
            "events": [],
        }
    }

