# from fastapi import APIRouter, HTTPException, status
# from fastapi import Depends


# #from sqlalchemy.exc import IntegrityError

# from db.mysql import async_session
# from models.orm import User
# from dtos.patient import PatientOutResponse, PatientCreate, PatientCreatedResponse, PatientsResponse
# from services.authService import getCurrentUser
# from services.patientService import PatientService





# patientRouter = APIRouter()




# @patientRouter.post('/createPatient', summary="Create new patient", response_model=PatientCreatedResponse)
# async def createPatient(data: PatientCreate, user: User = Depends(getCurrentUser)):
#     #error in dni relation
#     async with async_session() as session:
#         async with session.begin():
#             try:
#                 if not user:
#                     raise HTTPException(
#                         status_code=status.HTTP_403_FORBIDDEN,
#                         detail="Invalid token",
#                     )
#                 return await PatientService(session).createPatient(data)
#             except Exception as e:
#                 return  PatientCreatedResponse(status=False, details=f'Error DB, Patient was not created: {e}', PatientOut=None)
            

# @patientRouter.get('/availablesPatients/', summary="Get all patients.", response_model=PatientsResponse)
# async def getAllActivePatients(user: User = Depends(getCurrentUser)):
#     async with async_session() as session:
#         async with session.begin():
#             try:
#                 if not user:
#                     raise HTTPException(
#                         status_code=status.HTTP_403_FORBIDDEN,
#                         detail="Invalid token",
#                     )
#                 return await PatientService(session).getAllPatients()
#             except Exception as e:
#                 return PatientsResponse(status= False, details= f'{e}', patientsOut= [])