from models.patient_model import Patient
from models.vehicle_model import Vehicle
from repository.metrics.euclidean_distance import euclidean_distance
from repository.metaheuristic.simulated_annealing import x_sa
import copy
import random
from copy import deepcopy
from min_max_heap import MinMaxHeap
from typing import Any

class Instance(x_sa):
    def __init__(self, vehicles: list[Vehicle], patients: list[Patient]) -> None:
        super().__init__()
        """Crea una instancia  VRP

        Args:
            vehicles (list[Vehicle]): lista de vehiculos del problema
            patiens (list[Patient]): lista de pacientes
        """
        self.vehicles:  list[Vehicle] = copy.deepcopy(vehicles)
        patients_copy = copy.deepcopy(patients)
        patients_copy.sort(key= lambda p: p._id, reverse=False)
        self.patients: list[Patient] = patients_copy

    #@test
    #@check cost_function method
    def cost_function(self) -> float:
        return self.get_total_distance_and_vehicles()[0] 
    
    #@test
    #@check generate_neighbor method
    def generate_neighbor(self):
        return deepcopy(self.patient_exchange())
    
    #@no_test
    def check_restrictions(self) -> bool:
        print('')
        return True
    
    def get_information(self, ) -> Any:
        return self.get_output()

    #@test
    #@check __getitem__ method
    def __getitem__(self, key: int):
        return self.patients[key]     
       
    #@no_test
    def __str__(self) -> str:
        pass

    #@test    
    #@check sort_by_ready_time method
    def sort_by_ready_time(self,):
        self.patients.sort(key= lambda p: p.tw.a, reverse=False)

                   
    #@test 
    #@check find_inital_solution method
    def find_inital_solution(self):
        # excluir a wharehouse
        for i, vehicle in enumerate(self.vehicles):
            keep_searching: bool = True
            while keep_searching:

                heap: MinMaxHeap = MinMaxHeap()
                attended: bool = False

                print(f"{vehicle.id}" ,[ p[0]._id for p in vehicle.service_route])
                if ( vehicle.service_route[-1][0].isWarehouse and len(vehicle.service_route) > 1) or self.all_attended(self.patients[1:]): #criterio de parada
                    keep_searching = False
                    continue
                
                for patient in self.patients:  # O(n log n)
                    if not patient.isWarehouse and not patient.isAttended:
                        patient.priority = vehicle.compute_priority(patient= patient)
                        heap.push(patient)

                heap_force: MinMaxHeap = copy.deepcopy(heap) # O (n)

                while not heap.is_empty():
                    ref_min_patient: Patient = heap.pop_min() # O( log n)
                    if vehicle.attended_patient(self.patients[ref_min_patient._id]):
                        attended = True
                        break

                if attended:
                    continue

                print([j._id for j in heap.queue])

                while not heap_force.is_empty():
                    ref_min_patient: Patient = heap_force.pop_min() # O(n log n)
                    if vehicle.attended_patient_force(self.patients[ref_min_patient._id]):
                        break

                vehicle.return_warehouse()
                break

        for i, vehicle in enumerate(self.vehicles):
            if vehicle.t == vehicle.WARE_HOUSE.tw.a: # aun no ha  salido
                continue
            vehicle.return_warehouse() # retornamos a los vehiculos que quedan
        if not self.all_attended(patients= self.patients[1:], summary=True):
            print('Alert: Not all vehicles has been attended!')



        
    
    def patient_exchange(self):
        """
        # escogemos dos vehiculos aleatorios
        rand_v1: int = random.randint(a=0, b=len(self.vehicles) - 1 )
        v1: Vehicle = self.vehicles[rand_v1]
        # escogemos un nodo aleatorio
        v1_patients: list[Patient] = [ p[0]  for p in v1.service_route if not p[0].isWarehouse]
        v1_probabilities: list[float] = [ 1.0 / len(v1_patients) for p in v1.service_route if not p[0].isWarehouse]
        rand_patient_v1: Patient = random.choices(v1_patients, v1_probabilities, k=1)[0]
        v1.remove_patient(rand_patient_v1)
        while not rand_patient_v1.isAttended:
            if self.get_neighbour(patient= rand_patient_v1):
                return self
            self.get_neighbour(patient= rand_patient_v1, force=True)
        return self
        """
        patient_list: list[Patient] = self.patients[1:]
        weights_list: list[float] = [ 1 / len(self.vehicles[p.vehicle_id].service_route) for p in self.patients[1:]]
        rand_patient: Patient = random.choices(patient_list, weights_list, k=1)[0]
        v1: Vehicle = self.vehicles[rand_patient.vehicle_id]
        v1.remove_patient(rand_patient)
        while not rand_patient.isAttended:
            if self.get_neighbour(patient= rand_patient):
                return self
            self.get_neighbour(patient= rand_patient, force=True)
        return self
        
    #@test
    #@check get_neighbour method
    def get_neighbour(self, patient: Patient, force: bool= False): #listo
        shuffled = [ i for i in range(0, len(self.vehicles) - 1)] 
        random.shuffle(shuffled) # permutamos
        for vehicle_id in shuffled:
            vehicle: Vehicle = self.vehicles[vehicle_id]
            if force or vehicle.t != 0:
                if vehicle.try_attend_patient(patient): # tratamos de antender
                    return True
        return False
    
    #@test
    #@check get_output method
    def get_output(self, ) -> dict:
        dist: float = 0
        result: list = []
        for vehicle in self.vehicles:
            if vehicle.t == 0:
                continue
            vehicle.return_warehouse()
            dist += vehicle.total_distance
            result.append(vehicle.to_json())
        return {
            'vehicle_count': len(result),
            'distance': dist,
            'results': result
        }

    #@test 
    #@check all_attended method
    def all_attended(self, patients: list[Patient], summary: bool= False) -> bool: 
        """verifica si todos los pacientes fueron atendidos
        Args:
            patients (list[Patient]): lista de pacientes a comprobar si fueron todos atendidos
            summary (bool, optional): imprime que pacientes aun no son atendidos. Defaults to False.

        Returns:
            bool: Verdadero si todos los pacientes fueron atendidos, de lo contrario falso
        """
        result: bool = True
        for i, patient in enumerate(patients):
            if not patient.isAttended:
                if summary:
                    print(f'{i}: {patient}')
                result = False
        return result

    #@test 
    #@check get_total_distance_and_vehicles method
    def get_total_distance_and_vehicles(self,):
        dist = 0
        vehicles_used = 0
        for vehicle in self.vehicles:
            if vehicle.t == 0:
                continue
            vehicle.return_warehouse()
            vehicles_used += 1
            dist += vehicle.total_distance
        return dist, vehicles_used
            








