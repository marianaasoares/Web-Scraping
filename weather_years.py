import requests

url="http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/tas/1980/1999/BRA.csv"

# Usando requests
csv = requests.get(url).text
linhas = csv.splitlines()
header = linhas[0]

for l in range(1, len(linhas)):
    colunas = linhas[l].split(',')
    valores = map(float, colunas[4:])
    print(sum(list(valores)))
    break
