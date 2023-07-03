# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 530),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2


x1 = sites['Moscow'][0]
y1 = sites['Moscow'][1]

x2 = sites['London'][0]
y2 = sites['London'][1]
distance = {}

for city_1, coordinates_1 in sites.items():
    distance[city_1] = {}
    for city_2, coordinates_2 in sites.items():
        if city_1 != city_2:
            x1 = coordinates_1[0]
            y1 = coordinates_1[1]
            x2 = coordinates_2[0]
            y2 = coordinates_2[1]
            city_1_to_city_2 = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            distance[city_1][city_2] = round(city_1_to_city_2, 2)
print(distance)

        #print(f"from {city_1} to {city_2} distance = {city_1_to_city_2}")

#    for city_2, coordinates_2 in sites.items():
 #       if city_1 != city_2:
  #          x2, y2 = coordinates_2
   #         city_1_to_city_2 = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    #        distance[city_1][city_2] = city_1_to_city_2








# Distance:{
#     'Moscow': {
#         'London': distance btw Moscow & London
#         'Paris': distance btw Moscow & Paris
#         }
#     'London': {
#         'Moscow': distance btw London & Moscow
#       'Paris': distance btw London & Paris
#         }
#     'Paris': {
#        'London': distance btw Paris & London
#       'Moscow': distance btw Paris & Moscow
#   }
#   }




# for site_1 in sites:
#   site_1_x, site_1_y = site_1
#   for site_2 in sites:
#       site_2_x, site_2_y = site_2
#       distance_1 = math.sqrt((site_1_x - site_2_x) ** 2 + (site_1_y - site_2_y) ** 2)
#       print(distance_1)




# print(distances)




