
# coding: utf-8

# In[1]:


# dependencies
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import random


# In[2]:


pdx_sales_data = pd.read_csv("pdx_data.csv")

pdx_sales_data['Base Ratio'] = ""
pdx_sales_data['ARTR Ratio'] = ""
for key, value in pdx_sales_data.iterrows():
    br = float(value['Base Units']/value['Total Units'])
    ar = float(value['ARTR Units']/value['Total Units'])
    pdx_sales_data.at[key, "Base Ratio"] = br
    pdx_sales_data.at[key, "ARTR Ratio"] = ar
pdx_sales_data = pdx_sales_data.set_index(["ID"])    
pdx_sales_data.head(20)


# In[3]:


sexes = pdx_sales_data['Sex'].unique()
db_options = pdx_sales_data['DB Opt'].unique()
print (sexes)
print (db_options)
# print (pdx_sales_data['Number Of Pmts'])


# In[5]:


colors = ["blue", "pink", "green"]
shapes = ['s', '^', 'P']
legend_elements = []
fig, ax = plt.subplots(figsize=(15, 10))
for sex in np.arange(len(sexes)):
    filtered_df = pdx_sales_data.loc[pdx_sales_data['Sex']==sexes[sex]]
#     print (filtered_df.head())
    for db in np.arange(len(db_options)):
        gender_dbo_df = filtered_df.loc[filtered_df['DB Opt']==db_options[db]]
        print (sexes[sex], db_options[db], len(gender_dbo_df))
        
        leg = Line2D([0], [0], marker=shapes[db], color=colors[sex], label=f'Gender: {sexes[sex]}, DBO: {db_options[db]}', 
                     markersize=10, linewidth = 0)
        legend_elements.append(leg)
        ax.legend(handles=legend_elements, loc='upper right')
        for key, value in gender_dbo_df.iterrows():
            x = value['Total Units']
            y = value['IRR']
            nPmts = value['Number Of Pmts']
            baseRatio = value['Base Ratio']
            ax.scatter(x, y, color=colors[sex], s = nPmts*2, linewidth=1, marker=shapes[db], alpha=baseRatio)
ax.set_xlim(min(pdx_sales_data['Total Units'])-1000, max(pdx_sales_data['Total Units'])+1000)
ax.set_ylim(min(pdx_sales_data['IRR'])-1, max(pdx_sales_data['IRR'])+1)
ax.set_xlim([min(pdx_sales_data['Total Units'])-5000, max(pdx_sales_data['Total Units'])+5000])
ax.set_ylim([min(pdx_sales_data['IRR'])-.25, max(pdx_sales_data['IRR'])+.25])
ax.set_title('Total units vs. IRR', fontsize = 18)
ax.set_xlabel("Total Units", fontsize = 14)
ax.set_ylabel("IRR", fontsize = 14)
ax.tick_params(axis='both', labelsize = 12)
ax.text(max(pdx_sales_data['Total Units'])*.6, min(pdx_sales_data['IRR'])-.55,
       f'**Note**\n-- Size of the point corresponds to Number of Annual Premium Payments Made\n-- Opacity of the point corresponds to the % of Base')
ax.grid(True)
ax.set_axisbelow(True)
ax.set_facecolor('ghostwhite')
plt.savefig("sample.png")
plt.show()

