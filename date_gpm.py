import json
import datetime
import os

date_gpm = {}

for filename in os.listdir('Sample_Matches'):
    with open(str('Sample_Matches/'+filename)) as f:
        data = json.load(f)
        date_ep = data['start_time']
        type(date_ep)
        date = datetime.datetime.fromtimestamp(date_ep).strftime('%Y-%m-%d %H:%M:%S')
        for i in range(0,len(data['players'])):
            if data['players'][i]['account_id'] == 1163336706:
                gpm = data['players'][i]['gold_per_min']
        date_gpm[date] = gpm

print(date_gpm)