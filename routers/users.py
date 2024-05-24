from fastapi import APIRouter, HTTPException, status
from fastapi import Depends
from sqlalchemy.exc import IntegrityError

from models.orm2 import User
from services.user_service import UserService
from services.authService import get_current_user
from dtos.user import UserOut
from db.mysql import async_session



router = APIRouter()




@router.get('/me', summary='Get details of currently logged in user', response_model=UserOut)
async def get_me(user: UserOut = Depends(get_current_user)):
    async with async_session() as session:
        async with session.begin():
            return user

