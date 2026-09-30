from parking_ticket import ParkingTicket


class PoliceOfficer:
    """Represents a police officer who inspects parked cars."""

    def __init__(self, name, badge_number):
        """Initialize a police officer."""
        self.name = name
        self.badge_number = badge_number

    @property
    def name(self):
        """Return the officer's name."""
        return self._name

    @name.setter
    def name(self, value):
        """Set the officer's name."""
        if not isinstance(value, str):
            raise TypeError("Officer name must be a string.")
        if not value.strip():
            raise ValueError("Officer name cannot be empty.")
        self._name = value

    @property
    def badge_number(self):
        """Return the officer's badge number."""
        return self._badge_number

    @badge_number.setter
    def badge_number(self, value):
        """Set the officer's badge number."""
        if not isinstance(value, str):
            raise TypeError("Badge number must be a string.")
        if not value.strip():
            raise ValueError("Badge number cannot be empty.")
        self._badge_number = value

    def inspect_car(self, car, meter):
        """Inspect a parked car and return a ticket if time has expired."""
        if car.minutes_parked > meter.minutes_purchased:
            illegal_minutes = car.minutes_parked - meter.minutes_purchased
            return ParkingTicket(car, self, illegal_minutes)
        return None