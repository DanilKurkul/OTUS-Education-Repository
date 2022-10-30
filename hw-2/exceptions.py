"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


# Базовый класс для всех кастомных исключений для Vehicle
class VehicleException(Exception):
    pass


class LowFuelError(VehicleException):
    pass


class NotEnoughFuel(VehicleException):
    pass


class CargoOverload(VehicleException):
    pass
