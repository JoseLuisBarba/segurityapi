from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field 
from datetime import datetime

class VehicleCreate(BaseModel):
    reg_num: str = Field(..., description="Vehicle's plate")
    capacity: int = Field(..., description="Vehicle's capacity")
    average_speed: float = Field(..., description="Vehicle's avg speed")
    freight_km: float = Field(..., description="Vehicle's freight per km")

    lat: float = Field(..., description="Vehicle's latitude")
    lng: float = Field(..., description="Vehicle's longitude")

class VehicleOut(BaseModel):
    reg_num: str 
    capacity: int 
    average_speed: float 
    freight_km: float 
    lat: float 
    lng: float 
    is_active: bool
    createdAt:  datetime


class VehicleOutResponse(BaseModel):
    status: bool
    vehicleOut: VehicleOut

class VehiclesResponse(BaseModel):
    status: bool
    vehiclesOut: List[VehicleOut]

class VehicleId(BaseModel):
    id: str


class VehicleUpdate(BaseModel):
    reg_num: str = Field(..., description="Vehicle's plate")
    capacity: int = Field(..., description="Vehicle's capacity")
    average_speed: float = Field(..., description="Vehicle's avg speed")
    freight_km: float = Field(..., description="Vehicle's freight per km")
    lat: float = Field(..., description="Vehicle's latitude")
    lng: float = Field(..., description="Vehicle's longitude")
    is_active: bool = Field(..., description="Vehicle's viable")

