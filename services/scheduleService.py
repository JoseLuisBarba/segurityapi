# from sqlalchemy.sql import func
# from typing import Optional
# from sqlalchemy.exc import SQLAlchemyError
# from sqlalchemy.orm import Session
# from datetime import datetime
# from dtos.schedule import ScheduleCreate, ScheduleOut, ScheduleOutResponse, SchedulesResponse
# from repository.schedule import getScheduleById, getAllAviablesSchedules
# from models.orm import Schedule
# from sqlalchemy.sql import func
# from typing import List

# class ScheduleService:

#     def __init__(self, dbSession: Session):

#         self.dbSession = dbSession

#     async def createSchedule(self, schedule: ScheduleCreate) -> Optional[ScheduleOutResponse]:
#         try:
#             scheduleIn = Schedule(
#                 id= schedule.id,
#                 start_time= schedule.start_time,
#                 leaving_time= schedule.leaving_time,
#                 is_active= True,
#                 createdAt= func.Now(),
#                 updatedAt= None,
#                 deletedAt= None
#             )

#             self.dbSession.add(scheduleIn)
#             await self.dbSession.flush()

#             scheduleOut = ScheduleOut(
#                 id= schedule.id,
#                 start_time= schedule.start_time,
#                 leaving_time= schedule.leaving_time,
#                 is_active= True ,
#                 createdAt= datetime.now()
#             )
        

#             return ScheduleOutResponse(status=True, details='schedule created', scheduleOut=scheduleOut)
        
#         except SQLAlchemyError as e:
#             print(e)
#             return  ScheduleOutResponse(status=True, details='schedule was not created', scheduleOut=False)
        

#     async def getAllSchedules(self) ->  SchedulesResponse:
#         try:
#             schedules = await getAllAviablesSchedules(self.dbSession)

#             if not schedules:
#                 return SchedulesResponse(status=False, details='error in getting schedules', schedulesOut=[])
            
#             schedulesResponse: List[ScheduleOut] = []

#             for schedule in schedules:
#                 schedulesResponse.append(
#                     ScheduleOut(
#                         id= schedule.id,
#                         start_time= schedule.start_time,
#                         leaving_time= schedule.leaving_time,
#                         is_active= schedule.is_active,
#                         createdAt= schedule.createdAt
#                     )
#                 )

#             return SchedulesResponse(status=True, details='The schedules were get', schedulesOut=schedulesResponse)
        
#         except SQLAlchemyError as e:
#             print(e)
#             return SchedulesResponse(status=False, details='error in getting schedules', schedulesOut=[])
        


#     async def getScheduleById(self, id: int) -> Optional[ScheduleOutResponse]:
#         try:

#             schedule = await getScheduleById(self.dbSession, id)

#             if not schedule:
#                 return  ScheduleOutResponse(status=False, details='error in getting schedule', scheduleOut=None)
            
#             scheduleOut = ScheduleOut(
#                 id= schedule.id, 
#                 start_time= schedule.start_time, 
#                 leaving_time= schedule.leaving_time, 
#                 is_active= schedule.is_active, 
#                 createdAt= schedule.createdAt
#             )

#             return ScheduleOutResponse(status=True, details='The schedule was get', scheduleOut=scheduleOut)
        
#         except SQLAlchemyError as e:
#             print(e)
#             return  ScheduleOutResponse(status=False, details='error in getting schedule', scheduleOut=None)
        


