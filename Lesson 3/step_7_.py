# значения по умолчанию

def add_currency(price, currency='rub'):
    # pass
    return f'{price} {currency}'


price = 15.9

print(add_currency(price, 'rub'))
print(add_currency(5500, 'smf'))
print(add_currency('5500'))

print(add_currency(price))

print(add_currency(0, currency='smf'))

