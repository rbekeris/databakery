import json

date_gpm = {}

with open('Sample_Matches/6779631970.txt') as f:
    data = json.load(f)
    date = data['start_time']
    for i in range(0,len(data['players'])):
        if data['players'][i]['account_id'] == 872190418:
            gpm = data['players'][i]['gold_per_min']
    date_gpm[date] = gpm
    print(date_gpm)