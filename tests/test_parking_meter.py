"""Unit tests for the ParkingMeter class."""

import unittest
from parking_meter import ParkingMeter
class TestParkingMeter(unittest.TestCase):
    """Tests the ParkingMeter class."""

    def test_positive_minutes(self):
        meter = ParkingMeter(60)
        self.assertEqual(meter.minutes_purchased, 60)

    def test_zero_minutes(self):
        meter = ParkingMeter(0)
        self.assertEqual(meter.minutes_purchased, 0)

    def test_negative_minutes(self):
        with self.assertRaises(ValueError):
            ParkingMeter(-1)


    def test_noninteger_minutes(self):
        with self.assertRaises(TypeError):
            ParkingMeter(60.5)


    def test_reassignment(self):
        meter = ParkingMeter(60)
        meter.minutes_purchased = 120
        self.assertEqual(meter.minutes_purchased, 120)


if __name__ == "__main__":
    unittest.main()