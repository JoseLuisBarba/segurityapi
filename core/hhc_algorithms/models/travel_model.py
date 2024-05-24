from models.patient_model import Patient 

# check  Travel class
class Travel:
    def __init__(self, 
            is_warehouse: bool, vehicle_id: int, patient_id:  int, 
            travel_distance: float, travel_time: float, arrival_time: float, 
            wait_time: float, service_time: float, departure_time: float,
            total_distance: float, capacity: float, loc_x: float, loc_y: float  
        ) -> None:
        """_summary_

        Args:
            is_warehouse (bool): _description_
            vehicle_id (int): _description_
            patient_id (int): _description_
            travel_distance (float): _description_
            travel_time (float): _description_
            arrival_time (float): _description_
            wait_time (float): _description_
            service_time (float): _description_
            departure_time (float): _description_
            total_distance (float): _description_
            capacity (float): _description_
        """
        self.is_warehouse: bool = is_warehouse
        self.vehicle_id: int = vehicle_id
        self.patient_id: int = patient_id
        self.travel_distance: float = travel_distance
        self.travel_distance: float = travel_distance
        self.travel_time: float = travel_time
        self.arrival_time: float = arrival_time
        self.wait_time: float = wait_time
        self.service_time: float = service_time
        self.departure_time: float = departure_time
        self.total_distance: float = total_distance
        self.capacity: float = capacity
        self.loc_x: float = loc_x
        self.loc_y: float = loc_y

    def to_json(self, ):
        return {
            'is_warehouse': self.is_warehouse,
            'vehicle_id': self.vehicle_id,
            'patient_id': self.patient_id,
            'travel_distance': self.travel_distance,
            'travel_distance': self.travel_distance,
            'travel_time': self.travel_time,
            'arrival_time': self.arrival_time,
            'wait_time': self.wait_time,
            'service_time': self.service_time,
            'departure_time': self.departure_time,
            'total_distance': self.total_distance,
            'capacity': self.capacity,
            'loc_x': self.loc_x,
            'loc_y': self.loc_y,
        }
















