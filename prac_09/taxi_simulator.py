"""CP1404 Prac 09"""
from prac_01.menus import choice
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = ("q)uit, c)hoose taxi, d)rive\n"
        ">>>")

def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    choice - input(MENU).lower()
    while choice != 'q':
        if choice == 'c':
            print("Taxis available:")
            for i in range(0, len(taxis)):
                print(f"{i} - {taxis[i]}")
            taxi_choice = input("Choose taxi: ")
            if taxi_choice > len(taxis):
                print("Invalid taxi choice")
        if choice == 'd':
        print(bill)



main()