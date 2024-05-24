from fastapi import APIRouter, HTTPException, status
from fastapi import Depends
from sqlalchemy.exc import IntegrityError
from typing import Optional

from db.mysql import async_session
from dtos.user import UserOut
from dtos.user_role import UserRoleIn, UserRoleOut, UserRolesSet, UserRoleDescription, UserRoleRemove
from services.authService import get_current_user
from services.rol_user_service import RoleUserService

router = APIRouter()


@router.post("/assign-role", summary="assign role to user", response_model= UserRoleOut)
async def assign_role(user_rol_in: UserRoleIn, user: UserOut = Depends(get_current_user)) -> Optional[UserRoleOut]:
    async with async_session() as session:
        try:
            if not user:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="user not found"
                )
            user_rol: UserRoleOut = await RoleUserService(session).create(user_rol_in)
            if  not user_rol:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="role could not be assigned"
                )
            return user_rol
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="could not create user role"
            )


@router.patch('/user-role-remove/{id}', summary="remove user role", response_model=UserRoleRemove)
async def remove_user_role(identifier: str, user: UserOut = Depends(get_current_user)) -> Optional[UserRoleRemove]:
    async with async_session() as session:
        async with session.begin():
            try:
                if not user:
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="user not found"
                    )
                remove_msg = await RoleUserService(session).remove_user_role(identifier=identifier)
                if not remove_msg:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Error in request"
                    )
                return remove_msg
            except IntegrityError:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Error in request"
                )
            

@router.get('/get-user-roles/{id}', summary="get user roles", response_model=UserRolesSet)
async def get_user_roles(identifier: str,  user: UserOut = Depends(get_current_user)) -> Optional[UserRolesSet]:
    async with async_session() as session:
        async with session.begin():
            try:
                if not user:
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="user not found"
                    )
                user_roles: list[UserRoleDescription] = await RoleUserService(session).get_user_roles(identifier)
                if not user_roles:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail="user roles were not obtained"
                    )
                empty_roles: bool = False
                if len(user_roles) == 0:
                    empty_roles = True
                return UserRolesSet(
                    user_id= identifier, 
                    roles= user_roles, 
                    empty= empty_roles
                )
            except IntegrityError:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="could not create user role"
                )
