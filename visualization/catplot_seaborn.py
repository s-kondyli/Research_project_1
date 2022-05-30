import sys
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel(sys.argv[1], sheet_name='Kraken_EukRep')
data = data[['sample','EukRep_contigs','Kraken_contigs','overlapping_contigs']]
df = pd.melt(data, id_vars ='sample')
sns.catplot(x='sample', y='value', hue ='variable',data=df, kind='bar',legend=False, palette='pastel')
plt.yscale('log')
plt.ylabel('Number of contigs\n (log scale)')
plt.xlabel('Samples')
plt.xticks(rotation=45, fontsize=8)
plt.legend(loc='upper right', fontsize=10)
plt.tight_layout()
plt.show()
