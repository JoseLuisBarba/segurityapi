# from fastapi import APIRouter, HTTPException, status
# from fastapi import Depends
# from models.orm import User
# from services.authService import getCurrentUser
# from services.scheduleService import ScheduleService
# from dtos.schedule import ScheduleOutResponse, SchedulesResponse, ScheduleCreate
# from db.mysql import async_session
# from sqlalchemy.exc import IntegrityError
# from dtos.vehicle import VehicleOutResponse, VehicleCreate, VehicleUpdate

# scheduleRouter = APIRouter()



# @scheduleRouter.post('/createSchedule', summary="Create new schedule", response_model=ScheduleOutResponse)
# async def createVehicle(data: ScheduleCreate, user: User = Depends(getCurrentUser)):
#     async with async_session() as session:
#         async with session.begin():
#             try:
#                 if not user:
#                     raise HTTPException(
#                         status_code=status.HTTP_403_FORBIDDEN,
#                         detail="Invalid token",
#                     )
#                 return await ScheduleService(session).createSchedule(data)  
#             except IntegrityError:
#                 return ScheduleOutResponse(status=True, details='schedule was not created', scheduleOut=False)
            




# @scheduleRouter.get('/availables/', summary="Get all aviables schedules", response_model=SchedulesResponse)
# async def getAllActiveSchedules(user: User = Depends(getCurrentUser)):
#     async with async_session() as session:
#         async with session.begin():
#             try:
#                 if not user:
#                     raise HTTPException(
#                         status_code=status.HTTP_403_FORBIDDEN,
#                         detail="Invalid token",
#                     )
#                 return await ScheduleService(session).getAllSchedules()
#             except IntegrityError:
#                 return SchedulesResponse(status=False, details='error in getting schedules', schedulesOut=[])
            
            

# @scheduleRouter.get('/{id}', summary="Get schedule by Id", response_model=ScheduleOutResponse)
# async def getScheduleById(id: int, user: User = Depends(getCurrentUser)):
#     async with async_session() as session:
#         async with session.begin():
#             try:
#                 if not user:
#                     raise HTTPException(
#                         status_code=status.HTTP_403_FORBIDDEN,
#                         detail="Invalid token",
#                     )
#                 return await ScheduleService(session).getScheduleById(id)
#             except IntegrityError:
#                 return  ScheduleOutResponse(status=False, details='error in getting schedule', scheduleOut=None)




