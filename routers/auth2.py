from fastapi import APIRouter, status, HTTPException, Depends, Body
from fastapi.responses import RedirectResponse
from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError
from fastapi.security import OAuth2PasswordRequestForm
from typing import Optional
from jose import jwt, JWTError

from core.security2 import create_access_token, create_refresh_token
from core.config import settings
from db.mysql import async_session
from dtos.auth import TokenSchema , TokenPayload
from dtos.user import UserAuthResponse, UserCreate, UserOut
from services.user_service import UserService
from services.authService import get_current_user



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
                    refresh_token=create_refresh_token(user_auth.dni)
                )
            except IntegrityError:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="user could not be authenticated"
                )


@router.post('/test-token', summary="Test if the access token is valid", response_model=UserOut)
async def test_token(user: UserOut = Depends(get_current_user)) -> UserOut:
    return user


@router.post('/refresh', summary="Refresh token", response_model=TokenSchema)
async def get_refresh_token(refresh_token: str= Body(...)):
    async with async_session() as session:
        async with session.begin():
            try:
                payload = jwt.decode(refresh_token, settings.JWT_REFRESH_SECRET_KEY, algorithms=[settings.ALGORITHM])
                token_data = TokenPayload(**payload)
                user_out: UserOut = await UserService(session).get_current_user(token_data.sub)
                if user_out is None:
                    raise HTTPException(
                        status_code=status.HTTP_403_FORBIDDEN,
                        detail="Invalid token for user",
                        headers={"WWW-Authenticate": "Bearer"},
                    )    
                return TokenSchema(
                    access_token=create_access_token(user_out.dni),
                    refresh_token=create_refresh_token(user_out.dni)
                )
        
            except (JWTError, ValidationError):
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Could not validate credentials",
                    headers={"WWW-Authenticate": "Bearer"},
                ) 