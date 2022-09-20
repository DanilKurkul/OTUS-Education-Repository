# создание объекта
# ссылки на объеты
# type/id/size
from sys import getsizeof

name = 'Vitaly'
print(name)
print(id(name))

fruit = 'banana'
print(id(fruit))

fruit = 'orange'
print(id(fruit))

fruit2 = fruit

print(id(fruit2), getsizeof(fruit))

print(type(5))
