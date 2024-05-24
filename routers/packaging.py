# from fastapi import APIRouter, HTTPException, status
# from fastapi import Depends
# from models.orm import User
# from services.authService import getCurrentUser
# from services.packagingService import PackagingService
# from dtos.packaging import PackagingOutResponse
# from db.mysql import async_session
# from datetime import datetime

# packagingRouter = APIRouter()





# @packagingRouter.get('/list/', summary="Get all packages.", response_model=PackagingOutResponse)
# async def getAllActiveVehicles(user: User = Depends(getCurrentUser)):
#     async with async_session() as session:
#         async with session.begin():
#             try:
#                 if not user:
#                     raise HTTPException(
#                         status_code=status.HTTP_403_FORBIDDEN,
#                         detail="Invalid token",
#                     )
#                 return await PackagingService(session).package()
#             except Exception as e:
#                 return PackagingOutResponse(status=False, details=f'{e}', packagingOut=[], executeAt=datetime.now())