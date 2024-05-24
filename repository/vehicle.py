# from models.orm import Vehicle
# from typing import List
# from dtos.vehicle import VehicleUpdate
# from sqlalchemy.orm import Session
# from sqlalchemy.future import select
# from sqlalchemy import or_, and_, update
# from datetime import datetime


# async def getAllActiveVehicles(db: Session) -> List[Vehicle]:
#     query = (
#          select(Vehicle).where(Vehicle.is_active == True)
#     )
#     vehicles = await db.scalars(query)
#     return vehicles

# async def getVehicleById(db: Session, identifier: str) -> Vehicle:
#      query = ( 
#          select(Vehicle)
#          .where(Vehicle.reg_num == identifier)
#          .limit(1)
#      )
#      vehicle = await db.scalar(query)
#      return vehicle

# async def updateVehicleById(db: Session, data: VehicleUpdate) -> Vehicle:
#      try:
#           query = ( 
#                update(Vehicle). 
#                where(Vehicle.reg_num == data.reg_num).
#                values(
#                     capacity= data.capacity,
#                     average_speed= data.average_speed,
#                     freight_km= data.freight_km ,
#                     lat= data.lat,
#                     lng= data.lng,
#                     is_active= data.is_active,
#                     updatedAt= datetime.now(),
#                )
#           )
#           await db.execute(query)

#           query = ( 
#                select(Vehicle)
#                .where(Vehicle.reg_num == data.reg_num)
#                .limit(1)
#           )

#           vehicle = await db.scalar(query)

#           db.commit()

#           return vehicle
     
#      except Exception as e:
#         db.rollback()
#         raise e