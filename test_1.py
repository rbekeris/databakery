import json
import requests
import pprint

#let's try to get the response 1st test whats up dawg?
response = requests.get("https://api.opendota.com/api/matches/6776595085")
response2 = requests.get("https://api.opendota.com/api/matches/6778264672")

pprint.pprint(response.json())
pprint.pprint(response2.json())