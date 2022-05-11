import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_excel('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/Results from assembly step/contigs_reads.xlsx', sheet_name='Kraken_EukRep')
labels = data['sample'].tolist()
x = np.arange(22)
w = 0.5
plt.bar(x,data.Percent_overlap, color='g', label='kraken',width=w)
plt.bar(x+w,data.Percent_overlap_EukRep, color='b', label='EukRep', width=w)
plt.xticks(ticks=x, labels=labels, rotation=30, fontsize=5)
plt.legend()
plt.tight_layout()
plt.show()
