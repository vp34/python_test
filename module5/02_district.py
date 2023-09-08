# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join


from homework_skillbox.module5.district.central_street.house1.room1 import folks as house_1_room_1
from homework_skillbox.module5.district.central_street.house1.room2 import folks as house_1_room_2
# print(f"в house_1_room_1 живут {house_1_room_1}")
# print(f"в house_1_room_1 живут {house_1_room_2}")


from homework_skillbox.module5.district.soviet_street.house1.room1 import folks as soviet_house1_room1
# print(f"в soviet_house1_room1 живут {soviet_house1_room1}")

all_folks = house_1_room_1 + house_1_room_2
print(all_folks)
print(", ".join(all_folks))


