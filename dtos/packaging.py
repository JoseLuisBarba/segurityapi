from typing import List, Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime
from dtos.caregiver import CaregiverOut

class PackagingOut(BaseModel):
    id: int
    reg_num: str
    MAX_Q: float
    MIN_Q: float
    VD: float
    FLETE: float
    CC: float
    EM: float
    caregivers: Optional[List[CaregiverOut]]

class PackagingOutResponse(BaseModel):
    status: bool
    details: str
    packagingOut: Optional[List[PackagingOut]]
    executeAt: datetime

