"""CP1404 Prac 09"""
from taxi import Taxi

class SilverServiceTaxi(Taxi):

    def __init__(self, name, fuel, fanciness: float):
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness
