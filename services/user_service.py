from sqlalchemy.sql import func
from typing import Optional
from sqlalchemy import or_
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import update
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from datetime import datetime, date

from dtos.user import UserCreate, UserCratedResponse, UserOut,  UserOutResponse, UserDetailsResponse, UserAuth, UserAuthResponse
from core.security import getPassword, verifyPassword
from models.orm2 import User
from repository.users import sp_create_user, sp_get_user_by_id, sp_get_user_auth


class UserService:

    def __init__(self, db_session: Session):
        self.db: Session = db_session

    async def create_user(self, create_body: UserCreate) -> Optional[UserOut]:
        create_body.password = getPassword(create_body.password)
        user_created: UserOut = await sp_create_user(db=self.db, create_body= create_body)
        if user_created:
            return user_created
        else:
            return None
        
    async def get_current_user(self, identifier: str) -> Optional[UserOut]:
        user_out: UserOut = await sp_get_user_by_id(db= self.db, identifier=identifier)
        if not user_out:
            return None
        return user_out

    async def get_user_by_identifier(self, identifier: str) -> Optional[UserOut]:
        user_out: UserOut = await sp_get_user_by_id(db= self.db, identifier=identifier)
        if not user_out:
            return None
        return user_out

    async def authenticate(self, identifier: str, password: str) -> Optional[UserOut]:
        user_auth: UserAuth =  await sp_get_user_auth(db=self.db, identifier= identifier)
        if not user_auth or not verifyPassword(password, user_auth.password):
            return None
        user_out: UserOut = await sp_get_user_by_id(db= self.db, identifier=user_auth.dni)
        if not user_out:
            return None
        return user_out
            

        

        




#     async def authenticate(self, identifier: str, hashedPassword: str) -> Optional[UserOutResponse]:
#         try:
        
#             user = await getUserById(self.dbSession, identifier)

#             if not user or not verifyPassword(hashedPassword, user.password):
#                 return None
            
#             userOut = UserOut (
#                 dni= user.dni, 
#                 email= user.email, 
#                 name= user.name, 
#                 lastname=user.lastname, 
#                 is_active=user.is_active
#             )
#             return UserOutResponse(status=True, userOut=userOut)
        
#         except SQLAlchemyError as e:
#             print(e)
#             return  UserOutResponse(status=False, userOut=None)
        


#     async def getUserByIdentifier(self, identifier: str) -> Optional[UserDetailsResponse]:
#         try:
#             user = await getUserById(self.dbSession, identifier)

#             if not user:
#                 return UserDetailsResponse(status=False, userDetails=None)
#             if not user.is_active:
#                 return UserDetailsResponse(status=False, userDetails=None)
            
#             userDetails = UserDetails(
#                 dni= user.dni,
#                 email= user.email,
#                 name= user.name,
#                 lastname= user.lastname,
#                 is_active= user.is_active,
#                 phone= user.phone,
#                 birthdate = user.birthdate.__str__()
#             )
            
#             return UserDetailsResponse(status=True, userDetails=userDetails)
        
#         except SQLAlchemyError as e:
#             print(e)
#             return  UserDetailsResponse(status=False, userDetails=None)