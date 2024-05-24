from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field 
from datetime import datetime
from datetime import date

class PatientCreate(BaseModel):
    dni: str = Field(..., description="User's DNI")

class PatientCreated(BaseModel):
    dni:str 
    createdAt: datetime

class PatientOut(BaseModel):
    dni: str
    email: EmailStr
    name: str
    lastname: str
    is_active: bool
    phone: str
    birthdate: date
    userCreatedAt: datetime 
    patientCreatedAt: datetime    



class PatientOutResponse(BaseModel):
    status: bool
    PatientOut: Optional[PatientOut]

class PatientCreatedResponse(BaseModel):
    status: bool
    details: str
    PatientOut: Optional[PatientCreated]

class PatientsResponse(BaseModel):
    status: bool
    details: str
    patientsOut: Optional[List[PatientOut]]



# from typing import List, Optional
# from pydantic import BaseModel, Field , EmailStr
# from datetime import datetime
# from datetime import time
# from datetime import date


# class CaregiverCreate(BaseModel):
#     dni:str = Field(..., description="Caregiver dni")
#     skill: float = Field(..., description="Caregiver Demand skill")
#     schedule_id: int = Field(..., description="Caregiver schedule id")

# class CaregiverUpdate(BaseModel):
#     skill: float = Field(..., description="New caregiver Demand skill")
#     schedule_id: int = Field(..., description="New caregiver schedule id")
#     is_active: bool = Field(..., description="Changes caregiver activity")


# class CaregiverCreated(BaseModel):
#     dni:str 
#     skill: float 
#     schedule_id: int 
#     createdAt: datetime

# class CaregiverOut(BaseModel):
#     dni: str
#     skill: float 
#     schedule_id: int 
#     email: EmailStr
#     name: str
#     lastname: str
#     is_active: bool
#     phone: str
#     birthdate: date
#     createdAt: datetime    


# class CaregiverCreatedResponse(BaseModel):
#     status: bool
#     details: str
#     caregiverOut: Optional[CaregiverCreated]


# class CaregiverOutResponse(BaseModel):
#     status: bool
#     details: str
#     caregiverOut: Optional[CaregiverOut]


# class CaregiversResponse(BaseModel):
#     status: bool
#     details: str
#     caregiversOut: Optional[List[CaregiverOut]]
