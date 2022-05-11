import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height.""" ## optional 
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
data = pd.read_excel('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/Results from assembly step/contigs_reads.xlsx', sheet_name='Kraken_EukRep')
labels = data['sample'].tolist()
x = np.arange(data['sample'].nunique())
y = round(data['Percent_of_EukRep'],1)
fig, ax = plt.subplots()
rect = ax.bar(x, y, color='g', width=0.7)
ax.set_xticks(ticks=x, labels=labels, rotation=45, fontsize=6)
ax.set_title('Percetage of overlapping contigs in EukRep')
ax.set_ylabel('(%)')
ax.set_xlabel('Samples')
ax.legend()
#ax.set_yscale('log') # scale either x or y axis
plt.tight_layout()
autolabel(rect) # optional if you want the each bar value to be displayed
#plt.show()
plt.savefig('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/Python/Plots/barplot_EukRep.png', dpi=1200)
