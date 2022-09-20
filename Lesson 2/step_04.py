# стремиться избегать else
# пример с else и без else

age = 19
access_login = False
part_access_login = False

if age >= 18:
    print('Доступ разрешен')
    access_login = True
elif 16 <= age <= 17:
    print('Частичный доступ')
    part_access_login = False

print(access_login, part_access_login)


