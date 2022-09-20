# PEP8 (CTRL+ALT+L)
# пробелы / отступы (4 пробела)
#import this

# print(5 * 5.)
# print(5 == int('f'))

list_i = [i for i in range(3) for j in range(3)]
list_range3 = [range(3)]


for i in range(3):
    print(i)
print([i for i in range(3)])
print('List i: ', list_i)
print('List range: ', list_range3)

print([i*j for i in range(1, 4) for j in range(3, 5)])
