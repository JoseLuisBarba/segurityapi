# from fastapi import APIRouter, HTTPException, status
# from fastapi import Depends
# from models.orm import User
# from services.authService import getCurrentUser
# from services.caregiverService import CaregiverService
# from dtos.caregiver import CaregiverCreate, CaregiverUpdate, CaregiverCreatedResponse, CaregiversResponse, CaregiverOutResponse
# from db.mysql import async_session
# from sqlalchemy.exc import IntegrityError


# caregiverRouter = APIRouter()



# @caregiverRouter.post('/createCaregiver', summary="Create new caregiver", response_model=CaregiverCreatedResponse)
# async def createCaregiver(data: CaregiverCreate, user: User = Depends(getCurrentUser)):
#     #error in dni relation
#     async with async_session() as session:
#         async with session.begin():
#             try:
#                 if not user:
#                     raise HTTPException(
#                         status_code=status.HTTP_403_FORBIDDEN,
#                         detail="Invalid token",
#                     )
#                 return await CaregiverService(session).createCaregiver(data)  
                
#             except Exception:
#                 return CaregiverCreatedResponse(status=True, details='Caregiver was not created', caregiverOut=None)
            




# @caregiverRouter.get('/availables/', summary="Get all Caregivers.", response_model=CaregiversResponse)
# async def getAllActiveVehicles(user: User = Depends(getCurrentUser)):
#     async with async_session() as session:
#         async with session.begin():
#             try:
#                 if not user:
#                     raise HTTPException(
#                         status_code=status.HTTP_403_FORBIDDEN,
#                         detail="Invalid token",
#                     )
#                 return await CaregiverService(session).getAllCaregivers()
#             except Exception as e:
#                 return CaregiversResponse(status=False, details=f'{e}', caregiversOut=[])
            
            

# @caregiverRouter.get('/{id}', summary="Get caregiver by Id.", response_model=CaregiverOutResponse)
# async def getCaregiverById(id: str, user: User = Depends(getCurrentUser)):
#     async with async_session() as session:
#         async with session.begin():
#             try:
#                 if not user:
#                     raise HTTPException(
#                         status_code=status.HTTP_403_FORBIDDEN,
#                         detail="Invalid token",
#                     )
#                 return await CaregiverService(session).getCaregiverById(id)
#             except Exception as e:
#                 return  CaregiverOutResponse(status=False, details=f'{e}', caregiverOut=None)
            


# @caregiverRouter.put('/update/{id}', summary="Update caregiver by Id.", response_model=CaregiverOutResponse)
# async def updateCaregiverById(id: str, data: CaregiverUpdate, user: User = Depends(getCurrentUser)):
#     async with async_session() as session:
#         async with session.begin():
#             try:
#                 if not user:
#                     raise HTTPException(
#                         status_code=status.HTTP_403_FORBIDDEN,
#                         detail="Invalid token",
#                     )
#                 return await CaregiverService(session).updateCaregiverById(id, data)
#             except Exception as e:
#                 return  CaregiverOutResponse(status=False, details=f'{e}', caregiverOut=None)