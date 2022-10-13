import json
import datetime
import os
import plotly.express as px
import pandas as pd

# I would like to create a dictionary that contains the date of the match as key, and the GPM as value:
# First, I create an empty dictionary. 
date_gpm = {}

#Next, I go through each file in 'Sample_Matches' and find the relevant data I need. 
# Important to mention is that the account id is manually entered/selected.
for filename in os.listdir('Sample_Matches'):
    with open(str('Sample_Matches/'+filename)) as f:
        data = json.load(f)
        date_ep = data['start_time']
        # since start_time is in epoch format, I want to switch it to regular datetime.
        date = datetime.datetime.fromtimestamp(date_ep).strftime('%Y-%m-%d %H:%M:%S')
        # the .txt file contains a dictionary for each player, so I need to iterate through each till I find the  account
        # id I need. 
        for i in range(0,len(data['players'])):
            if data['players'][i]['account_id'] == 1163336706:
                gpm = data['players'][i]['gold_per_min']
        # I add the key:value pair to the dict. 
        date_gpm[date] = gpm

print(date_gpm)

dict_data_final = {'Date': date_gpm.keys(), 'GPM': date_gpm.values()}

df = pd.DataFrame.from_dict(dict_data_final)
df = df.sort_values(by="Date")

plot = px.scatter(df,
                  x='Date', 
                  y='GPM'
                 ) 

# create a figure with all plots and display it
plot.show()

fig = px.line(df, x='Date', y='GPM')
fig.show()