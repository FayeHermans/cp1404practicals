"""CP1404 Prac 09"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = ("q)uit, c)hoose taxi, d)rive\n"
        ">>> ")


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill = 0
    print("Let's drive!")
    choice = input(MENU).lower()
    while choice != 'q':
        if choice == 'c':
            print("Taxis available:")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            if taxi_choice > len(taxis):
                print("Invalid taxi choice")
            else:
                current_taxi = taxis[taxi_choice]

        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                trip_fare = drive_taxi(current_taxi, taxis)
                bill += trip_fare

        else:
            print("Invalid option")

        print(f"Bill to date: ${bill:.2f}")
        choice = input(MENU).lower()
    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def drive_taxi(current_taxi: Taxi | SilverServiceTaxi, taxis: list[Taxi | SilverServiceTaxi]) -> float:
    distance = int(input("Drive how far? "))
    Taxi.start_fare(current_taxi)
    Taxi.drive(current_taxi, distance)
    if current_taxi == taxis[0]:
        trip_fare = Taxi.get_fare(current_taxi)
    else:
        trip_fare = SilverServiceTaxi.get_fare(current_taxi)
    print(f"Your {current_taxi.name} trip cost you ${trip_fare:.2f}")
    return trip_fare


def display_taxis(taxis: list[Taxi | SilverServiceTaxi]):
    for i in range(0, len(taxis)):
        print(f"{i} - {taxis[i]}")


main()
