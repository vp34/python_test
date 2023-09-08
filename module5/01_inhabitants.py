# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...


# from room_1 import folks as room_1_folks
# from room_2 import folks as room_2_folks
# print(f"в комнате room_1 живут {room_1_folks}")
# print(f"в комнате room_2 живут {room_2_folks}")
#


from homework_skillbox.module5.district.central_street.house1.room1 import folks as house_1_room_1
from homework_skillbox.module5.district.central_street.house1.room2 import folks as house_1_room_2
# print(f"в house_1_room_1 живут {house_1_room_1}")
# print(f"в house_1_room_1 живут {house_1_room_2}")


from homework_skillbox.module5.district.soviet_street.house1.room1 import folks as soviet_house1_room1
# print(f"в soviet_house1_room1 живут {soviet_house1_room1}")

all_folks = house_1_room_1 + house_1_room_2
print(all_folks)
print(", ".join(all_folks))