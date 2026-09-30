"""Unit tests for the ParkingTicket class."""

import unittest
from parked_car import ParkedCar
from police_officer import PoliceOfficer
from parking_ticket import ParkingTicket


class TestParkingTicket(unittest.TestCase):
    """Tests the ParkingTicket class."""

    def setUp(self):
        self.car = ParkedCar("Honda", "Civic", "Black", "ABC123", 120)
        self.officer = PoliceOfficer("Cole Fischbach", "1234")

    def test_one_minute_fine(self):
        ticket = ParkingTicket(self.car, self.officer, 1)
        self.assertEqual(ticket.fine, 25)

    def test_sixty_minute_fine(self):
        ticket = ParkingTicket(self.car, self.officer, 60)
        self.assertEqual(ticket.fine, 25)

    def test_sixty_one_minute_fine(self):
        ticket = ParkingTicket(self.car, self.officer, 61)
        self.assertEqual(ticket.fine, 35)

    def test_120_minute_fine(self):
        ticket = ParkingTicket(self.car, self.officer, 120)
        self.assertEqual(ticket.fine, 35)

    def test_121_minute_fine(self):
        ticket = ParkingTicket(self.car, self.officer, 121)
        self.assertEqual(ticket.fine, 45)

    def test_car_information(self):
        ticket = ParkingTicket(self.car, self.officer, 60)

        self.assertEqual(ticket.car.make, "Honda")
        self.assertEqual(ticket.car.model, "Civic")
        self.assertEqual(ticket.car.color, "Black")
        self.assertEqual(ticket.car.license_number, "ABC123")

    def test_officer_information(self):
        ticket = ParkingTicket(self.car, self.officer, 60)

        self.assertEqual(ticket.officer.name, "Cole Fischbach")
        self.assertEqual(ticket.officer.badge_number, "1234")

    def test_illegal_minutes(self):
        ticket = ParkingTicket(self.car, self.officer, 45)
        self.assertEqual(ticket.illegal_minutes, 45)

    def test_invalid_illegal_minutes(self):
        with self.assertRaises(ValueError):
            ParkingTicket(self.car, self.officer, 0)

    def test_readable_report(self):
        ticket = ParkingTicket(self.car, self.officer, 61)
        report = str(ticket)

        self.assertIn("Honda", report)
        self.assertIn("Civic", report)
        self.assertIn("ABC123", report)
        self.assertIn("61", report)
        self.assertIn("35", report)
        self.assertIn("Cole Fischbach", report)
        self.assertIn("1234", report)


if __name__ == "__main__":
    unittest.main()