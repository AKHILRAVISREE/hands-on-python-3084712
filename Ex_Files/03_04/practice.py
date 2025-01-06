import csv
import json
from pprint import pprint

store_laurt = []

with open("laureates.csv","r") as f:
  read = csv.DictReader(f)
  laureate = list(read)

#pprint(laureate)

for lau in laureate:
  if lau['name'][0] == "A":
    store_laurt.append(lau)

with open("laur.json","w") as f:
  json.dump(store_laurt,f,indent=2)
