import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/EukDetect/crosstab_Euk.csv')
# Preping for the barplot
w = 0.5 # width of the bar
labels = data['patients'].tolist()
x = np.arange(data['patients'].nunique()) # for the x coordinates of the bars 
h = round(data['overall_perc_positive'],1) # h for height of the bars aka the values on the y axis
h2 = round(data['overall_perc_negative'],1)
# Creating the barplot
fig, ax = plt.subplots()
rect = ax.bar(x, h, color='#C79FEF', width=w, label='positive') #label to know which category is represented by each bar 
rect2 = ax.bar(x+w, h2, color='#C5C9C7', width=w, label='negative') # x+w gia na paei to 2bar sta deksia toso oso einai to platos toy kathe bar kai einai kollhta etsi 
ax.set_xticks(ticks=x, labels=labels, rotation=25, fontsize=9)
ax.set_ylabel('%')
ax.set_xlabel('Patients')
ax.set_title('Percetange of fungi positive & negative samples \n (out of all samples)') 
ax.legend()
plt.show()
#plt.savefig('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/Python/Plots/read_counts_taxa.png', dpi=1200)
