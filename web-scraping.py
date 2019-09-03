import requests

url = "http://climatedataapi.worldbank.org/climateweb/rest/v1/country/mavg/tas/1980/1999/BRA.csv"

csv = requests.get(url).json
print(csv)

