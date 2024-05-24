from typing import List, Optional
from pydantic import BaseModel, Field , EmailStr
from datetime import datetime
from datetime import time
from datetime import date

class TravelCreate(BaseModel):
    vehicle_id: str = Field(..., description="Travel vehicle id")
    schedule_id: int = Field(..., description="Travel Schedule id")


class SearchTravelDay(BaseModel):
    day: date = Field(..., description="Day of travel")


class TravelUpdate(BaseModel):
    vehicle_id: str = Field(..., description="New travel vehicle id")
    schedule_id: int = Field(..., description="New travel Schedule id")

class TravelOut(BaseModel):
    vehicle_id: str
    schedule_id: int 
    createdAt: datetime
    dateTravel: date

class TravelOutResponse(BaseModel):
    status: bool
    details: str
    travelOut: Optional[TravelOut]


class TravelsResponse(BaseModel):
    status: bool
    details: str
    travelsOut: Optional[List[TravelOut]]





