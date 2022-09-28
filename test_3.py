import json
import requests
import pprint

#I want to get the benchmarks for lich. First, I get all heroes to find Lich's hero_ID. It's 31.
heroes = requests.get("https://api.opendota.com/api/heroes")

# Then I query the benchmarks for that hero_id:
benchmarks_lich = requests.get("https://api.opendota.com/api/benchmarks?hero_id=31")

# Then we save both as .txt and open with json editor. 
with open('heroes.txt', 'w') as f:
  json.dump(heroes.json(), f, ensure_ascii=False)

with open('benchmarks_lich.txt', 'w') as f:
  json.dump(benchmarks_lich.json(), f, ensure_ascii=False)