from datetime import datetime
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from pydantic import ValidationError
from typing import Optional

from core.config import settings
from dtos.auth import TokenPayload
from dtos.user import  UserOut
from services.user_service import UserService
from db.mysql import async_session


reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/auth/login",
    scheme_name="JWT"
)

async def get_current_user( token: str = Depends(reuseable_oauth), ) -> Optional[UserOut]:
    async with async_session() as session:
        async with session.begin():
            try:
                payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.ALGORITHM])
                token_data = TokenPayload(**payload)
                if datetime.fromtimestamp(token_data.exp) < datetime.now():
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Token expired",
                        headers={"WWW-Authenticate": "Bearer"},
                    )
              
                user_out: UserOut = await UserService(session).get_current_user(token_data.sub)
        
                if user_out is None:
                    raise HTTPException(
                        status_code=status.HTTP_403_FORBIDDEN,
                        detail="Could not find user",
                        headers={"WWW-Authenticate": "Bearer"},
                    )    
                return user_out
        
            except (JWTError, ValidationError):
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Could not validate credentials",
                    headers={"WWW-Authenticate": "Bearer"},
                )  
        
            
            

            