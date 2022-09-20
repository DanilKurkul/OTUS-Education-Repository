# тернарный оператор
# сокращенный тернарный оператор
# тернарный оператор с помощью кортежей

age = 19
msg = 'Доступ запрещен'

if 'Доступ разрешен':
    print('Доступ разрешен')

msg = 'Доступ разрешен' if age >= 18 else 'Доступ запрещен'

print(msg)

# True or "smf" - True
# False or "smf" - "smf"

msg = age >= 18 or 'Доступ запрещен'
print(msg)

msg = ('Доступ запрещен', 'Доступ разрешен')[age >= 18]
print(msg)
tup = ('Доступ запрещен', 'Доступ разрешен', 'третье значение')
#str = tup[1]
#print(str)
print(tup[1:2])
print(type(tup[1:2]))
from sys import getsizeof
print('Size of tup: ', len(tup[1]))

