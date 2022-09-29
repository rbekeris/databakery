import json
import requests
import pprint

#I want to get the benchmarks for lich. First, I get all heroes to find Lich's hero_ID. It's 31.
schema = requests.get("https://api.opendota.com/api/schema")

# Then we save both as .txt and open with json editor. 
with open('schema.txt', 'w') as f:
  json.dump(schema.json(), f, ensure_ascii=False)