import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_excel(sys.argv[1], sheet_name='Kraken_EukRep')
# Preping for the barplot
w = 0.5 # width of the bar
labels = data['sample'].tolist()
x = np.arange(data['sample'].nunique()) # for the x coordinates of the bars
h = round(data['perc_EukRep'],1) # h for height of the bars aka the values on the y axis
h2 = round(data['perc_kraken'],1)
# Creating the barplot
fig, ax = plt.subplots()
ax.bar(x, h, color='darkgrey', width=w, label='EukRep') #label to know which category is represented by each bar
ax.bar(x+w, h2, color='skyblue', width=w, label='kraken') # x+w gia na paei to 2bar sta deksia toso oso einai to platos toy kathe bar kai einai kollhta etsi
ax.set_xticks(ticks=x, labels=labels, rotation=25, fontsize=9)
ax.set_yticks(np.arange(0,110,10))
ax.set_ylabel('% of total number of contigs')
ax.set_xlabel('Samples')
ax.set_title('Percetange of fungi positive on a per patient basis & overall')
ax.legend()
plt.tight_layout()
plt.show()
