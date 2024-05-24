from __future__ import division
from math import atan
from math import atan2
from math import cos
from math import radians
from math import sin
from math import sqrt
from math import tanh

from models.location_model import  GPSLocation

class vicenty_inv_distance:
    def __call__(self, loc1: GPSLocation, loc2: GPSLocation) -> float:
        A: float  = 6378137.0  # length of semi-major axis of the ellipsoid aka radius of the equator in meters
        F: float  = 0.0034 # flattening of the ellipsoid
        
