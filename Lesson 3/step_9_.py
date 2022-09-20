# Изменяемые объекты в аргументах по умолчанию

def append_to_list(value, my_list=[0]):
    """
    Добавить значение в конец списка. В случае отсуствия второго аргумента список должен быть пустой
    :param value:
    :param my_list:
    :return:
    """

    my_list2 = my_list.copy()
    my_list2.append(value)
    print(my_list2, id(my_list2))

testlist = [1]
testlist2 = testlist.copy()

append_to_list(77)
append_to_list(99)
append_to_list(111)
append_to_list(111, [1, 2, 3])
append_to_list(222)

a = [5]
b = []
a[0] = 3
print(f'b: {b}, id = {id(b)}')


def append_to_list(value, my_list=None):
    """
    Добавить значение в конец списка. В случае отсуствия второго аргумента список должен быть пустой
    :param value:
    :param my_list:
    :return:
    """

    # if my_list is None:
    #     my_list = []
    my_list = [] if my_list is None else my_list
    my_list.append(value)
    print(my_list, id(my_list))


append_to_list(77)
append_to_list(99)
append_to_list(111)
append_to_list(111, [1, 2, 3])
append_to_list(222)




