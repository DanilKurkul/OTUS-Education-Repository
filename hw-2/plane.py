from vehicle import Vehicle, exceptions


# Cоздайте класс Plane, наследник Vehicle
class Plane(Vehicle):
    _MAX_CARGO = Vehicle._WEIGHT * 0.1

    # добавьте атрибуты cargo и max_cargo классу Plane
    # добавьте max_cargo в инициализатор (переопределите родительский)
    def __init__(self, max_cargo=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._cargo = 0
        self._max_cargo = max_cargo if not max_cargo is None else self._MAX_CARGO

    @property
    def cargo(self):
        return self._cargo

    # объявите метод load_cargo, который принимает число,
    # проверяет, что в сумме с текущим cargo не будет перегруза, и обновляет значение,
    # в ином случае выкидывает исключение exceptions.CargoOverload
    def load_cargo(self, added_cargo):
        added_cargo = float(added_cargo)
        if not added_cargo > 0:
            # Общее исключение для VehicleException, может тут ValueErroe или TypeError вызывать
            raise exceptions.VehicleException(
                'Additional cargo must be positive value of int or float. ' + \
                f'Passed additional cargo is {added_cargo}, type {type(added_cargo)}'
            )

        cargo_sum = self._cargo + added_cargo

        if cargo_sum <= self._max_cargo:
            self._cargo = cargo_sum
        else:
            raise exceptions.CargoOverload(
                f'Lots of cargo. Current cargo {self._cargo}, additional cargo {added_cargo}. ' + \
                f'Combined cargo {cargo_sum} - it is more then max {self._max_cargo}.'
            )

    # объявите метод remove_all_cargo, который обнуляет значение cargo
    # и возвращает значение cargo, которое было до обнуления
    def remove_all_cargo(self):
        removed_cargo = self._cargo
        self._cargo = 0
        return removed_cargo


# Конец ДЗ. Дальше - отладка
if __name__ == '__main__':
    # Проверки
    __DEBUG = True


    def __debugging_examples():
        if not __DEBUG: return

        print('-- Debugging --')

        plane1 = Plane()

        # -- Параметры экземпляра и класса
        print('\nПараметры экземпляра plane1\n', vars(plane1), sep='')
        print('\nПараметры класса Plane\n', vars(Plane), sep='')

        # -- Cargo проверки
        plane1.load_cargo('80')
        # plane1.load_cargo(-21)

        # -- Move проверки
        plane1.fuel = 65
        plane1.move(600, stop_arter_moving=True)

        # -- Проверка перегрузки cargo в другой plane
        plane2 = Plane()
        plane2.load_cargo(plane1.remove_all_cargo())

        print('\nplane2.cargo:', plane2.cargo)
        print('\nПараметры экземпляра plane1\n', vars(plane1), sep='')

        # Проверка переопределения class property при наследовании
        class SuperPlane(Plane):
            _WEIGHT = Plane._WEIGHT * 2
            _MAX_CARGO = _WEIGHT * 0.3

        plane3 = SuperPlane()

        print('\nПараметры экземпляра plane3 класса SuperPlane\n', vars(plane3), sep='')

        # End of debugging_examples()

    __debugging_examples()

# End of __name__ == '__main__'