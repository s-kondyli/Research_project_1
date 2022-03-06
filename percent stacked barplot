import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
import seaborn as sns
import re

#calculates the percentage of tha daily total reads of each taxon
dict_counts={}
grouped=df.groupby("Day_related_to_HCT")
for day,group in grouped:
    dict_counts[day]='x'
newgroup=df.groupby("Day_related_to_HCT").sum()
for key,value in dict_counts.items():
    dict_counts[key]=newgroup.loc[key]['Read_counts']
df['corresp_sum']=df['Day_related_to_HCT'].map(dict_counts)
df['percent']=df.apply(lambda row: row.Read_counts/row.corresp_sum*100 if row.corresp_sum !=0 else 0,axis=1)

#make a color dictionary
list_categories = df['Name'].unique().tolist()
list_colors = ['tomato', 'floralwhite', 'lightgray', 'gold','darkkhaki','olive','bisque','beige','honeydew','mintcream','azure','lightcyan','navy','lavenderblush','pink','thistle','linen','seashell','cornsilk','tan','white','mistyrose','sienna','snow','aliceblue', 'lightgreen']
zipobj = zip(list_categories, list_colors)
color_dict = dict(zipobj)
#make a percent stacked plot 
df1=df.groupby(['Day_related_to_HCT','Name'])['percent'].sum().unstack()
df1.plot.bar(stacked = True, color = colors, figsize = (20, 10))
plt.legend(bbox_to_anchor=(1.04,1), loc="upper left", prop={'size':8}) #places the legend outside of the axes of the plot in the upper left corner
plt.title('Patient 1179 microbiota composition over time')
plt.xlabel('Day related to HCT')
plt.tight_layout()
plt.ylabel('% of read counts')

#saves figure in desired path 
plt.savefig('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/Python/Plots/filename.png', dpi=1200)
