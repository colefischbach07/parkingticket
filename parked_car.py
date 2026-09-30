class ParkedCar:
    """Represents a car parked at a parking meter."""

    def __init__( self, make, model, color, license_number, minutes_parked ):
        """Initialize a parked car."""
        self.make =  make
        self.model = model
        self.color = color
        self.license_number = license_number
        self.minutes_parked = minutes_parked

    @property
    def make(self):
        """Return the car's make."""
        return self._make

    @make.setter
    def make(self, value):
        """Set the car's make."""
        if not isinstance(value, str):
            raise TypeError(" Make must be a string ")
        if not value.strip():
            raise ValueError(" Make cannot be empty ")
        self._make = value

    @property
    def model(self):
        """Return the car's model."""
        return self._model


    @model.setter
    def model(self, value):
        """Set the car's model."""
        if not isinstance(value, str):
            raise TypeError("Model must be a string.")
        if not value.strip():
            raise ValueError("Model cannot be empty.")
        self._model = value

    @property
    def color(self):
        """Return the car's color."""
        return self._color

    @color.setter
    def color(self, value):
        """Set the car's color."""
        if not isinstance(value, str):
            raise TypeError("Color must be a string.")
        if not value.strip():
            raise ValueError("Color cannot be empty.")
        self._color = value

    @property
    def license_number(self):
        """Return the car's license number."""
        return self._license_number



    @license_number.setter
    def license_number(self, value):
        """Set the car's license number."""
        if not isinstance(value, str):
            raise TypeError("License number must be a string.")
        if not value.strip():
            raise ValueError("License number cannot be empty.")
        self._license_number = value

    @property
    def minutes_parked(self):
        """Return the number of minutes parked."""
        return self._minutes_parked


    @minutes_parked.setter
    def minutes_parked(self, value):
        """Set the number of minutes parked."""
        if not isinstance(value, int):
            raise TypeError("Minutes parked must be an integer.")
        if value < 0:
            raise ValueError("Minutes parked cannot be negative.")
        self._minutes_parked = value