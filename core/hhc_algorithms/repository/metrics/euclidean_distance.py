import math
from models.location_model import EuclideanLocation


class euclidean_distance:
    def __call__(self, loc1: EuclideanLocation, loc2: EuclideanLocation) -> float:
        diff_x = loc1.x - loc2.x
        diff_y = loc1.y - loc2.y
        return math.sqrt(diff_x**2 + diff_y**2)
    
