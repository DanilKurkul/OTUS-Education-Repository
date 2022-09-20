# поименное указание аргумента

def add_currency(price, currency='rub', brackets=False):
    if brackets:
        return f'{price} ({currency})'
    return f'{price} {currency}'


price = 15.9

print(add_currency(price))
print(add_currency(price, 'rub'))
print(add_currency(0, currency='smf'))
print(add_currency(5500, 'smf'))
print(add_currency('5500'))
print(add_currency(5500, brackets=True, currency='smf'))


