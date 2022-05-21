import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_excel(sys.argv[1])
labels = data['sample'].tolist()
colors = ['lightgreen','pink','slategray']
x = np.arange(data['sample'].nunique())
data = data[['sample', 'Kraken_contigs', 'overlapping_contigs', 'EukRep_contigs']]
data.plot(kind='bar', stacked=True, color=colors)
plt.xticks(ticks=x,labels=labels, rotation=48,fontsize=8)
plt.xlabel('Samples')
plt.ylabel('Number of contigs')
plt.yscale('log')
plt.tight_layout()
plt.legend(labels=['kraken','overlapping','EukRep'])
plt.show()
