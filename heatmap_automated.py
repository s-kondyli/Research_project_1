import sys
import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns
from skbio.stats.composition import clr, multiplicative_replacement
sheet_dict = pd.read_excel('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/mOTUs/ordered/All_patients_top3_ordered.xlsx', sheet_name=None)
for key, value in sheet_dict.items():
    x = re.findall(r'\d+', key)
    i = x[0]
    value = value.set_index('Name')  # reseting the index
    index = value.index  # storing the index into a list for the scaled_df for the plot
    columns = value.columns.tolist()  # storing the columns into a list for the scaled_df for the plot
    # Log-scaling the data
    value = multiplicative_replacement(value)  # replaces all zeros with small-non-zero-values
    value = clr(value)  # center-log ratio transformation
    # Creating the new scaled_df
    scaled_df = pd.DataFrame(value, index=index, columns=columns)
    # Plotting the heatmap
    sns.heatmap(scaled_df, cmap='BuPu', linewidth=0.7, yticklabels=True, xticklabels=True)  # yticklabels for all taxa to appear
    plt.xticks(rotation=0, fontsize=4)  # rotation & size of the ticks
    plt.yticks(rotation=4, fontsize=6)
    plt.ylabel('Taxa')
    plt.xlabel('Day related to HCT')
    plt.title('Patient_' + i + '_Heatmap')
    plt.tight_layout()
    plt.show()
    #plt.savefig('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/Python/Patient_'+i+'_Heatmap.png', dpi=1200)
