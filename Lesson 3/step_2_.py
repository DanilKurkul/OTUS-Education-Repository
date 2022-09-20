# • строки: str

print(complex('1+2j'))
print(str('1+2j'))

len_room = 5.933
width_room = 3.333

print('Длина комнаты 4.5 м и ширина комнаты 3 м')
print(f'Длина комнаты {len_room} м и ширина комнаты {width_room} м')
print('Длина комнаты {len_room} м и ширина комнаты {width_room} м'.format(len_room=len_room, width_room=width_room))
print('Длина комнаты ' + str(len_room) + ' м и ширина комнаты ' + str(width_room) + ' м')
print()
print('Длина комнаты %s м и ширина комнаты %s м' % (len_room, width_room))
print('Длина комнаты %i м и ширина комнаты %d м' % (len_room, width_room))
print('Длина комнаты %r м и ширина комнаты %s м' % (len_room, width_room))
