"""Defines the ParkingMeter class."""


class ParkingMeter:
    """shows a parking meter."""

    def __init__( self, minutes_purchased ):
        """Initialize the parking meter."""
        self.minutes_purchased = minutes_purchased

    @property
    def minutes_purchased(self):
        """Return the number of purchased parking minutes."""
        return self._minutes_purchased


    @minutes_purchased.setter
    def minutes_purchased(self, value):
        """Set the number of purchased parking minutes."""
        if not isinstance(value, int):
            raise TypeError("Minutes purchased must be an integer. " )
        if value < 0:
            raise ValueError("Minutes purchased cannot be negative")
        self._minutes_purchased = value