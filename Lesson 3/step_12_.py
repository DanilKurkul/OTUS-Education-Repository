# map, filter
# lambda

products = [15.9, 16.9, 155.5, 5555.5]

products_2 = map(int, products)
print(products_2)  # O(1)
# print(*products_2)  # O(n)
# print(*products_2)

# print(list(products_2))  # O(n)
# print(sum(list(products_2)))  # O(n)
print(sum(products_2))  # O(1)


# lambda
def func_int(value):
    return int(value**2)


products_3 = map(func_int, products)
print(*products_3)

products_3 = map(lambda x: int(x**2), products)
print(*products_3)

products_3 = filter(lambda x: x > 100, products)
print(*products_3)





