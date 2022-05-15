import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#Creating the dataframe 
mean_depth = []
patients = []
sheet_dict = pd.read_excel(sys.argv[1], sheet_name=None)
for key, value in sheet_dict.items():
    depth = value.at[1,'contig_depth']
    mean_depth.append(depth)
    patients.append(key)

data = pd.DataFrame({'patients': patients, 'mean_depth': mean_depth})
# Plotting 
def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height.""" ## optional
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
labels = data['patients'].tolist()
x = np.arange(data['patients'].nunique())
y = round(data['mean_depth'],1)
fig, ax = plt.subplots()
rect = ax.bar(x, y, color='hotpink', width=0.7)
ax.set_xticks(ticks=x, labels=labels, rotation=45, fontsize=6)
#ax.set_title('Percetage of overlapping contigs in EukRep')
ax.set_ylabel('Mean contig depth')
ax.set_xlabel('Samples')
ax.legend()
#ax.set_yscale('log') # scale either x or y axis
plt.tight_layout()
autolabel(rect) # optional if you want the each bar value to be displayed
plt.show()
