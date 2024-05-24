from typing import List, Optional
from pydantic import BaseModel, Field 
from datetime import datetime
from datetime import time


class ScheduleCreate(BaseModel):
    id: int = Field(..., description="Schedule id")
    start_time: time = Field(..., description="start time of turn work, exa: 10:30:00")
    leaving_time: time = Field(..., description="leaving time of turn work,  exa: 10:30:00")


class ScheduleOut(BaseModel):
    id: int 
    start_time: time 
    leaving_time: time 
    is_active: bool
    createdAt: datetime


class ScheduleOutResponse(BaseModel):
    status: bool
    details: str
    scheduleOut: Optional[ScheduleOut]


class SchedulesResponse(BaseModel):
    status: bool
    details: str
    schedulesOut: Optional[List[ScheduleOut]]