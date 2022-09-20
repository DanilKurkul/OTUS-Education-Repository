# DRY (Don’t repeat yourself - не повторяйся)

def add_rub(price):  # будет предупреждение для именования price, означает, что глобальная переменная price переопределена внутри функции
    # pass
    return f'{price} rub'


price = 15.9

print(add_rub(price))
print(add_rub(5500))
print(add_rub('5500'))
