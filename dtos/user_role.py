from typing import Optional
from pydantic import BaseModel, EmailStr, Field 
from datetime import datetime
from datetime import date
import uuid 

class UserRoleIn(BaseModel):
    user_id: str
    role_id: int 

class UserRoleOut(BaseModel):
    id: uuid.UUID
    user_id: str
    role_id: int
    is_active: bool
    createdAt: datetime
    updatedAt: Optional[datetime]
    deletedAt: Optional[datetime]


class UserRoleDescription(BaseModel):
    id: uuid.UUID
    user_id: str
    role_id: int
    is_active: bool
    createdAt: datetime
    updatedAt: Optional[datetime]
    deletedAt: Optional[datetime]
    role_name: str
    role_desp: str



class UserRolesSet(BaseModel):
    user_id: str
    roles: Optional[list[UserRoleDescription]]
    empty: bool 



class UserRoleRemove(BaseModel):
    status: bool
    detail: str