# from sqlalchemy.sql import func
# from typing import Optional
# from sqlalchemy import or_
# from sqlalchemy.exc import SQLAlchemyError
# from sqlalchemy import update
# from sqlalchemy.future import select
# from sqlalchemy.orm import Session
# from datetime import datetime
# from dtos.vehicle import VehicleCreate, VehicleOutResponse, VehicleOut, VehiclesResponse, VehicleUpdate
# from repository.vehicle import getAllActiveVehicles, getVehicleById, updateVehicleById
# from models.orm import Vehicle
# from sqlalchemy.sql import func
# from typing import List

# class VehicleService:

#     def __init__(self, dbSession: Session):
#         self.dbSession = dbSession

#     async def createVehicle(self, vehicle: VehicleCreate) -> Optional[VehicleOutResponse]:
#         try:

            
#             vehicleIn = Vehicle(
#                 reg_num= vehicle.reg_num,
#                 capacity= vehicle.capacity,
#                 average_speed= vehicle.average_speed,
#                 freight_km= vehicle.freight_km,
#                 lat= vehicle.lat,
#                 lng= vehicle.lng,
#                 is_active= True,
#                 createdAt= func.now(),
#                 updatedAt= None,
#                 deletedAt= None,
#             )

#             self.dbSession.add(vehicleIn)

#             await self.dbSession.flush()
            
#             vehicleOut = VehicleOut(
#                 reg_num= vehicle.reg_num,
#                 capacity= vehicle.capacity,
#                 average_speed= vehicle.average_speed, 
#                 freight_km= vehicle.freight_km, 
#                 lat= vehicle.lat, 
#                 lng= vehicle.lng,
#                 createdAt= datetime.now(),
#                 is_active=True
#             )

#             return VehicleOutResponse(status=True, vehicleOut=vehicleOut)
        
        
    
#         except SQLAlchemyError as e:
#             print(e)
#             return  VehicleOutResponse(status=False, vehicleOut=None)
        

#     async def getAllVehicles(self) ->  VehiclesResponse:
#         try:
#             vehicles = await getAllActiveVehicles(self.dbSession)

#             if not vehicles:
#                 return VehiclesResponse(status=False, vehiclesOut=[])
            
#             vehiclesResponse: List[VehicleOut] = []

#             for vehicle in vehicles:
#                 vehiclesResponse.append(VehicleOut(
#                     reg_num= vehicle.reg_num, 
#                     capacity= vehicle.capacity,
#                     average_speed= vehicle.average_speed, 
#                     freight_km= vehicle.freight_km, 
#                     lat= vehicle.lat, 
#                     lng= vehicle.lng,
#                     is_active= vehicle.is_active, 
#                     createdAt= vehicle.createdAt
#                 ))

#             return VehiclesResponse(status=True, vehiclesOut=vehiclesResponse)

        
#         except SQLAlchemyError as e:
#             print(e)
#             return  VehiclesResponse(status=False, vehiclesOut=[])
        


#     async def getVehicleById(self, id) -> Optional[VehicleOutResponse]:
#         try:

#             vehicle = await getVehicleById(self.dbSession, id)

#             if not vehicle:
#                 return  VehicleOutResponse(status=False, vehicleOut=None)
            
#             vehicleOut = VehicleOut(
#                 reg_num= vehicle.reg_num,
#                 capacity= vehicle.capacity,
#                 average_speed= vehicle.average_speed, 
#                 freight_km= vehicle.freight_km, 
#                 lat= vehicle.lat, 
#                 lng= vehicle.lng,
#                 createdAt= vehicle.createdAt,
#                 is_active=True
#             )
#             return VehicleOutResponse(status=True, vehicleOut=vehicleOut)
        
#         except SQLAlchemyError as e:
#             print(e)
#             return  VehicleOutResponse(status=False, vehicleOut=None)
        
#     async def updateVehicleById(self, newData: VehicleUpdate) -> Optional[VehicleOutResponse]:
#         try:

#             vehicle = await updateVehicleById(self.dbSession, newData)

#             if not vehicle:
#                 return  VehicleOutResponse(status=False, vehicleOut=None)
            
#             vehicleOut = VehicleOut(
#                 reg_num= vehicle.reg_num,
#                 capacity= vehicle.capacity,
#                 average_speed= vehicle.average_speed, 
#                 freight_km= vehicle.freight_km, 
#                 lat= vehicle.lat, 
#                 lng= vehicle.lng,
#                 createdAt= vehicle.createdAt,
#                 is_active=True
#             )
#             return VehicleOutResponse(status=True, vehicleOut=vehicleOut)
        
#         except SQLAlchemyError as e:
#             print(e)
#             return  VehicleOutResponse(status=False, vehicleOut=None)       
    

