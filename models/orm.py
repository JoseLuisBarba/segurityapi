# from sqlalchemy import Column, ForeignKey, Integer, Boolean, Date, String, DateTime,  Double, Time, Text
# from sqlalchemy.orm import relationship
# from sqlalchemy.sql import func
# from datetime import datetime
# from db.mysql import  Base


# # segurity ai
# class Rol(Base):
    
#     __tablename__ = "rol"
    
#     id = Column(Integer, primary_key=True)
#     name = Column(String(20), unique=True ,nullable=False)
#     description = Column(String(100), nullable=True)
#     is_active = Column(Boolean, default=True)
#     createdAt = Column(DateTime, server_default= func.now())
#     updatedAt = Column(DateTime)
#     deletedAt = Column(DateTime)




# # segurity ai
# class User(Base):
    
#     __tablename__ = "user"

#     dni = Column(String(20), primary_key=True)
#     email = Column(String(50), unique=True, nullable=False)
#     password = Column(String(50), nullable=False)

#     name = Column(String(20), nullable=False)
#     lastname = Column(String(20), nullable=False)
#     phone = Column(String(20), nullable=False)
#     birthdate = Column(Date, nullable=False)
#     is_active = Column(Boolean, default=True)
#     createdAt = Column(DateTime, server_default= func.now())
#     updatedAt = Column(DateTime)
#     deletedAt = Column(DateTime)

#     #relationships
#     admin = relationship('Admin', uselist=False, back_populates='user')
#     caregiver = relationship('Caregiver', uselist=False, back_populates='user')
#     patient = relationship('Patient', uselist=False, back_populates='user')





# #@relationship
# class UserRol(Base):
    
#     __tablename__ = "user_rol"

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(String(20), ForeignKey('user.dni'), nullable=False)
#     rol_id = Column(Integer, ForeignKey('rol.id'), nullable=False)
#     is_active = Column(Boolean, default=True)
#     createdAt = Column(DateTime, server_default= func.now())
#     updatedAt = Column(DateTime)
#     deletedAt = Column(DateTime)


#     #relationships
#     user = relationship('User')
#     rol = relationship('Rol')


# class Admin(Base):
#     __tablename__ = "admin" 

#     dni = Column(String(20), ForeignKey('user.dni'), primary_key=True, nullable=False)

#     is_active = Column(Boolean, default=True)
#     createdAt = Column(DateTime, server_default= func.now())
#     updatedAt = Column(DateTime)
#     deletedAt = Column(DateTime)

#     #relationship 
#     user = relationship('User', uselist=False, back_populates='admin')




# class Schedule(Base):
#     __tablename__ = "schedule"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     start_time = Column(Time, nullable=False)
#     leaving_time = Column(Time, nullable=False)

#     is_active = Column(Boolean, default=True)
#     createdAt = Column(DateTime, server_default= func.now())
#     updatedAt = Column(DateTime)
#     deletedAt = Column(DateTime)


# class Caregiver(Base):
#     __tablename__ = "caregiver" 

#     dni = Column(String(20), ForeignKey('user.dni'), primary_key=True, nullable=False)
#     skill = Column(Double(), nullable=False)

#     schedule_id = Column(Integer, ForeignKey('schedule.id'), nullable=False)

#     is_active = Column(Boolean, default=True)
#     createdAt = Column(DateTime, server_default= func.now())
#     updatedAt = Column(DateTime)
#     deletedAt = Column(DateTime)

#     #relationship 
#     schedule = relationship('Schedule')
#     user = relationship('User', uselist=False, back_populates='caregiver')


# class Vehicle(Base):

#     __tablename__ = "vehicle"

#     reg_num = Column(String(20), primary_key=True)
#     capacity = Column(Integer, nullable=False)
#     average_speed = Column(Double, nullable=False)
#     freight_km = Column(Double, nullable=False)

#     lat = Column(Double(), nullable=False)
#     lng = Column(Double(), nullable=False)

#     is_active = Column(Boolean, default=True)
#     createdAt = Column(DateTime, server_default= func.now())
#     updatedAt = Column(DateTime)
#     deletedAt = Column(DateTime)


# class Patient(Base):
    
#     __tablename__ = "patient"

#     dni = Column(String(20), ForeignKey('user.dni'), primary_key=True, nullable=False)

#     is_active = Column(Boolean, default=True)
#     createdAt = Column(DateTime, server_default= func.now())
#     updatedAt = Column(DateTime)
#     deletedAt = Column(DateTime)

#     #relationship 
#     user = relationship('User', uselist=False, back_populates='patient')


# class Travel(Base):

#     __tablename__ = "travel"

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     vehicle_id = Column(String(20), ForeignKey('vehicle.reg_num'), nullable=False)
#     schedule_id = Column(Integer, ForeignKey('schedule.id'), nullable=False)


#     is_active = Column(Boolean, default=True)
#     createdAt = Column(DateTime, server_default= func.now())
#     updatedAt = Column(DateTime)
#     deletedAt = Column(DateTime)

#     #relationship 
#     vehicle = relationship('Vehicle')
#     schedule = relationship('Schedule')



# class Cite(Base):


#     __tablename__ = "cite"


#     id = Column(Integer, primary_key=True, autoincrement=True)

#     travel_id = Column(Integer, ForeignKey('travel.id'), nullable=False)
#     patient_id = Column(Integer, ForeignKey('patient.dni'), nullable=False)

#     skill = Column(Double(), nullable=False)

#     cite_date = Column(Date, nullable=False)

#     lat = Column(Double(), nullable=False)
#     lng = Column(Double(), nullable=False)

#     arrival_time = Column(Time, nullable=False)
#     departure_time = Column(Time, nullable=False)
#     service_time = Column(Time, nullable=False)
#     wait_time = Column(Time, nullable=False)

#     body = Column(String(250), nullable=False)

#     is_active = Column(Boolean, default=True)
#     createdAt = Column(DateTime, server_default= func.now())
#     updatedAt = Column(DateTime)
#     deletedAt = Column(DateTime)
    
#     #relationship 
#     travel = relationship('Travel')
#     patient = relationship('Patient')



# class CaregiverTravel(Base):

#     __tablename__ = "caregiver_travel"

#     id = Column(Integer, primary_key=True, autoincrement=True)

#     travel_id = Column(Integer, ForeignKey('travel.id'), nullable=False)
#     caregiver_id = Column(String(20), ForeignKey('caregiver.dni'), nullable=False )

#     is_active = Column(Boolean, default=True)
#     createdAt = Column(DateTime, server_default= func.now())
#     updatedAt = Column(DateTime)
#     deletedAt = Column(DateTime)

#     #relationship 
#     travel = relationship('Travel')
#     caregiver = relationship('Caregiver')






