# базовые типы данных

from copy import deepcopy

# • контейнеры: [list], (tuple)
# • хеш-таблицы: {dict:dict}, {set} - аналог математического множества, уникально
# dict - ключи уникальны
#             1       2       3      4
users = ['Дима', 'Толя', 'Ваня', 'Таня']

dct = {1: 'Дима', 2: 'Толя', 'l': ['Таня', 'Оля']}
dct_2 = dct.copy()
dct_2 = deepcopy(dct)
dct_2[1] = 'Дима2'
dct_2['l'][0] = 'Таня2'
print(dct[2])
print(dct)
print(dct_2)
print(type(dct[1]))

some_set = {1, 2, 2, 4}
print(some_set)

lst2 = [1, 2, 2, 4]
print(list(set(lst2)))
