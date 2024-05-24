import uuid
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from sqlalchemy import or_, and_, update, insert, Uuid
from typing import Optional
from sqlalchemy.exc import SQLAlchemyError

from datetime import datetime, date

from models.orm2 import UserRole, Role
from dtos.user import UserCreate, UserOut
from dtos.user_role import UserRoleIn, UserRoleOut, UserRoleDescription, UserRoleRemove




async def sp_assign_role(db: Session, user_rol_assign: UserRoleIn) -> Optional[UserRoleOut]:
    try:
        user_role_in = UserRole(
            id= uuid.uuid4(),
            user_id= user_rol_assign.user_id,
            role_id= user_rol_assign.role_id,
            is_active= True,
            createdAt= datetime.now()
        )
        db.add(user_role_in)
        await db.commit()
        await db.refresh(user_role_in)
        if not user_role_in:
            return None
        return UserRoleOut(
            id= user_role_in.id, 
            user_id= user_role_in.user_id, 
            role_id= user_role_in.role_id, 
            is_active= user_role_in.is_active, 
            createdAt= user_role_in.createdAt, 
            updatedAt= user_role_in.updatedAt, 
            deletedAt= user_role_in.deletedAt
        )    
    except SQLAlchemyError as e:
        await db.rollback()
        return None 




async def sp_get_user_roles_by_id(db: Session, identifier: str) -> Optional[list[UserRoleDescription]]:
    try:

        query = (
            select(UserRole, Role)
                .select_from(UserRole)
                .where(and_(UserRole.is_active == True, UserRole.user_id == identifier, Role.is_active == True))
                .join(Role, UserRole.role_id == Role.id )
                .order_by(UserRole.createdAt.desc())
        )
        roles = await db.execute(query)
        user_role_set = [
            UserRoleDescription(
                id= user_role.id, 
                user_id= user_role.user_id, 
                role_id= user_role.role_id, 
                is_active= user_role.is_active, 
                createdAt= user_role.createdAt, 
                updatedAt= user_role.updatedAt, 
                deletedAt= user_role.deletedAt, 
                role_name= role.name, 
                role_desp= role.description
            ) for user_role, role in roles
        ]
        if not user_role_set:
            None
        return user_role_set

    except SQLAlchemyError as e:
        await db.rollback()
        return None
 

async def sp_remove_user_role(db: Session, identifier: str) -> Optional[UserRoleRemove]:
    try:
        identifier_uuid = uuid.UUID(identifier)
        query = (
            update(UserRole)
            .where(UserRole.id == identifier_uuid)
            .values(
                is_active= False,
                updatedAt= datetime.now(), 
                deletedAt= datetime.now()
            ) 
        )
        await db.execute(query)
        await db.commit()

        return UserRoleRemove(
            status=True,
            detail="role successfully removed"
        )
    except SQLAlchemyError as e:
        await db.rollback()
        return UserRoleRemove(
            status=False,
            detail="could not remove role"
        )