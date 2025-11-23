"""CP1404 Prac 09"""
from silver_service_taxi import SilverServiceTaxi

def main():
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    print(hummer)
    test_taxi = SilverServiceTaxi("test", 200, 2)
    test_taxi.start_fare()
    test_taxi.drive(18)
    print(test_taxi.get_fare())
main()