from abc import ABC, abstractmethod

class Location:
    def __init__(self) -> None:
        pass

    @abstractmethod
    def to_json(self):
        pass

    @abstractmethod
    def is_equal(self, other: 'Location'):
        pass

    
class EuclideanLocation(Location):
    def __init__(self, x: float, y: float) -> None:
        super().__init__()
        self._x = x
        self._y = y

    @property
    def x(self,) -> float:
        return self._x
    @property
    def y(self,) -> float:
        return self._y
    
    @x.setter
    def x(self, value: float) -> None:
        self._x = value

    @y.setter 
    def y(self, value: float) -> None:
        self._y = value

    def is_equal(self, other: 'EuclideanLocation'):
        return (self._x == other.x) and (self._y == other.y)
    
    def to_json(self):
        return {
            'x': self._x,
            'y': self._y
        }
    
    
 
        
    

class GPSLocation(Location):
    def __init__(self, latitude: float, longitude: float) -> None:
        super().__init__()
        self.latitude = latitude
        self.longitude = longitude

    def is_equal(self, other: 'GPSLocation'):
        return (self.latitude == other.latitude) and (self.latitude == other.latitude)

    def to_json(self):
        return {
            'latitude': self.latitude,
            'logitude': self.latitude 
        }
    






        

    




    