# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =

garden_set = set(garden)
meadow_set = set(meadow)

print(garden_set)
print(meadow_set)

# выведите на консоль все виды цветов
all_flowers = garden_set | meadow_set
print(all_flowers)

# выведите на консоль те, которые растут и там и там
duplicate_flowers = garden_set & meadow_set
print(duplicate_flowers)

# выведите на консоль те, которые растут в саду, но не растут на лугу
unique_garden = garden_set - meadow_set
print(unique_garden)

# выведите на консоль те, которые растут на лугу, но не растут в саду
unique_meadow = meadow_set - garden_set
print(unique_meadow)

