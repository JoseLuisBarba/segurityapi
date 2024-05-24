# from fastapi import APIRouter, HTTPException, status
# from fastapi import Depends
# from models.orm import User
# from services.authService import getCurrentUser
# from services.vehicleService import VehicleService
# from dtos.vehicle import VehiclesResponse, VehicleId
# from db.mysql import async_session
# from sqlalchemy.exc import IntegrityError
# from dtos.vehicle import VehicleOutResponse, VehicleCreate, VehicleUpdate

# vehicleRouter = APIRouter()

# @vehicleRouter.post('/createVehicle', summary="Create new vehicle", response_model=VehicleOutResponse)
# async def createVehicle(data: VehicleCreate, user: User = Depends(getCurrentUser)):
#     async with async_session() as session:
#         async with session.begin():
#             try:
#                 if not user:
#                     raise HTTPException(
#                         status_code=status.HTTP_403_FORBIDDEN,
#                         detail="Invalid token",
#                     )
#                 return await VehicleService(session).createVehicle(data)  
#             except IntegrityError:
#                 raise HTTPException(
#                     status_code=status.HTTP_400_BAD_REQUEST,
#                     detail="Vehicle already exist"
#                 )

# @vehicleRouter.get('/availables/', summary="Get all aviables vehicles", response_model=VehiclesResponse)
# async def getAllActiveVehicles(user: User = Depends(getCurrentUser)):
#     async with async_session() as session:
#         async with session.begin():
#             try:
#                 if not user:
#                     raise HTTPException(
#                         status_code=status.HTTP_403_FORBIDDEN,
#                         detail="Invalid token",
#                     )
#                 return await VehicleService(session).getAllVehicles()
#             except IntegrityError:
#                 raise HTTPException(
#                     status_code=status.HTTP_400_BAD_REQUEST,
#                     detail="Error in request"
#                 )
            

# @vehicleRouter.get('/{id}', summary="Get vehicle by Id", response_model=VehicleOutResponse)
# async def getVehicleById(id: str, user: User = Depends(getCurrentUser)):
#     async with async_session() as session:
#         async with session.begin():
#             try:
#                 if not user:
#                     raise HTTPException(
#                         status_code=status.HTTP_403_FORBIDDEN,
#                         detail="Invalid token",
#                     )
#                 return await VehicleService(session).getVehicleById(id)
#             except IntegrityError:
#                 raise HTTPException(
#                     status_code=status.HTTP_400_BAD_REQUEST,
#                     detail="Error in request"
#                 )



# @vehicleRouter.put('/update/{id}/', summary="Update vehicle by id", response_model= VehicleOutResponse)
# async def updateVehicleById(id: str, data: VehicleUpdate, user: User = Depends(getCurrentUser)):
#     async with async_session() as session:
#         async with session.begin():
#             try:
#                 if not user:
#                     raise HTTPException(
#                         status_code=status.HTTP_403_FORBIDDEN,
#                         detail="Invalid token",
#                     )

#                 return await VehicleService(session).updateVehicleById(data)
              
#             except IntegrityError:
#                 raise HTTPException(
#                     status_code=status.HTTP_400_BAD_REQUEST,
#                     detail="Error in request"
#                 )