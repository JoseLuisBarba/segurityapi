from models.patient_model import Patient
from models.location_model import Location
from models.travel_model import Travel
from repository.metrics.euclidean_distance import euclidean_distance


#stochastic
import random

# data structures
from typing import List, Tuple
from min_max_heap import MinMaxHeap



class Vehicle:
    def __init__(
            self, 
            id: int, MAX_Q: float, MIN_Q: float, 
            WARE_HOUSE: Patient,
            VD: float, FLETE: float, 
            CC: float, EM: float
        ) -> None:
        
        self.id: int = id
        self.MAX_Q: float = MAX_Q
        self.MIN_Q: float = MIN_Q 
        self.q: float = MAX_Q
        self.location: Location = WARE_HOUSE.loc 
        self.WARE_HOUSE: Patient = WARE_HOUSE
        self.VD: float = VD
        self.FLETE: float = FLETE
        self.t: float = self.WARE_HOUSE.tw.a
        self.CC: float = CC
        self.EM: float = EM
        self.is_assigned: bool = False
        self.total_distance: float = 0

        # agregamos al almacen como primer nodo visitado
        self.service_route: List[Tuple[Patient,Travel]] = [ ( self.WARE_HOUSE, Travel(
            is_warehouse= True,
            vehicle_id= self.id,
            patient_id= self.WARE_HOUSE._id,
            travel_distance= 0,
            travel_time= self.t,
            arrival_time= self.t,
            wait_time= 0,
            service_time= 0,
            departure_time= self.t,
            total_distance= self.total_distance,
            capacity= self.MAX_Q,
            loc_x= self.WARE_HOUSE.loc.x,
            loc_y= self.WARE_HOUSE.loc.y
        )),]
            
 
    def try_attend_patient(self, new_patient: Patient) -> bool:
        # si aun no se ha atendido a nadie, entonces, atendemos al paciente sin discriminacion
        if len(self.service_route) == 1:
            return self.attended_patient(patient= new_patient) or self.attended_patient_force(patient= new_patient)
        
        shuffled: list[int] = list(
            range(1, len(self.service_route))
        )

        random.shuffle(shuffled)

        for i in shuffled:

            vehicle: Vehicle = Vehicle(
                id= self.id, 
                MAX_Q= self.MAX_Q, 
                MIN_Q= self.MIN_Q, 
                WARE_HOUSE= self.WARE_HOUSE, 
                VD= self.VD, 
                FLETE= self.FLETE, 
                CC= self.CC,
                EM= self.EM
            ) # build a vehicle

            vehicle.hard_reset_vehicle() # initial status
            index: int = i # get current index
            should_use_route: bool = True
            new_patient.isAttended = False

            for e, (curr_patient, curr_travel) in enumerate(self.service_route[1:]):
                if (e + 1) == index:
                    if not vehicle.attended_patient(patient= new_patient):
                        if not vehicle.attended_patient_force(patient= new_patient):
                            should_use_route = False
                            break
                if not vehicle.attended_patient(patient=curr_patient):
                    if not vehicle.attended_patient_force(patient=curr_patient):
                        should_use_route = False
                        break
            if not should_use_route or not new_patient.isAttended:
                new_patient.isAttended = False
                continue

            self.service_route = vehicle.service_route[:]
            self.t = vehicle.t
            self.q = vehicle.q
            self.total_distance = vehicle.total_distance
            return True
        return False        


    def attended_patient(self, patient: Patient) -> bool: 

        # calculamos la distancia al paciente
        dist: float = euclidean_distance()(loc1=self.location, loc2=patient.loc)
        travel_time: float = dist / self.VD
        arrival_time: float =  self.t  + travel_time
        time_forecast: float = self.t + travel_time + patient.serviceTime


        # el vehiculo debe estar dentro de la ventana de tiempo del paciente
        if not(patient.tw.check_status(x=time_forecast)):
            return False
        
        # el vehiculo debe satisfacer la demanda
        q_forecast: float = self.q - patient.demand
        if not(q_forecast >= self.MIN_Q):
            return False
    
        #el vehiculo debe contar con tiempo en volver al almacen
        dist_wh: float = euclidean_distance()(loc1= patient.loc, loc2= self.WARE_HOUSE.loc)
        travel_time_wh: float = dist_wh / self.VD # tiempo del posible paciente al almacen
        time_forecast_wh: float = time_forecast + travel_time_wh
        if not(time_forecast_wh <= self.WARE_HOUSE.tw.b):
            return False
        
        # si se cumplen las restricciones
        self.location = patient.loc # se asigna su nueva ubicacion
        self.q = q_forecast # se actualiza su capacidad actual
        self.t = time_forecast  # se actualiza su tiempo actual de viaje  
        self.total_distance += dist # se actualiza su distancia total actual de viaje 

        patient.attended_by(self.id) #el paciente es atendido por el vehiculo

        # resumen del viaje
        travel: Tuple[Patient,Travel] = ( patient, Travel(
            is_warehouse= False,
            vehicle_id= self.id,
            patient_id= patient._id,
            travel_distance= dist,
            travel_time= travel_time,
            arrival_time= arrival_time,
            wait_time= 0,
            service_time= patient.serviceTime,
            departure_time= time_forecast,
            total_distance= self.total_distance,
            capacity= self.q,
            loc_x=  patient.loc.x,
            loc_y= patient.loc.y
        )) # se agrega el paciente a su ruta de viaje


        self.service_route.append(travel)
        # si ya no hay capacidad se retorna al almacen

        if self.q < self.MIN_Q:
            self.return_warehouse()

        return True
    

    def return_warehouse(self) -> None: # check?
        if not(self.WARE_HOUSE.loc.is_equal(other=self.location)):
            self.q = self.MAX_Q # se resetea su capacidad actual a su maximo
            dist_wh: float = euclidean_distance()(loc1= self.location, loc2= self.WARE_HOUSE.loc) #calcular distancia al almacen 
            travel_time_wh: float = dist_wh / self.VD # tiempo de la posicion actual del vehiculo al almacen
            self.t +=  travel_time_wh #actualizamos el tiempo total mas el tiempo de retorno
            self.total_distance += dist_wh # actualizamos distancia total + las distancia de retorno
            self.location = self.WARE_HOUSE.loc # actualizamos ubicacion
            
            #resumen del viaje

            travel: Tuple[Patient,Travel] = ( self.WARE_HOUSE, Travel(
                is_warehouse= True,
                vehicle_id= self.id,
                patient_id= self.WARE_HOUSE._id,
                travel_distance= dist_wh,
                travel_time= travel_time_wh,
                arrival_time= self.t,
                wait_time= 0,
                service_time= self.WARE_HOUSE.serviceTime,
                departure_time= 0,
                total_distance= self.total_distance,
                capacity= self.q,
                loc_x=  self.WARE_HOUSE.loc.x,
                loc_y= self.WARE_HOUSE.loc.y
            )) # se agrega el paciente a su ruta de viaje
            self.service_route.append(travel)
            

    def attended_patient_force(self, patient: Patient) -> bool:
        # calculamos la distancia al paciente
        dist: float = euclidean_distance()(loc1=self.location, loc2=patient.loc)
        travel_time: float = dist / self.VD
        arrival_time: float = self.t + travel_time 
        

        # si el vehiculo llega antes de la hora de atencion del cliente, entonces debe esperar
        if not(arrival_time < patient.tw.a): 
            return False

        wait_time: float = patient.tw.a - arrival_time 
        time_forecast: float = arrival_time + wait_time + patient.serviceTime

        # si el vehiculo no cumple con la hora de salida
        if not(time_forecast <= patient.tw.b):
            return False

        # el vehiculo debe satisfacer la demanda
        q_forecast: float = self.q - patient.demand
        if not(q_forecast > self.MIN_Q):
            return False
        
        #el vehiculo debe contar con tiempo en volver al almacen
        dist_wh: float = euclidean_distance()(loc1= patient.loc, loc2= self.WARE_HOUSE.loc)
        travel_time_wh: float = dist_wh / self.VD # tiempo del posible paciente al almacen
        time_forecast_wh: float = time_forecast + travel_time_wh
        if not(time_forecast_wh <= self.WARE_HOUSE.tw.b):
            return False


        # si se cumplen las restricciones
        self.location = patient.loc # se asigna su nueva ubicacion
        self.q = q_forecast # se actualiza su capacidad actual
        self.t = time_forecast # se actualiza su tiempo actual de viaje  
        self.total_distance += dist # se actualiza su distancia total actual de viaje

        patient.attended_by(self.id)  #atendemos al paciente


        travel: Tuple[Patient,Travel] = ( patient, Travel(
            is_warehouse= False,
            vehicle_id= self.id,
            patient_id= patient._id,
            travel_distance= dist,
            travel_time= travel_time,
            arrival_time= arrival_time,
            wait_time= wait_time,
            service_time= patient.serviceTime,
            departure_time= time_forecast,
            total_distance= self.total_distance,
            capacity= q_forecast,
            loc_x=  patient.loc.x,
            loc_y= patient.loc.y
        )) # se agrega el paciente a su ruta de viaje
        

        self.service_route.append(travel) # se agrega el paciente a su ruta de viaje

        return True
    

    def compute_priority(self, patient: Patient) -> float:
        patient_dist: float = euclidean_distance()(loc1=self.location, loc2=patient.loc)
        warehouse_dist: float = euclidean_distance()(loc1= patient.loc, loc2= self.WARE_HOUSE.loc)
        return patient_dist + warehouse_dist



    # correguir 
    def hard_reset_vehicle(self,) -> None:
        """reset vehicle status
        """
        self.q = self.MAX_Q # reiniciamos su capacidad
        self.location = self.WARE_HOUSE.loc # se regresa a su almacen
        self.t = self.WARE_HOUSE.tw.a # el tiempo de viaje inicial
        self.total_distance = 0
        self.service_route = [ ( self.WARE_HOUSE, Travel(
            is_warehouse= True,
            vehicle_id= self.id,
            patient_id= self.WARE_HOUSE._id,
            travel_distance= 0,
            travel_time= self.t,
            arrival_time= self.t,
            wait_time= 0,
            service_time= self.WARE_HOUSE.tw.a,
            departure_time= self.t,
            total_distance= self.total_distance,
            capacity= self.MAX_Q,
            loc_x= self.WARE_HOUSE.loc.x,
            loc_y= self.WARE_HOUSE.loc.y
        )),]


    def reset_vehicle_used(self)-> None:
        if self.service_route[0] == self.service_route[1]:
            self.hard_reset_vehicle()


    def remove_patient(self, patient: Patient):

        # remove
        patient_index = [ route_node[0] for route_node in self.service_route].index(patient)
        del self.service_route[patient_index] 
        self.q += patient.demand
        patient.not_attended()

        # conflicts resolve
        for i, (curr_patient, curr_travel) in enumerate(self.service_route[patient_index : ]):

            prev_patient: Patient
            prev_travel: Travel
            prev_patient, prev_travel = self.service_route[patient_index + i - 1]

            # summary: distance
            travel_dist: float = euclidean_distance()(loc1=prev_patient.loc, loc2=curr_patient.loc)
            total_dist: float = prev_travel.total_distance + travel_dist
            # summary: travel
            travel_time: float = travel_dist / self.VD
            arrival_time: float = prev_travel.departure_time + travel_time 
            wait_time: float = curr_patient.tw.a - arrival_time
            service_time: float = curr_patient.serviceTime
            departure_time: float = arrival_time + wait_time + service_time
            # summary: demand
            capacity: float = prev_travel.capacity - curr_patient.demand


            travel: Travel = Travel(
                is_warehouse= curr_patient.isWarehouse, 
                vehicle_id= self.id, 
                patient_id= curr_patient._id, 
                travel_distance= travel_dist, 
                travel_time= travel_time, 
                arrival_time= arrival_time,
                wait_time=  wait_time, 
                service_time= service_time, 
                departure_time= departure_time, 
                total_distance= total_dist, 
                capacity= capacity, 
                loc_x= curr_patient.loc.x, 
                loc_y= curr_patient.loc.y, 
            ) 

            self.service_route[patient_index + i] = (curr_patient, travel)


        next_patient: Patient = self.service_route[patient_index][0] 
        prev_patient: Patient = self.service_route[patient_index - 1][0]
        self.total_distance -= ( euclidean_distance()(loc1= prev_patient.loc, loc2=patient.loc) + euclidean_distance()(loc1=patient.loc, loc2=next_patient.loc))
        self.total_distance +=  euclidean_distance()(loc1= prev_patient.loc, loc2=next_patient.loc) 
        self.reset_vehicle_used()


    #@test
    #@check  to_json method    
    def to_json(self) -> dict:
        travel_route = [ travel[1].to_json() for travel in self.service_route]
        return {
            "id": self.id,
            "MAX_Q": self.MAX_Q,
            "MIN_Q": self.MIN_Q,
            "q": self.q,
            "x_location": self.location.x,
            "y_location": self.location.y,
            "WARE_HOUSE_id": self.WARE_HOUSE._id,
            "VD": self.VD,
            "FLETE": self.FLETE,
            "t": self.t,
            "CC": self.CC,
            "EM": self.EM,
            "is_assigned": self.is_assigned,
            "total_distance": self.total_distance,
            "service_route": travel_route if travel_route else []
        }





    

        

        

        

        

"""
https://json-generator.com/
[
  '{{repeat(1, 3)}}',
  {
    id: '{{objectId()}}',
    MAX_Q:80,
    MIN_Q:0,
    VD:40,
    FLETE: 15,
    CC:0.35,
    EM:2.7,
  }
]
"""



        

    