import json
import requests
from sqlalchemy import create_engine
import numpy as np
from dotenv import load_dotenv
import os
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import MetaData
from sqlalchemy import insert
from sqlalchemy.dialects import postgresql

load_dotenv()
db_connection_string = os.getenv('SQLALCHEMY_DATABASE_URL_FROM_OUTSIDE_CONTAINER_NETWORK')
engine = create_engine(db_connection_string)
heroes_table = Table("heroes",
                    MetaData(),
                    Column("id",Integer, primary_key =True),
                    Column("name",String),
                    Column("localized_name",String),
                    Column("primary_attr",String),
                    Column("attack_type",String),
                    Column("roles",Integer, postgresql.ARRAY(String)),
                    schema="core_schema")

heroes = requests.get("https://api.opendota.com/api/heroes").json()

for hero in heroes:
    id = hero['id']
    name = hero['name']
    localized_name = hero['localized_name']
    primary_attr = hero['primary_attr']
    attack_type = hero['attack_type']
    roles = hero['roles']

    stmt = stmt = insert(heroes_table).values(id = id,
                                                    name = name, 
                                                    localized_name = localized_name,
                                                    primary_attr = primary_attr,
                                                    attack_type = attack_type,
                                                    roles = roles)
    with engine.connect() as conn:
        result = conn.execute(stmt)
