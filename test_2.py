import json
import requests
import pprint

#let's try to get the response 1st test whats up dawg?
response = requests.get("https://api.opendota.com/api/matches/6776595085")
heroes = requests.get("https://api.opendota.com/api/heroes")

with open('response.txt', 'w') as f:
  json.dump(response.json(), f, ensure_ascii=False)

with open('heroes.txt', 'w') as f:
  json.dump(heroes.json(), f, ensure_ascii=False)

#after runnign this file:
#1) install Json Editor VsCode extension
#2) open response.txt
#3) from VsCode "command pallette" (google what it is) run ">Start JSON editor session"
