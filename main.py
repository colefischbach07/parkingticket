"""Demonstrates the parking ticket simulator."""

from parked_car import ParkedCar
from parking_meter import ParkingMeter
from police_officer import PoliceOfficer


def main():
    """Run a demonstration of the parking ticket simulator."""

    car = ParkedCar(
        "Honda",
        "Civic",
        "Black",
        "ABC123",
        125
    )

    meter = ParkingMeter(60)

    officer = PoliceOfficer(
        "Cole Fischbach",
        "1234"
    )

    ticket = officer.inspect_car(car, meter)

    if ticket is not None:
        print(ticket)
    else:
        print("No parking violation.")


if __name__ == "__main__":
    main()