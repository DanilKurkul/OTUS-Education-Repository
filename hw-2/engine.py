from dataclasses import dataclass


# Создайте датакласс Engine
@dataclass
class Engine:
    # добавьте атрибуты volume и pistons
    volume: float
    pistons: int


# Конец ДЗ. Дальше - отладка
if __name__ == '__main__':
    # Проверки
    __DEBUG = True


    def __debugging_examples():
        if not __DEBUG: return

        print('-- Debugging --')

        v6_2_2 = Engine(volume=2.2, pistons=6)

        print('\nV6 объемом 2.2\n', vars(v6_2_2), sep='')

        # End of debugging_examples()


    __debugging_examples()

# End of __name__ == '__main__'
