import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_excel('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/Results from assembly step/contigs_reads.xlsx', sheet_name='Kraken_EukRep')
labels = data['sample'].tolist()
x = np.arange(data['sample'].nunique())
plt.bar(x, data.Percent_of_kraken, color='g', label='kraken', width=0.7)
plt.xticks(ticks=x, labels=labels, rotation=45, fontsize=6)
#plt.bar(x+w,data.Percent_overlap_EukRep, color='b', label='EukRep', width=w)
plt.title('Percetage of kraken contigs \n that are also found with Eukrep')
plt.ylabel('(%)')
plt.xlabel('Samples')
plt.legend()
plt.tight_layout()
#plt.show()
plt.savefig('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/Python/Plots/barplot_kraken.png', dpi=1200)
