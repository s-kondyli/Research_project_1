import pandas as pd
import matplotlib.pyplot as plt
import sys
import numpy as np
data = pd.read_excel(sys.argv[1])
data = data.fillna(0)
data = data[['taxa', 'mean']]
data = data.set_index('taxa')

fig, ax = plt.subplots()
ax = data.plot.barh(color='g')
x = np.arange(0,110,10) # to show from 0-100% in the x axis ticks
ax.set_ylabel('Taxa')
ax.set_xlabel('Percentage of the bases with at least one aligned read')
ax.set_xticks(x)
plt.tight_layout()
plt.show()
