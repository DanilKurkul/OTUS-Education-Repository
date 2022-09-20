# comprehensions

a = 5
b = 'five'
print(a, b)

a, b = 5, 'five'
print(a, b)

a, b = b, a
print(a, b)

products = ['iphone', 'macbook', 's21', 'redmi note 8']

products_upper = []

for item in products:
    if item != 'macbook':
        products_upper.append(item.upper())

print(products)
print(products_upper)

products_upper_2 = [item.upper() for item in products if item != 'macbook']

print(products_upper_2)

