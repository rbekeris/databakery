import json
import requests
import pprint

#let's try to get the response 1st test whats up dawg?
response = requests.get("https://api.opendota.com/api/matches/6776595085")


pprint.pprint(response.json())