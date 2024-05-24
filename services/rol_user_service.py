from sqlalchemy.orm import Session
from typing import List, Optional

from dtos.user_role import UserRoleIn, UserRoleOut, UserRoleDescription, UserRoleRemove
from repository.user_role import sp_assign_role, sp_get_user_roles_by_id, sp_remove_user_role

class RoleUserService:
    def __init__(self, db_session: Session) -> None:
        self.db = db_session
    
    async def create(self, rol_user_in: UserRoleIn) -> Optional[UserRoleOut]:
        rol_user_out = await sp_assign_role(self.db, user_rol_assign= rol_user_in)
        if rol_user_out:
            return rol_user_out
        else:
            return None

    async def get_user_roles(self, identifier: str) -> Optional[list[UserRoleDescription]]:
        role_set = await sp_get_user_roles_by_id(self.db, identifier=identifier)
        if role_set:
            return role_set
        else:
            return None
        

    async def remove_user_role(self, identifier: str) -> Optional[UserRoleRemove]:
        user_role_remove = await sp_remove_user_role(self.db, identifier= identifier)
        if user_role_remove:
            return user_role_remove
        else:
            return None
