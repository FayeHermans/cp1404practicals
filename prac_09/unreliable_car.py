"""CP1404 Prac 09"""
import random

from car import Car

class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability: float):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if random.randint(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0

