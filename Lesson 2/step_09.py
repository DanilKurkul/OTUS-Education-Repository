# Коварство списков

from copy import deepcopy
# users = ['Дима', 'Толя', 'Ваня', 'Таня']
# print(id(users))
#
# users_2 = users.copy()
#
# users_2[1] = 'Николай'
#
# print(id(users_2))
# print(users)
# print(users_2)


users = ['Дима', 'Толя', 'Ваня', ['Таня', 'Ольга']]
print(id(users))

users_2 = deepcopy(users)
users_3 = users.copy()
users_3[-1] = users[-1].copy()
users_4 = users.copy()

users_2[-1][0] = 'Николай2'
#users_3[-1][0] = 'Николай3'
#users_4[-1][0] = 'Николай4'
#users_4[0]= 'Дима4'

print(id(users) == id(users_2))
print('id 1',id(users))
print('id 2',id(users_2))
print('id 3',id(users_3))
print('id 4',id(users_4))

print(users)
print(users_2)
print(users_3)
print(users_4)


print('Одинаковость id 1 и 4: ', id(users[0]) == id(users_4[0]), id(users[1]) == id(users_4[1]), id(users[2]) == id(users_4[2]), id(users[3]) == id(users_4[3]))
print('Одинаковость id 1 и 3: ', id(users[0]) == id(users_3[0]), id(users[1]) == id(users_3[1]), id(users[2]) == id(users_3[2]), id(users[3]) == id(users_3[3]))
print('Одинаковость id 1 [3] и 3 [3]: ', id(users[3][0]) == id(users_3[3][0]), id(users[3][1]) == id(users_3[3][1]))


print(id(users_4[0]))



