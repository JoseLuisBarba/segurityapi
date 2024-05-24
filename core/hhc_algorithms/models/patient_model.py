from models.time_window_model import TimeWindow
from models.location_model import Location
import copy

#@passed_test
class Patient:
    def __init__(self, id: int, loc: Location, tw :TimeWindow, service_time: float,  demand: float, isWarehouse: bool= False) -> None:
        self._id: int = id
        self.loc: Location = loc
        self.tw: TimeWindow = tw
        self.demand: float = demand
        self.isAttended: bool = False
        self.vehicle_id: int = None
        self.serviceTime: float = service_time
        self.isWarehouse: bool = isWarehouse
        self.priority: float = float('inf')
        
    
    def copy(self, ) -> 'Patient':
        return Patient(self._id, self.loc, self.tw, self.serviceTime, self.demand, self.isWarehouse, self.isAttended)

    def attended_by(self, vehicle_id) -> None:
        self.isAttended = True
        self.vehicle_id = vehicle_id
    
    def not_attended(self,) -> None:
        self.isAttended = False
        self.vehicle_id = None


    def __eq__(self, other: 'Patient') -> bool:
        return self._id == other._id
    
    def __lt__(self, other: 'Patient'):
        return self.priority < other.priority
    
    def __gt__(self, other: 'Patient'):
        return self.priority > other.priority
    
    def __le__(self, other: 'Patient'):
        return self.priority <= other.priority
    
    def __ge__(self, other: 'Patient'):
        # Definir la comparación basada en la prioridad (mayor o igual que)
        return self.priority >= other.priority
    
    #check error none type vehicle id
    def to_json(self) -> dict:
        return {
            "_id": self._id,
            "x_loc": self.loc.x,
            "y_loc": self.loc.y,
            "a_tw": self.tw.a,
            "b_tw": self.tw.b,
            "demand": self.demand,
            "isAttended": self.isAttended,
            "vehicle": self.vehicle_id,
            "serviceTime": self.serviceTime,
            "isWarehouse": self.isWarehouse
        }
    

    

    
    



"""
    https://json-generator.com/
[
  '{{repeat(5, 7)}}',
  {
    _id: '{{objectId()}}',
    loc: {
      x: '{{floating(9, 20)}}',
      y: '{{floating(9, 20)}}'
    },
    tw: {
      a: '{{floating(9, 20)}}',
      b: '{{floating(9, 20)}}'
    },
    serviceTime: '{{floating(9, 20)}}',
    demand: '{{floating(0, 100)}}',
    isWarehouse: '{{bool()}}'
  }
]

"""