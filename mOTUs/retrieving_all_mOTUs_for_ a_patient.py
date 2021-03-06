import pandas as pd
import numpy as np 

# Filtering the original mOTUs.s.tsv file to keep only the species level with split
motus_df = pd.read_csv('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/mOTUs.s.tsv', sep='\t')
motus_df['Unnamed: 0'] = motus_df['Unnamed: 0'].str.rsplit('|',1).apply(lambda x:x[1])

# Reshape the data so that are in 3 columns: Species (Unnamed: 0), Patient ID, Read_counts
motus_df = motus_df.melt(id_vars='Unnamed: 0', var_name='Patient_ID', value_name='Read_counts')

# Import data from excel files & specifying sheet for patient of interest
data = pd.read_excel('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/Python/Results_python.xlsx', sheet_name='Patient_1042')

# Filter out of the mOTUs_df the patient ID we are interested in each time
values = data['Patient_ID']
data_bacteria = motus_df[motus_df['Patient_ID'].isin(values)]
data_bacteria = data_bacteria.replace(0, np.nan) # replaces 0 with NaN values
data_bacteria = data_bacteria[data_bacteria['Read_counts'].notna()] # drops NaN values from column Read_counts 

#Save the filtered dataframe to a file
data_bacteria.to_csv('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/mOTUs/bacteria_1042_Patient.csv', index=False)
