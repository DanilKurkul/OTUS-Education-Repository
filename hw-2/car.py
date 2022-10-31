from vehicle import Vehicle, exceptions
from engine import Engine


# Cоздайте класс Car - класс Car должен быть наследником Vehicle
class Car(Vehicle):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # добавьте атрибут engine классу Car
        self._engine = None

    # объявите метод set_engine, который принимает в себя экземпляр объекта Engine
    # и устанавливает на текущий экземпляр Car
    def set_engine(self, newengine: Engine, swap: bool = False):
        if self._engine is None or swap is True:
            self._engine = newengine
        else:
            raise exceptions.VehicleException(
                'Engine could be added only if car have no engine yet ' + \
                'or if it is swap engine operation, called with parameter swap=True. ' + \
                f'Current engine is {vars(self._engine)}'
            )


# Конец ДЗ. Дальше - отладка
if __name__ == '__main__':
    # Проверки
    __DEBUG = True


    def __debugging_examples():
        if not __DEBUG: return

        print('-- Debugging --')

        car1 = Car()

        # -- Старт и стоп проверки
        car1.fuel = 80
        car1.start()
        assert car1.started
        car1.stop()
        assert not car1.started

        # -- Move проверки
        # car1.move(-801)
        # car1.move('Far')
        # car1.move()
        car1.move('600')

        # -- Проверки engine
        v6_2_2 = Engine(volume=2.2, pistons=6)
        car1.set_engine(v6_2_2)
        r4_1_4 = Engine(1.4, 4)
        car1.set_engine(r4_1_4, swap=True)

        # -- Параметры экземпляра и класса
        print('\nПараметры экземпляра car1\n', vars(car1), sep='')
        print('\nПараметры класса Car\n', vars(Car), sep='')

        # -- Наследование, переопределение и использование свойств класса
        class HeavyCar(Car):
            _WEIGHT = 2000
            _FUEL_CONSUMPTION = Vehicle._FUEL_CONSUMPTION * 1.5

        car2 = HeavyCar()
        car2.set_engine(Engine(5.5, 10))

        print('\nПараметры экземпляра car2\n', vars(car2), sep='')
        print('\nПараметры класса HeavyCar\n', vars(HeavyCar), sep='')

        # End of debugging_examples()


    __debugging_examples()

# End of __name__ == '__main__'
