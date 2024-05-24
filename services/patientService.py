# from sqlalchemy.sql import func
# from typing import Optional
# from sqlalchemy import or_
# from sqlalchemy.exc import SQLAlchemyError
# from sqlalchemy import update, insert
# from sqlalchemy.future import select
# from sqlalchemy.orm import Session
# from datetime import datetime

# from dtos.patient import PatientCreate, PatientCreated, PatientCreatedResponse, PatientsResponse
# from repository.patient import dbGetAllAviablesPatients
# from models.orm import Patient




# class PatientService:
#     def __init__(self, dbSession: Session):
#         self.dbSession = dbSession


#     async def createPatient(self, data: PatientCreate) -> Optional[PatientCreatedResponse]:
#         try:
#             caregiverIn = Patient(
#                 dni=data.dni,
#                 is_active=True,
#                 createdAt=func.now(),
#                 updatedAt=None,
#                 deletedAt=None
#             )

#             caregiverOut = PatientCreated(
#                 dni= data.dni, 
#                 createdAt= datetime.now()
#             )
            
#             self.dbSession.add(caregiverIn)
#             await self.dbSession.flush()
#             await self.dbSession.commit()
        
#             return PatientCreatedResponse(status= True, details= 'Patient was created', PatientOut=caregiverOut)
        
#         except Exception as e:
#             await self.dbSession.rollback()
#             return  PatientCreatedResponse(status=False, details=f'Error DB, Patient was not created: {e}', PatientOut=None)
        
        
#     async def getAllPatients(self) ->  PatientsResponse:
#         try:
#             patients = await dbGetAllAviablesPatients(self.dbSession)
#             if not patients:
#                 return PatientsResponse(status= False, details= 'The patients were not found', patientsOut= [])
            
#             return PatientsResponse(status= False, details= 'The patients were found', patientsOut= patients)
#         except SQLAlchemyError as e:
#             return PatientsResponse(status= False, details= f'Error DB, the patients were not found: {e}', patientsOut= [])