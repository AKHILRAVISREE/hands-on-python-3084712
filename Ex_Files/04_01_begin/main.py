import requests
import json

response = requests.get(
    "http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json",
)

last_twenty_years = response.json()[1][:20]

for year in last_twenty_years:
  val = year["value"]
  print(f'{year["date"]}: {year["value"]}', "="*val)

