# DRY (Don’t repeat yourself - не повторяйся)

phones = ['nokia', 'iphone', 'xiaomi', 'samsung']

print(phones[0])
print(phones[1])
print(phones[2])
print(phones[3])
print(len(phones))

item = 0
while item < len(phones):
    phones[item] = phones[item].upper()
    item += 1  # item = item + 1

print(phones)
phones = ['nokia', 'iphone', 'xiaomi', 'samsung']

for item in phones:
    item = item.upper()
    print(item)

print(phones)

print('-----------')
print(type(enumerate(phones)))
print ( number, item in enumerate(phones))

for number, item in enumerate(phones, start=1):
    # phones[number] = phones[number].upper()
    print('Номер', number)

# print(phones)

