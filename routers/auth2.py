from fastapi import APIRouter, FastAPI, status, HTTPException, Depends
from fastapi.responses import RedirectResponse
from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError
from fastapi.security import OAuth2PasswordRequestForm
from typing import Optional


from core.security2 import create_access_token, create_refresh_token
from core.config import settings
from db.mysql import async_session
from models.orm2 import User
from dtos.auth import TokenSchema , TokenPayload
from dtos.user import UserAuthResponse, UserCreate, UserOut
from services.user_service import UserService



router = APIRouter()


@router.post('/signup', summary="Create new user", response_model=UserOut)
async def create_user(data: UserCreate):
    async with async_session() as session:
            try:
                #check if user already exist
                user_out: UserOut  = await UserService(session).get_user_by_identifier(data.email)
                if user_out:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail="User with this email already exist"
                    )
                #saving
                user_created: UserOut = await UserService(session).create_user(data)
                if not user_created:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail="the user was not created"
                    )
                return user_created  
            except IntegrityError:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="User with this email or dni already exist"
                )

@router.post('/login', summary="Create access and refresh tokens for user", response_model=TokenSchema)
async def login(form_data: OAuth2PasswordRequestForm= Depends()) -> Optional[TokenSchema]:
    async with async_session() as session:
        async with session.begin():
            try:
                #check if user already exist
                user_out: UserOut  = await UserService(session).get_user_by_identifier(
                    identifier=form_data.username
                )
                if not user_out:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail="The user with this email or clave does not exist"
                    )
                #verify
                user_auth: UserOut = await UserService(session).authenticate(
                    identifier= form_data.username,
                    password= form_data.password
                )
                if not user_auth:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail="incorrect password"
                    )
                return TokenSchema(
                    access_token=create_access_token(user_auth.dni),
                    refresh_token
                    =create_refresh_token(user_auth.dni)
                )
            except IntegrityError:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="user could not be authenticated"
                )


            