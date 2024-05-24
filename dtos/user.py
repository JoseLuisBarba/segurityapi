from typing import Optional
from pydantic import BaseModel, EmailStr, Field 
from datetime import datetime
from datetime import date


class UserCreate(BaseModel):
    dni: str = Field(..., description="User's DNI")
    email: EmailStr = Field(...,   description="User's email address")
    password: str = Field(...,  description="User's password")
    name: str = Field(..., description="User's first name")
    lastname: str = Field(..., description="User's last name")
    birthdate: date = Field(..., description="User's birthdate (YYYY-MM-DD)")  
    phone: str = Field(...,  description="User's phone number")

class UserOut(BaseModel):
    dni: str
    email: EmailStr
    name: str
    lastname: str
    is_active: Optional[bool] = True
    phone: str
    birthdate: date
    img: Optional[str]
    createdAt: datetime

class UserAuthResponse(BaseModel):
    user: Optional[UserOut]
    status: bool
    detail: str

class UserCratedResponse(BaseModel):
    user_created: Optional[UserOut]
    status: bool
    detail: str 

class UserAuth(BaseModel):
    dni: str 
    email: EmailStr 
    password: str 


class UserDetails(BaseModel):
    dni: str
    email: EmailStr
    name: str
    lastname: str
    is_active: Optional[bool] = True
    phone: str
    birthdate: date
    img: Optional[None]
    createdAt: datetime

class UserUpdate(BaseModel):
    email: Optional[str] = None
    is_active: Optional[bool] = None


class UserCurrent(BaseModel):
    dni: str 
    email: EmailStr 
    name: str 
    lastname: str 
    phone: str 
    birthdate: str  
    is_active: bool
    createdAt: datetime

class UserOutResponse(BaseModel):
    status: bool
    userOut: Optional[UserOut]


class UserDetailsResponse(BaseModel):
    status: bool
    userDetails: Optional[UserDetails]



