# from typing import Optional,List
# from sqlalchemy.exc import SQLAlchemyError
# from sqlalchemy.orm import Session
# from sqlalchemy.sql import func
# from datetime import datetime

# from dtos.packaging import PackagingOut, PackagingOutResponse
# from services.caregiverService import CaregiverService
# from services.vehicleService import VehicleService
# from core.algorithms import bin_packing_heuristic



# class PackagingService:

#     def __init__(self, dbSession: Session):

#         self.dbSession = dbSession

#     async def package(self ) -> Optional[PackagingOutResponse]:
#         try:
#             caregiversResp = await CaregiverService(self.dbSession).getAllCaregivers()
#             vehiclesResp = await VehicleService(self.dbSession).getAllVehicles()

#             if not caregiversResp.status or not vehiclesResp.status:
#                 return PackagingOutResponse(status=True, details='Error in packaging: data not faund.', packagingOut=[],  executeAt=datetime.now())
            
#             caregivers = caregiversResp.caregiversOut
#             vehicles = vehiclesResp.vehiclesOut
#             packagingOutList = await bin_packing_heuristic(caregivers, vehicles)

#             if len(packagingOutList) < 1:
#                 return PackagingOutResponse(status=True, details='Error in packaging: empty list', packagingOut=[],  executeAt=datetime.now())

#             return PackagingOutResponse(status=True, details='packaging is done', packagingOut=packagingOutList,  executeAt=datetime.now())
        
#         except SQLAlchemyError as e:
#             return PackagingOutResponse(status=True, details='Error in packaging: {e}', packagingOut=[],  executeAt=datetime.now())



    
