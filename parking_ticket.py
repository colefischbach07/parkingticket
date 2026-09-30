"""Defines the ParkingTicket class."""

import math

class ParkingTicket:
    
    """Represents a ticket issued to an illegally parked car."""

    def __init__(self, car, officer, illegal_minutes):
        """Initialize a parking ticket."""
        if not isinstance(illegal_minutes, int):
            raise TypeError("Illegal minutes must be an integer.")
        if illegal_minutes <= 0:
            raise ValueError("Illegal minutes must be greater than zero.")

        self._car = car
        self._officer = officer
        self._illegal_minutes = illegal_minutes
        self._fine = self._calculate_fine()

    @property
    def car(self):
        """Return the car associated with the ticket."""
        return self._car

    @property
    def officer(self):
        """Return the officer who issued the ticket."""
        return self._officer

    @property
    def illegal_minutes(self):
        """Return the number of illegal parking minutes."""
        return self._illegal_minutes

    @property
    def fine(self):
        """Return the ticket fine."""
        return self._fine

    def _calculate_fine(self):
        """Calculate the fine based on illegal parking time."""
        hours = math.ceil(self._illegal_minutes / 60)
        return 25 + (hours - 1) * 10

    def __str__(self):
        """Return a readable parking ticket report."""
        return (
            "PARKING TICKET\n"
            f"Make: {self._car.make}\n"
            f"Model: {self._car.model}\n"
            f"Color: {self._car.color}\n"
            f"License: {self._car.license_number}\n"
            f"Illegal Minutes: {self._illegal_minutes}\n"
            f"Fine: ${self._fine}\n"
            f"Officer: {self._officer.name}\n"
            f"Badge Number: {self._officer.badge_number}"
        )