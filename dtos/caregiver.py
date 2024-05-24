from typing import List, Optional
from pydantic import BaseModel, Field , EmailStr
from datetime import datetime
from datetime import time
from datetime import date


class CaregiverCreate(BaseModel):
    dni:str = Field(..., description="Caregiver dni")
    skill: float = Field(..., description="Caregiver Demand skill")
    schedule_id: int = Field(..., description="Caregiver schedule id")

class CaregiverUpdate(BaseModel):
    skill: float = Field(..., description="New caregiver Demand skill")
    schedule_id: int = Field(..., description="New caregiver schedule id")
    is_active: bool = Field(..., description="Changes caregiver activity")


class CaregiverCreated(BaseModel):
    dni:str 
    skill: float 
    schedule_id: int 
    createdAt: datetime

class CaregiverOut(BaseModel):
    dni: str
    skill: float 
    schedule_id: int 
    email: EmailStr
    name: str
    lastname: str
    is_active: bool
    phone: str
    birthdate: date
    createdAt: datetime    


class CaregiverCreatedResponse(BaseModel):
    status: bool
    details: str
    caregiverOut: Optional[CaregiverCreated]


class CaregiverOutResponse(BaseModel):
    status: bool
    details: str
    caregiverOut: Optional[CaregiverOut]


class CaregiversResponse(BaseModel):
    status: bool
    details: str
    caregiversOut: Optional[List[CaregiverOut]]
