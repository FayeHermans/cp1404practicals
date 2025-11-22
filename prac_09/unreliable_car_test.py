"""CP1404 Prac 09"""
from prac_09.unreliable_car import UnreliableCar
import random

def main():
    my_car = UnreliableCar("Subi", 100, 80)
    for i in range(0,10):
        my_car.drive(5)
        print(my_car)

main()