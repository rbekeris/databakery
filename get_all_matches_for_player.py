import json
import requests
import pprint

#let's try to get the response 1st test whats up dawg?
response = requests.get("https://api.opendota.com/api/players/1163336706/matches")

all_match_ids = []
for i in response.json():
  match_id = i['match_id']
  all_match_ids.append(match_id)

players_bank = []
for id in all_match_ids[0:10]:
  print("retrieving match with id: {id}".format(id = id))
  match_data = requests.get("https://api.opendota.com/api/matches/{match_id}".format(match_id = match_id)).json()
  for player in match_data['players']:
    players_bank.append(player['account_id'])


print(players_bank)