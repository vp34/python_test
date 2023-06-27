# есть список животных в зоопарке
# print('hello world')
zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]
print(zoo)
# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
zoo.insert(1, 'bear')
print(zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
zoo.extend(birds)
print(zoo)

# уберите слона
#  и выведите список на консоль
# zoo.remove('lion')
# print(zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
print("лев сидит в клетке " + str(zoo.index('lion')+1))
print("жаворонок сидит в клетке " + str(zoo.index('lark')+1))

