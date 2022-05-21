import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
sheet_dict = pd.read_excel(sys.argv[1], sheet_name=None)
patient = []
depth = []
for key, value in sheet_dict.items():
    patient.append(key)
    depth.append(value.at[1,'contig_depth'])

data = pd.DataFrame({'patients':patient,'mean_depth':depth})
plt.hist(data['mean_depth'],edgecolor='black', color='skyblue')
plt.title('kraken mean contig depth')
plt.ylabel('Number of contigs')
plt.xlabel('Mean contig depth')
plt.xticks(np.arange(0,22,2))
plt.yticks(np.arange(0,12,2))
plt.tight_layout()
plt.show()
