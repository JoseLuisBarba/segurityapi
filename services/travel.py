# from models.orm import  Travel
# from dtos.travel import TravelCreate, TravelOut, TravelOutResponse

# from sqlalchemy.exc import SQLAlchemyError
# from sqlalchemy.orm import Session
# from sqlalchemy.sql import func
# from datetime import datetime, date
# from typing import List, Optional




# class TravelService:

#     def __init__(self, dbSession: Session):

#         self.dbSession = dbSession

#     async def createTravel(self, travel: TravelCreate) -> Optional[TravelOutResponse]:
#         try:

#             travelIn = Travel(
#                 vehicle_id= travel.vehicle_id, 
#                 schedule_id= travel.schedule_id,
#                 is_active= True,
#                 createdAt= datetime.now(),
#                 updatedAt= None,
#                 deletedAt= None
#             )

#             self.dbSession.add(travelIn)

#             await self.dbSession.flush()
#             await self.dbSession.commit()

#             travelOut = TravelOut(
#                 vehicle_id= travel.vehicle_id, 
#                 schedule_id= travel.schedule_id, 
#                 createdAt= datetime.now(), 
#                 dateTravel= datetime.now().date()
#             )
#             return TravelOutResponse(status=True, details=f'Travel was not created', travelOut=travelOut)
        
#         except SQLAlchemyError as e:
#             await self.dbSession.rollback()
#             return TravelOutResponse(status=False, details=f'Error DB, Caregiver was not created: {e}', travelOut=None)
            
        
