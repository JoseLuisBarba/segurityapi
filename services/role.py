from sqlalchemy.orm import Session
from typing import List, Optional

from dtos.role import RoleCreate, RoleOut, RoleId, RoleRemove, RoleUpdate
from repository.role import create_rol, get_all_roles, get_one, deactivate_role, update_role

class RolService:
    def __init__(self, db_session: Session) -> None:
        self.db = db_session
    
    async def create(self, rol_create: RoleCreate) -> Optional[RoleOut]:
        rol_out = await create_rol(self.db, rol=rol_create)
        if rol_out:
            return rol_out
        else:
            return None
    async def get_all(self ) -> Optional[List[RoleOut]]:
        rol_out_list = await get_all_roles(self.db)
        if rol_out_list:
            return rol_out_list
        else:
            return None
    async def get_one(self, rol_id: RoleId) -> Optional[RoleOut]:
        rol_out = await get_one(self.db, rol_id=rol_id)
        if rol_out:
            return rol_out
        else:
            return None
    async def remove(self, rol_id: RoleId) -> Optional[RoleRemove]:
        remove_msg = await deactivate_role(self.db, rol_id=rol_id)
        if remove_msg:
            return remove_msg
        else:
            return None
        
    async def update(self, rol_id: RoleId, update_body: RoleUpdate) -> Optional[RoleOut]:
        rol_updated =  await update_role(self.db, rol_id=rol_id, update_body= update_body)
        if rol_updated:
            return rol_updated
        else:
            return None


    
