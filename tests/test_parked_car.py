"""Unit tests for the ParkedCar class."""



import unittest
from parked_car import ParkedCar


class TestParkedCar(unittest.TestCase):
    """Tests the ParkedCar class."""

    def test_valid_construction(self):
        car = ParkedCar("Honda", "Civic", "Black", "ABC123", 60)
        self.assertEqual(car.make, "Honda")
        self.assertEqual(car.model, "Civic")
        self.assertEqual(car.color, "Black")
        self.assertEqual(car.license_number, "ABC123")
        self.assertEqual(car.minutes_parked, 60)

    def test_property_reassignment(self):
        car = ParkedCar("Honda", "Civic", "Black", "ABC123", 60)
        car.make = "Toyota"
        car.model = "Camry"
        car.color = "White"
        car.license_number = "XYZ789"
        car.minutes_parked = 90

        self.assertEqual(car.make, "Toyota")
        self.assertEqual(car.model, "Camry")
        self.assertEqual(car.color, "White")
        self.assertEqual(car.license_number, "XYZ789")
        self.assertEqual(car.minutes_parked, 90)



    def test_empty_strings(self):
        with self.assertRaises(ValueError):
            ParkedCar("", "Civic", "Black", "ABC123", 60)

        with self.assertRaises(ValueError):
            ParkedCar("Honda", "", "Black", "ABC123", 60)

        with self.assertRaises(ValueError):
            ParkedCar("Honda", "Civic", "", "ABC123", 60)

        with self.assertRaises(ValueError):
            ParkedCar("Honda", "Civic", "Black", "", 60)

    def test_incorrect_string_types(self):
        with self.assertRaises(TypeError):
            ParkedCar(123, "Civic", "Black", "ABC123", 60)

        with self.assertRaises(TypeError):
            ParkedCar("Honda", 123, "Black", "ABC123", 60)

        with self.assertRaises(TypeError):
            ParkedCar("Honda", "Civic", 123, "ABC123", 60)

        with self.assertRaises(TypeError):
            ParkedCar("Honda", "Civic", "Black", 123, 60)

    def test_zero_minutes(self):
        car = ParkedCar("Honda", "Civic", "Black", "ABC123", 0)
        self.assertEqual(car.minutes_parked, 0)

    def test_positive_minutes(self):
        car = ParkedCar("Honda", "Civic", "Black", "ABC123", 120)
        self.assertEqual(car.minutes_parked, 120)

    def test_negative_minutes(self):
        with self.assertRaises(ValueError):
            ParkedCar("Honda", "Civic", "Black", "ABC123", -1)

    def test_noninteger_minutes(self):
        with self.assertRaises(TypeError):
            ParkedCar("Honda", "Civic", "Black", "ABC123", 60.5)




if __name__ == "__main__":
    unittest.main()