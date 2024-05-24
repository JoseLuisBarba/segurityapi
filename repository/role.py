from models.orm2 import Role
from typing import List, Optional
from sqlalchemy.orm import Session
from dtos.role import RoleCreate, RoleOut, RoleId, RoleRemove, RoleUpdate
from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import or_, and_, update
from datetime import datetime
from sqlalchemy.sql import func

async def get_all_roles(db: Session) -> Optional[List[RoleOut]]:
    try:
        query = (
            select(Role).where(Role.is_active == True)
        )
        roles = await db.scalars(query)
        return [
            RoleOut(
                id= rol.id,
                name= rol.name,
                description= rol.description,
                is_active= rol.is_active,
                createdAt= rol.createdAt,
                updatedAt= rol.updatedAt,
                deletedAt= rol.deletedAt,
            ) for rol in roles
        ]
    except SQLAlchemyError as e:
        return None

async def get_one(db: Session, rol_id: RoleId) -> Optional[RoleOut]:
    try:
        query = (
            select(Role).where(Role.id == rol_id.id).limit(1) 
        )
        rol = await db.scalar(query)
        if rol:
            return RoleOut(
                id= rol.id,
                name= rol.name,
                description= rol.description,
                is_active= rol.is_active,
                createdAt= rol.createdAt,
                updatedAt= rol.updatedAt,
                deletedAt= rol.deletedAt,
            )
        else:
            return None
    except SQLAlchemyError as e:
        return None



async def create_rol(db: Session, rol: RoleCreate) ->  Optional[RoleOut]:
    try:
        rol_in = Role(
            name = rol.name,
            description = rol.description,
            is_active = True,
            createdAt = datetime.now(),
            updatedAt = None,
            deletedAt = None
        )
        db.add(rol_in)
        await db.commit()
        await db.refresh(rol_in)
        rol_out = await get_one(db, rol_id= RoleId(id=rol_in.id))
        if rol_out:
            return rol_out
        else:
            return None
    except SQLAlchemyError as e:
        await db.rollback()
        return None 

async def deactivate_role(db: Session, rol_id: RoleId) ->  Optional[RoleRemove]:
    try:
        query = (
            update(Role)
            .where(Role.id == rol_id.id)
            .values(
                is_active= False,
                updatedAt= datetime.now(), 
                deletedAt= datetime.now()
            ) 
        )
        await db.execute(query)
        await db.commit()
        return RoleRemove(status=True, detail="successfully deleted")
    except SQLAlchemyError as e:
        await db.rollback()
        return RoleRemove(status=False, detail="deletion error")


async def update_role(db: Session, rol_id: RoleId, update_body: RoleUpdate) ->  Optional[RoleOut]:
    try:
        query = (
            update(Role)
            .where(Role.id == rol_id.id)
            .values(
                **update_body.model_dump()
            ) 
        )
        await db.execute(query)
        await db.commit()
        return await get_one(db, rol_id=rol_id)
    except SQLAlchemyError as e:
        await db.rollback()
        return await get_one(db, rol_id=rol_id)