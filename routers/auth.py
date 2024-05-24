from fastapi import APIRouter, Depends, HTTPException, status, Body
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from jose import jwt , JWTError
from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError


from core.security import createAccessToken, createRefreshToken
from core.config import settings
from db.mysql import async_session
from models.orm2 import User
from dtos.auth import TokenSchema , TokenPayload
from dtos.user import UserAuthResponse, UserCreate, UserOut
from services.user_service import UserService


# router = APIRouter()


# @router.post('/login', summary="Create access and refresh tokens for user", response_model=TokenSchema)
# async def login(formData: OAuth2PasswordRequestForm= Depends()) -> Any:
#     async with async_session() as session:
#         async with session.begin():
#             user: UserAuthResponse = await UserService(session).authenticate(identifier= formData.username, hashedPassword= formData.password)
#             if not user:
#                 raise HTTPException(
#                     status_code=status.HTTP_400_BAD_REQUEST,
#                     detail="Incorrect identifier or password"
#                 )
#             if not user.user:
#                 raise HTTPException(
#                     status_code=status.HTTP_401_UNAUTHORIZED,
#                     detail="user not found"
#                 )
#             return {
#                 "access_token": createAccessToken(user.user.dni),
#                 "refresh_token": createRefreshToken(user.user.dni),
#             }


# @router.post('/signup', summary="Create user of system", response_model=TokenSchema)
# async def sign_up(data: UserCreate):
#     async with async_session() as session:
#             try:
#                 no_hashed = data.password
#                 user_created: UserOut = await UserService(session).create_user(create_body= data)
#                 if not user_created:
#                     raise HTTPException(
#                         status_code=status.HTTP_400_BAD_REQUEST,
#                         detail="the user was not created"
#                     )
                
#                 user: UserAuthResponse = await UserService(session).authenticate(identifier= data.email, hashedPassword= no_hashed)
#                 if not user:
#                     raise HTTPException(
#                         status_code=status.HTTP_400_BAD_REQUEST,
#                         detail="Incorrect identifier or password"
#                     )
#                 if not user.user:
#                     raise HTTPException(
#                         status_code=status.HTTP_401_UNAUTHORIZED,
#                         detail="user not found"
#                     )
#                 return {
#                     "access_token": createAccessToken(user.user.dni),
#                     "refresh_token": createRefreshToken(user.user.dni),
#                 }
#             except IntegrityError:
#                 raise HTTPException(
#                     status_code=status.HTTP_400_BAD_REQUEST,
#                     detail="User with this email or dni already exist"
#                 )


        
# @router.post('/refresh', summary="Refresh token", response_model=TokenSchema)
# async def refreshToken(refres_token: str = Body(...)) -> Any:
#     async with async_session() as session:
#         async with session.begin():
#             try:
#                 payload = jwt.decode(refres_token, settings.JWT_REFRESH_SECRET_KEY, algorithms=[settings.ALGORITHM])
#                 tokenData = TokenPayload(**payload)
#                 user: UserAuthResponse = await UserService(session).get_current_user(tokenData.sub)
#                 if not user:
#                     raise HTTPException(
#                         status_code=status.HTTP_403_FORBIDDEN,
#                         detail="Invalid token",
#                     )
#                 return {
#                     "access_token": createAccessToken(user.userDetails.dni),
#                     "refresh_token": createRefreshToken(user.userDetails.dni),
#                 }
#             except (JWTError, ValidationError):
#                 raise HTTPException(
#                     status_code=status.HTTP_403_FORBIDDEN,
#                     detail="Invalid token",
#                     headers={"WWW-Authenticate": "Bearer"},
#                 )
            
            

# @authRouter.post('/login', summary="Create access and refresh tokens for user", response_model=TokenSchema)
# async def login(formData: OAuth2PasswordRequestForm= Depends()) -> Any:
#     async with async_session() as session:
#         async with session.begin():
#             user = await UserService(session).authenticate(identifier= formData.username, hashedPassword= formData.password)
#             if not user:
#                 raise HTTPException(
#                     status_code=status.HTTP_404_NOT_FOUND,
#                     detail="Incorrect identifier or password"
#                 )
#             return {
#                 "access_token": createAccessToken(user.userOut.dni),
#                 "refresh_token": createRefreshToken(user.userOut.dni),
#             }




# @authRouter.post('/refresh', summary="Refresh token", response_model=TokenSchema)
# async def refreshToken(refres_token: str = Body(...)):
#     async with async_session() as session:
#         async with session.begin():
#             try:
#                 payload = jwt.decode(refres_token, settings.JWT_REFRESH_SECRET_KEY, algorithms=[settings.ALGORITHM])
#                 tokenData = TokenPayload(**payload)
#             except (JWTError, ValidationError):
#                 raise HTTPException(
#                     status_code=status.HTTP_403_FORBIDDEN,
#                     detail="Invalid token",
#                     headers={"WWW-Authenticate": "Bearer"},
#                 )
#             user = await UserService(session).getUserByIdentifier(tokenData.sub)
#             if not user:
#                 raise HTTPException(
#                     status_code=status.HTTP_403_FORBIDDEN,
#                     detail="Invalid token",
#                 )
#             return {
#                 "access_token": createAccessToken(user.userDetails.dni),
#                 "refresh_token": createRefreshToken(user.userDetails.dni),
#             }
