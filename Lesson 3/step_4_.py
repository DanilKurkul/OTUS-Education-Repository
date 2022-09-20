# • хеш-таблицы: {dict:dict}, {set} - аналог математического множества, уникально
import timeit

digital_set = {1, 2, 3, 4, 5, 5}
str_set = {'1', '2', '3', '4', '5', '5'}  # O(1)

print(digital_set)
print(str_set)

phones = ['nokia', 'iphone', 'xiaomi', 'samsung']
print(phones)

print(timeit.timeit('8 in [1, 2, 3, 4, 5, 6, 7, 8, 9]', number=100000))
print(timeit.timeit('8 in {1, 2, 3, 4, 5, 6, 7, 8, 9}', number=100000))




