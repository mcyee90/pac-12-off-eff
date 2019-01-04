
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[2]:


plays = pd.read_csv("plays.csv")
plays
scores = plays[['opponent','game_id', 'pf', 'pa', 'p_diff']]
scores


# In[3]:


schedule = pd.read_csv("schedule.csv")
schedule


# In[4]:


plays = plays.loc[plays['play_type'] != "special"]
plays = plays.loc[plays['play_type'] != "penalty"]
plays


# In[5]:


success_rate_by_down = plays.groupby(['team','wk','down','play_type'])['success'].mean()
success_rate_by_down = pd.DataFrame(success_rate_by_down)
success_rate_by_down = success_rate_by_down.reset_index()
success_rate_by_down['game_id'] = ''
for i, r in success_rate_by_down.iterrows():
    success_rate_by_down.at[i, 'game_id'] = r['wk'] + r['team']
success_rate_by_down['wk'] = success_rate_by_down['wk'].replace('P',15)
success_rate_by_down['wk'] = success_rate_by_down['wk'].astype('int32')
success_rate_by_down


# In[11]:


success = success_rate_by_down.merge(scores, left_on="game_id", right_on='game_id', how='left')
success = success.drop_duplicates().reset_index(drop = True)


# In[12]:


success


# In[21]:


teams = sorted(list(set(success['team'])))
teams


# In[27]:


colors = {"Arizona": ['#CC0033', '#003366'],
         "Arizona St.":['#8C1D40','#FFC627'],
         "California":["#003262","#FDB515"],
         "Colorado":['#CFB87C','#000000'],
         "Oregon":["#154733","#FEE123"],
         "Oregon St.":["#DC4405","#000000"],
         "Southern California":["#990000","#FFC72C"],
         "Stanford":["#8C1515","#007662"],
         "UCLA":["#2D68C4","#F2A900"],
         "Utah":["#CC0000","#808080"],
         "Washington":["#4B2E83","#B7A57A"],
         "Washington St.":["#981E32","#5E6A71"]}


# In[30]:


for t in teams:
    success_df = success.loc[success['team']==t]
    print(success_df)
    for k, v in colors.items():
        if t == k:
            c1 = v[0]
            c2 = v[1]

