from enum import Enum

class VehicleSize(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Vehicle(object):
    def __init__(self,license_plate, size):
        self.license_plate = license_plate
        self.size = size

class ParkingLot(object):
    def __init__(self, )
