import json
import requests
from sqlalchemy import create_engine
import numpy as np

engine = create_engine('conn_string_here')

heroes = requests.get("https://api.opendota.com/api/heroes").json()

for hero in heroes:
    id = hero['id']
    name = str(hero['name'])
    localized_name = str(hero['localized_name'])
    attack_type = str(hero['attack_type'])
    #roles = hero['roles']

    engine.execute('''INSERT INTO core_schema.heroes (id,
                                                    name,
                                                    localized_name,
                                                    attack_type)
                    VALUES ({id},
                            {name},
                            {localized_name},
                            {attack_type}
                            );
                    '''.format(
                        id = id,
                        name = name, 
                        localized_name = localized_name,
                        attack_type = attack_type
                    ))