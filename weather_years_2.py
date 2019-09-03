import requests

url="http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/tas/1980/1999/BRA.csv"

# Usando requests
csv = requests.get(url).text
linhas = csv.splitlines()
header = linhas[0]

dict_valores = {}


for linha in linhas[1:]:
    colunas = linha.split(',')
    q1 = sum(map(float, colunas[4:7]))
    q2 = sum(map(float, colunas[7:10]))
    q3 = sum(map(float, colunas[10:14]))
    q4 = sum(map(float, colunas[14:]))
    dict_valores = [colunas[0], (q1,q2,q3,q4)]
print(dict_valores)
