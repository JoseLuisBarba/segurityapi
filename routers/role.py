from fastapi import APIRouter, HTTPException, status
from fastapi import Depends
from db.mysql import async_session
from sqlalchemy.exc import IntegrityError
from typing import Optional
from dtos.role import RoleOut, RoleCreate, RoleId, RoleResponse, RolesResponse, RoleRemove, RoleUpdate
from dtos.user import UserOut
from dtos.user_role import UserRoleIn, UserRoleOut
from services.role import RolService
from services.authService import get_current_user


route = APIRouter()



@route.post("/create", summary="Create new rol", response_model= RoleResponse)
async def create_rol(data: RoleCreate, user: UserOut = Depends(get_current_user)) -> Optional[RoleResponse]:
    async with async_session() as session:
        try:
            if not user:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="user not found"
                )
            rol_out = await RolService(db_session=session).create(data)
            if  not rol_out:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="could not create role"
                )
            return RoleResponse(
                rol = rol_out,
                detail= "was created successfully"
            )
            
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="could not create role"
            )

@route.get('/getall/', summary="Get all rol", response_model=RolesResponse)
async def get_all(user: UserOut = Depends(get_current_user)):
    async with async_session() as session:
        async with session.begin():
            try:
                if not user:
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="user not found"
                    )
                roles = await RolService(session).get_all()
                if roles:
                    if len(roles) == 0:
                        return RolesResponse(
                            roles= [],
                            detail= "empty"
                        )
                    return RolesResponse(
                        roles=roles,
                        detail="was successfully obtained"
                    )
                else:
                    return RolesResponse(
                            roles= [],
                            detail= "empty"
                    )
            except IntegrityError:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Error in request"
                )

@route.get('/get/{id}', summary="Get rol by id", response_model=RoleResponse)
async def get_one(id: int,  user: UserOut = Depends(get_current_user)):
    async with async_session() as session:
        async with session.begin():
            try:
                if not user:
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="user not found"
                    )
                role = await RolService(session).get_one(RoleId(id=id))
                if not role:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Error in request"
                    )
                return RoleResponse(
                    rol=role,
                    detail="was successfully obtained"
                )
            except IntegrityError:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Error in request"
                )

@route.patch('/remove/{id}', summary="Remove rol by id", response_model=RoleRemove)
async def remove(id: int, user: UserOut = Depends(get_current_user)):
    async with async_session() as session:
        async with session.begin():
            try:
                if not user:
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="user not found"
                    )
                remove_msg = await RolService(session).remove(rol_id=RoleId(id=id))
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
            
@route.put('/update/{id}', summary="update rol by id", response_model=RoleResponse)
async def update_rol(id: int, update_body: RoleUpdate, user: UserOut = Depends(get_current_user)):
    async with async_session() as session:
        try:
            if not user:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="user not found"
                )
            role_updated = await RolService(db_session=session).update(rol_id=RoleId(id=id), update_body=update_body)
            if not role_updated:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="could not update role"
                )
            return RoleResponse(
                rol = role_updated,
                detail= "was updated successfully"
            )             
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="could not update role"
            )

@route.delete('/delete/{id}', summary="Remove rol by id", response_model=RoleRemove)
async def delete_rol(id: int):
    pass