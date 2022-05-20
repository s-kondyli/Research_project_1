import pandas as pd
import matplotlib.pyplot as plt
import sys
import numpy as np
data = pd.read_excel(sys.argv[1])
data = data.fillna(0)
y = np.arange(0,110,10)
x = np.arange(0,1400,200)
mean = data['percent_observed'].mean()
plt.axhline(mean, color='salmon', label='mean %')
plt.legend()
plt.scatter(data.Read_counts, data.percent_observed, c='g', s=15)
plt.xlabel('Number of aligned reads')
plt.ylabel('Percentage of marker genes observed')
plt.yticks(y)
plt.xticks(x)
plt.tight_layout()
plt.tight_layout()
plt.show()
