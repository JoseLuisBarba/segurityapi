from fastapi import APIRouter
from routers import role
from routers import user_rol
from routers import users
from routers import auth2





router = APIRouter()

router.include_router(auth2.router, prefix='/auth', tags=["auth"])
router.include_router(role.route, prefix="/rol", tags=["rol"])
router.include_router(users.router, prefix="/user", tags=["user"])
router.include_router(user_rol.router, prefix="/role-management", tags=["role-management"])






