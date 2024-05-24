# from models.orm import Schedule
# from typing import List
# from dtos.schedule import ScheduleCreate, ScheduleOut, ScheduleOutResponse
# from sqlalchemy.orm import Session
# from sqlalchemy.future import select
# from sqlalchemy import or_, and_, update
# from datetime import datetime


# async def getAllAviablesSchedules(db: Session) -> List[Schedule]:
#     query = (
#          select(Schedule).where(Schedule.is_active == True)
#     )
#     schedule = await db.scalars(query)
#     return schedule


# async def getScheduleById(db: Session, identifier: int) -> Schedule:
#      query = ( 
#          select(Schedule)
#          .where(Schedule.id == identifier)
#          .limit(1)
#      )
#      schedule = await db.scalar(query)
#      return schedule


