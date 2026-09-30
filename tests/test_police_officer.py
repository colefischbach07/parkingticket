"""Unit tests for the PoliceOfficer class."""

import unittest
from parked_car import ParkedCar
from parking_meter import ParkingMeter
from parking_ticket import ParkingTicket
from police_officer import PoliceOfficer


class TestPoliceOfficer(unittest.TestCase):
    """Tests the PoliceOfficer class."""

    def setUp(self):
        self.officer = PoliceOfficer("Cole Fischbach", "1234")

    def test_less_time_than_purchased(self):
        car = ParkedCar("Honda", "Civic", "Black", "ABC123", 50)
        meter = ParkingMeter(60)

        ticket = self.officer.inspect_car(car, meter)

        self.assertIsNone(ticket)

    def test_exact_time_purchased(self):
        car = ParkedCar("Honda", "Civic", "Black", "ABC123", 60)
        meter = ParkingMeter(60)

        ticket = self.officer.inspect_car(car, meter)

        self.assertIsNone(ticket)

    def test_one_minute_over(self):
        car = ParkedCar("Honda", "Civic", "Black", "ABC123", 61)
        meter = ParkingMeter(60)

        ticket = self.officer.inspect_car(car, meter)

        self.assertIsNotNone(ticket)
        self.assertIsInstance(ticket, ParkingTicket)

    def test_illegal_minutes(self):
        car = ParkedCar("Honda", "Civic", "Black", "ABC123", 100)
        meter = ParkingMeter(60)

        ticket = self.officer.inspect_car(car, meter)

        self.assertEqual(ticket.illegal_minutes, 40)

    def test_ticket_information(self):
        car = ParkedCar("Honda", "Civic", "Black", "ABC123", 90)
        meter = ParkingMeter(60)

        ticket = self.officer.inspect_car(car, meter)

        self.assertEqual(ticket.car.make, "Honda")
        self.assertEqual(ticket.car.model, "Civic")
        self.assertEqual(ticket.car.color, "Black")
        self.assertEqual(ticket.car.license_number, "ABC123")
        self.assertEqual(ticket.officer.name, "Cole Fischbach")
        self.assertEqual(ticket.officer.badge_number, "1234")
if __name__ == "__main__":
    unittest.main()