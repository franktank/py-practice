# Vehicle / Car
# Parking Spot
# Parking Lot
# Potential Levels
class Vehicle(object):
    def __init__(self, license_plate):
        self.license_plate = license_plate
        self.parking_spot = None

    def park(self, spot):
        self.parking_spot = spot

    def unpark(self):
        self.parking_spot = None

class ParkingLot(object):
    def __init__(self, number_spots):
        self.total_spots = number_spots
        self.available_spots = number_spots
        self.parking_spots = [ParkingSpot(i) for i in range(number_spots)]

    def get_available_spots(self):
        return self.available_spots

    def find_spot(self):
        if self.available_spots == 0:
            return -1
        for i in range(self.total_spots):
            if self.parking_spots[i].is_available():
                return i

    def park_at_spot(self, index, vehicle):
        res = self.parking_spots[index].park(vehicle)
        return res

    def park(self, vehicle):
        idx = self.find_spot()
        res = self.park_at_spot(idx, vehicle)
        if res:
            self.available_spots -= 1
        return res

class ParkingSpot(object):
    def __init__(self, spot_number):
        self.vehicle = None
        self.spot_number = spot_number

    def is_available(self):
        return self.vehicle == None

    def park(self, vehicle):
        if self.is_available():
            self.vehicle = vehicle
            return True
        return False

    def unpark(self):
        self.vehicle = None
