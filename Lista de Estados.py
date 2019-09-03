import rows
from collections import defaultdict

cities = rows.import_from_csv("data/brazilian-cities.csv")

inhabitants_cities = 0
lista_de_estados = []

'''for city in cities:
    lista_de_estados.append(city.state)
print(list(set(lista_de_estados)))'''

pop_estados = defaultdict(int)
for city in cities:
    pop_estados[city.state] += city.inhabitants
print(pop_estados)