import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
sheet_dict = pd.read_excel(sys.argv[1], sheet_name=None)
patient = []
median_length = []
for key, value in sheet_dict.items():
    patient.append(key)
    length = value['contig_length'].median()
    median_length.append(length)

data = pd.DataFrame({'patients':patient,'median_length':median_length})

data = data.set_index('patients')
fig, ax = plt.subplots()
ax = data.plot.barh(color='royalblue')
ax.set_title('EukRep contigs')
ax.set_ylabel('Samples')
ax.set_xlabel('Median length in bp')
plt.tight_layout()
plt.show()

