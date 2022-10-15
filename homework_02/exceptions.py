"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""
class LowFuelError(BaseException):
    """ The error of low fuel level. """
    pass

class NotEnoughFuel(BaseException):
    """ Fuel level is not enough. """
    pass

class CargoOverload(BaseException):
    """ Overloading of cargo. """
    pass

