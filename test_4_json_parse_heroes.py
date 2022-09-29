import json
import requests
import pprint

#I want to get a list of heroes based on a certain criteria. 
# Here, I want all Melee heroes:

# Step 1: Get all heroes data from opendotaapi.
heroes = requests.get("https://api.opendota.com/api/heroes")

# Step 2: Save the heroes data in a .txt file: 
with open('heroes.txt', 'w') as f:
  json.dump(heroes.json(), f, ensure_ascii=False)

# Step 3: Open .txt file using 'r' read-mode. 
# Here 'r' is not mentioned because it is the default:
with open('heroes.txt') as f:

# Step 4: Store the data in a variable. Here, it is a list of dicts:
  data = json.load(f)
# I also want to store the list of heroes in a file. So I start with an empty list and add the heroes there:
  hero_list = []
# Step 5: Look at the .txt file using json editor and select the key:value pairs you need:
# Here, I need key: 'attack_type' value: 'Melee', and I want to also see the hero name and id:
  for i in data:
      if i['attack_type'] == 'Melee':
          print('Hero id:',i['id'],'hero name:',i['localized_name'],'attack type:',i['attack_type'])
          hero_list.append(i['localized_name'])

# Step 6. I save the final list of Melee heroes in a .txt file:
  with open('melee_heroes.txt', 'w') as f:
    json.dump(hero_list, f, ensure_ascii=False)