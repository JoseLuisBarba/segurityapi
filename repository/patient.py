# from sqlalchemy.orm import Session
# from sqlalchemy.future import select 
# from sqlalchemy import or_, and_, update
# from typing import List, Optional
# from datetime import datetime

# from models.orm import  User, Patient
# from dtos.patient import PatientOut

# async def dbGetAllAviablesPatients(db: Session) -> Optional[List[PatientOut]]:
#     try:
#         query = (
#             select(Patient, User)
#             .where(Patient.is_active == True)
#             .join(User, Patient.dni == User.dni)
#         )
        
#         patients = await db.execute(query)

#         patientsResponse: List[PatientOut] = []

#         for patient, user in patients:
#             patientsResponse.append(PatientOut(
#                 dni= patient.dni,
#                 email= user.email,
#                 name= user.name,
#                 lastname= user.lastname,
#                 is_active= user.is_active,
#                 phone= user.phone,
#                 birthdate= user.birthdate,
#                 userCreatedAt= user.createdAt,
#                 patientCreatedAt= patient.createdAt
#             ))

#         return patientsResponse
#     except Exception as e:
#         return None


# # async def dbGetCaregiverById(db: Session, identifier: str) -> List[CaregiverOut]:
# #     query = (
# #          select(Caregiver, User)
# #          .where( and_(Caregiver.is_active == True, Caregiver.dni == identifier))
# #          .join(User, Caregiver.dni == User.dni)
# #          .limit(1)

# #     )
    
# #     caregivers = await db.execute(query)

# #     caregiversResponse: List[CaregiverOut] = []

# #     for caregiver, user in caregivers:
# #         caregiversResponse.append(
# #             CaregiverOut(
# #                 dni= caregiver.dni, 
# #                 skill= caregiver.skill, 
# #                 schedule_id= caregiver.schedule_id, 
# #                 email= user.email, 
# #                 name= user.name, 
# #                 lastname= user.lastname, 
# #                 is_active= user.is_active, 
# #                 phone= user.phone, 
# #                 birthdate= user.birthdate, 
# #                 createdAt= user.createdAt
# #             )
# #         )

# #     return caregiversResponse




# # async def dbUpdateCaregiverById(db: Session, id: str, data: CaregiverUpdate) -> Optional[List[CaregiverOut]]:
# #     try:
# #         query = ( 
# #             update(Caregiver). 
# #             where(Caregiver.dni == id).
# #             values(             
# #                 schedule_id= data.schedule_id,
# #                 skill= data.skill,
# #                 is_active= data.is_active,
# #                 updatedAt= datetime.now()
# #             )
# #         )

# #         await db.execute(query)

# #         query = (
# #             select(Caregiver, User)
# #             .where( and_(Caregiver.is_active == True, Caregiver.dni == id))
# #             .join(User, Caregiver.dni == User.dni)
# #             .limit(1)

# #         )
    
# #         caregivers = await db.execute(query)

# #         caregiversResponse: List[CaregiverOut] = []

# #         for caregiver, user in caregivers:
# #             caregiversResponse.append(
# #                 CaregiverOut(
# #                     dni= caregiver.dni, 
# #                     skill= caregiver.skill, 
# #                     schedule_id= caregiver.schedule_id, 
# #                     email= user.email, 
# #                     name= user.name, 
# #                     lastname= user.lastname, 
# #                     is_active= user.is_active, 
# #                     phone= user.phone, 
# #                     birthdate= user.birthdate, 
# #                     createdAt= user.createdAt
# #                 )
# #             )

# #         await db.commit()

# #         return caregiversResponse
     
# #     except Exception as e:
# #         await db.rollback()

# #         return None