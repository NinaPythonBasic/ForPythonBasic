from abc import ABC
from homework_02 import exceptions

class Vehicle(ABC):
    #weight,
    started = False
    #fuel,
    #fuel_consumption
    def __init__(self, weight = 1000, fuel = 500, fuel_consumption = 6):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if (not self.started):
            if (self.fuel > 0):
                self.started = True
            else:
                raise exceptions.LowFuelError()

    def move(self, distance):
        used_fuel = self.fuel_consumption * distance
        if (self.fuel >= used_fuel):
            self.fuel -= used_fuel
        else:
            raise exceptions.NotEnoughFuel()
