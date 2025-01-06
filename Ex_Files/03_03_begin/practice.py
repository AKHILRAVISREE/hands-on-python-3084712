import csv
import json

with open("laureates.csv","r") as f:
  reader = csv.DictReader(f)
  laureate = list(reader)

  with open("laur.json", "w") as f:
    json.dump(laureate, f, indent=2)
