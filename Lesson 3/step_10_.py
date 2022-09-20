# *args, **kwargs

def add_currency(price, currency='rub', *args, **kwargs):
    print('args:  ', *args)
    print('kwargs:', *kwargs)
    print('--------------------------------------')
    return f'{price} {currency}'


price = 15.9

# print(add_currency(price))
# print(add_currency(price, 'rub'))
# print(add_currency(0, currency='smf'))
print(add_currency(5500, brackets=True, currency='smf'))

print(add_currency(5500, 'rub', 456, 2342, currency_smf='smf', currency_smf2='smf'))

print(2, 3, 4, 5, sep='_')

lst = [1, 2, 3]
print(*lst)

dct = {'currency_smf': 'smf', 'currency_smf2': 'smf'}
print(*dct.keys())
print(*dct.values())
