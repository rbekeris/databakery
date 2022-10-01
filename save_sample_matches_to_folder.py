import json
import requests
import pprint

#let's try to get the response 1st test whats up dawg?
response = requests.get("https://api.opendota.com/api/players/1163336706/matches")

all_match_ids = []
for i in response.json():
  match_id = i['match_id']
  all_match_ids.append(match_id)

for id in all_match_ids[0:20]:
  match_data = requests.get("https://api.opendota.com/api/matches/{match_id}".format(match_id = id)).json()
  with open('./Sample_matches/{match_id}.txt'.format(match_id = id), 'w') as f:
    json.dump(match_data, f, ensure_ascii=False)

