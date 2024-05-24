from sqlalchemy.orm import Session
from sqlalchemy.future import select
from sqlalchemy import or_
from typing import Optional
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime, date

from models.orm2 import User
from dtos.user import UserCreate, UserOut, UserDetails, UserAuth



async def sp_get_user_by_id(db: Session, identifier: str) -> Optional[UserOut]: 
    """Retrieves a user by their DNI or email
    """
    try:
        query = (
            select(User).where(or_(User.dni == identifier, User.email == identifier)).limit(1) 
        )
        user: User = await db.scalar(query)
        if user:
            return UserOut(
                dni= user.dni, 
                email= user.email, 
                name= user.name, 
                lastname= user.lastname, 
                is_active= user.is_active, 
                phone= user.phone, 
                birthdate= user.birthdate, 
                img= user.img, 
                createdAt= user.createdAt
            )
        
        else:
            return None
    except SQLAlchemyError as e:
        return None
    

async def sp_get_user_auth(db: Session, identifier: str) -> Optional[UserAuth]: 
    try:
        query = (
            select(User).where(or_(User.dni == identifier, User.email == identifier)).limit(1) 
        )
        user: User = await db.scalar(query)
        if user:
            return UserAuth(
                dni= user.dni, 
                email= user.email, 
                password= user.password
            )
        else:
            return None
    except SQLAlchemyError as e:
        return None
    


async def sp_create_user(db: Session, create_body: UserCreate) -> Optional[UserOut]:
    try:
        user_in = User(
            dni = create_body.dni,
            email = create_body.email,
            password = create_body.password,
            name = create_body.name,
            lastname = create_body.lastname,
            phone = create_body.phone,
            birthdate = create_body.birthdate,
            img = None,
            is_active = True,
            createdAt = datetime.now(),
            updatedAt = None,
            deletedAt = None
        )
        db.add(user_in)
        await db.commit()
        await db.refresh(user_in)
        user_out: UserOut = await sp_get_user_by_id(db=db, identifier=user_in.dni)
        if user_out:
            return user_out
        else:
            return None
    except SQLAlchemyError as e:
        await db.rollback()
        return None 




