# • контейнеры: [list], (tuple)

phones = ['nokia', 'iphone', 'xiaomi', 'samsung']

print(type(phones))

phones[0] = 'some_phone'
print(phones)

phones_2 = phones
print(id(phones))
print(id(phones_2))


phones = ('nokia', 'iphone', 'xiaomi', 'samsung')

# phones[0] = 'some_phone'
# print(phones)


