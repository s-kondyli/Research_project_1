import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_excel('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/Python/Results_python.xlsx', sheet_name='Table_with_patients')
data['Read_counts'].fillna(0, inplace=True) #fill all NaN values with 0
# Calculate the range of the x ticks
min_val = data.Read_counts.min()
max_val = data.Read_counts.max()
val_width = max_val - min_val
median = data.Read_counts.median()
n_bin = 15 #number of bins to be displayed 
bin_width = val_width/n_bin
plt.hist(data['Read_counts'], bins=n_bin, log=True, edgecolor='black') 
# Plot and show the median read_count value
plt.axvline(median, color='r', label='Median read count')
plt.legend()
plt.xticks(np.arange(min_val-bin_width, max_val+bin_width, bin_width)) # caclulates a range for the xticks
plt.title('Distribution of read counts')
plt.ylabel('Number of samples')
plt.xlabel('Read counts')
plt.tight_layout()
#plt.show()
plt.savefig('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/Python/Plots/Histogram_read_counts_distribution', dpi=1200)
