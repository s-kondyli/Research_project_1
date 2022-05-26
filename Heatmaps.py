import pandas as pd
import sys
import matplotlib.pyplot as plt
import seaborn as sns
from skbio.stats.composition import clr, multiplicative_replacement

data = pd.read_excel(sys.argv[1])
data = data[data['Name'].notna()]
data = data[['Name', 'Day_related_to_HCT', 'Read_counts']]
data = data.pivot(index='Day_related_to_HCT', columns='Name', values='Read_counts').T
data = data.fillna(0)
index = data.index.tolist() # for the scaled dataframe 
columns = data.columns.tolist() # for the scaled dataframe 

#Replace all zeros with small non-zero values
data = multiplicative_replacement(data)

data = clr(data)

scaled_datadf = pd.DataFrame(data, index=index, columns=columns , yticklabels=True) #yticklabels for all taxa to appear
sns.heatmap(scaled_datadf, cmap='BuPu', linewidth=0.7)
plt.xticks(rotation=0, fontsize=4) # rotation & size of the ticks
plt.yticks(rotation=4, fontsize=6)
plt.ylabel('Taxa')
plt.xlabel('Day related to HCT')
plt.title('Patient 668 Heatmap')
plt.tight_layout()
#plt.show()
plt.savefig('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/Python/Plots/Patient_1179_Heatmap.png' , dpi=1200)
