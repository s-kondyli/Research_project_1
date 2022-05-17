import pandas as pd
import sys
import matplotlib.pyplot as plt
import seaborn as sns
from skbio.stats.composition import clr, multiplicative_replacement
#importing our data
sheet_dict = pd.read_excel(sys.argv[1], sheet_name=None)
for key, value in sheet_dict.items():
    patient = key
    value['name'] = value['name'].str.split('\\[ref').str[0] # \\ because [ is a special character
    value['name'] = value['name'].str.split('\\[met').str[0]
    value = value.set_index('name')   #reseting the index
    index = value.index # storing the index into a list for the scaled_df for the plot
    columns = value.columns.tolist() # storing the columns into a list for the scaled_df for the plot
    data = multiplicative_replacement(value)  # replaces all zeros with small-non-zero-values
    data = clr(data) # center-log ratio transformation
    scaled_df = pd.DataFrame(data, index=index, columns=columns) # creating the scaled_df
    sns.heatmap(scaled_df, cmap='YlGn', linewidth=0.7, yticklabels=True, square=True)  # yticklabels for all taxa to appear
    plt.xticks(rotation=0, fontsize=6)  # rotation & size of the ticks
    plt.yticks(rotation=4, fontsize=8)
    plt.ylabel('Taxa')
    plt.xlabel('Day related to HCT')
    plt.title('Patient' + ' ' + patient + ' ' + 'Heatmap') # mona autakia gia to keno
    plt.tight_layout()
    plt.show()


exit()

