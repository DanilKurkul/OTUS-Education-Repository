from abc import ABC, abstractmethod
import exceptions


class Vehicle(ABC):
    # добавьте атрибуты weight, started, fuel, fuel_consumption со значениями по умолчанию
    _WEIGHT = 1000
    _STARTED = False
    # _FUEL = 0
    _FUEL_CONSUMPTION = 10

    # добавьте инициализатор для установки weight, fuel, fuel_consumption
    @abstractmethod
    def __init__(self, weight=None, fuel=0, fuel_consupmtion=None):
        # Значения по умолчанию приходится внутри проверять,
        # чтобы можно было свойство класса переопределить при наследовании
        self._weight = float(weight) if not weight is None else self._WEIGHT
        self._started = self._STARTED
        self.fuel = float(fuel)
        self._fuel_consupmtion = float(fuel_consupmtion) if not fuel_consupmtion is None else self._FUEL_CONSUMPTION

    # добавьте метод start, который, если ещё не состояние started,
    # проверяет, что топлива больше нуля, и обновляет состояние started,
    # иначе выкидывает исключение exceptions.LowFuelError
    def start(self):
        if not self._started:
            if (self.fuel > 0):
                self._started = True
            else:
                raise exceptions.LowFuelError(f'Current fuel level is {self.fuel}')

    def stop(self):
        self._started = False

    @property
    def started(self):
        return self._started

    # добавьте метод move, который проверяет, что достаточно топлива для преодоления переданной дистанции,
    # и изменяет количество оставшегося топлива,
    # иначе выкидывает исключение exceptions.NotEnoughFuel
    def move(self, distance, stop_arter_moving: bool = False):
        # Проверка переданной дистанции
        distance = float(distance)
        if not (
                # isinstance(distance, (int, float)) and
                distance > 0
        ):
            # Общее исключение для VehicleException, может тут ValueErroe или TypeError вызывать
            raise exceptions.VehicleException(
                'Moving distance must be positive value of int or float. ' + \
                f'Current distance is {distance}, type {type(distance)}'
            )

        # Остаток топлива
        rest_fuel = self.fuel - distance * self._fuel_consupmtion / 100

        if rest_fuel < 0:  # Если не хваатет
            raise exceptions.NotEnoughFuel(f'Not enough {self.fuel} fuel. Need {rest_fuel * (-1)} fuel more.')
        else:
            self.start()  # решил, что не гоже выключенными катиться
            self.fuel = rest_fuel
            if stop_arter_moving: self.stop()


# Конец ДЗ. Дальше - отладка
if __name__ == '__main__':
    # Проверки
    __DEBUG = True


    def __debugging_examples():
        if not __DEBUG: return

        print('-- Debugging --')

        # -- Класс какой-то техники для проверки
        class EnyVehicle(Vehicle):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

        veh1 = EnyVehicle()
        veh1.fuel = 80

        # -- Старт и стоп проверки
        veh1.start()
        assert veh1.started
        veh1.stop()
        assert not veh1.started

        # -- Move проверки
        # veh1.move(-801)
        # veh1.move('Far')
        # veh1.move()
        veh1.move('600')

        # -- Параметры экземпляра и класса
        print('\nПараметры экземпляра veh1\n', vars(veh1), sep='')
        print('\nПараметры класса EnyVehicle\n', vars(EnyVehicle), sep='')

        # End of debugging_examples()


    __debugging_examples()

    # End of __name__ == '__main__'
