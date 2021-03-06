import pandas as pd

# Filtering the original mOTUs.s.tsv file to keep only the species level with split 
motus_df = pd.read_csv('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/mOTUs.s.tsv', sep='\t')
motus_df['Unnamed: 0'] = motus_df['Unnamed: 0'].str.rsplit('|',1).apply(lambda x:x[1])

# Reshape the data so that are in 3 columns: Species (Unnamed: 0), Patient ID, Read_counts
motus_df = motus_df.melt(id_vars='Unnamed: 0', var_name='Patient_ID', value_name='Read_counts')

# Import data from excel files & specifying sheet for patient of interest
data = pd.read_excel('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/Python/Results_python.xlsx', sheet_name='Patient_1179')

# Filter out of the mOTUs_df the patient ID we are interested in each time
values = data['Patient_ID']
data_bacteria = motus_df[motus_df['Patient_ID'].isin(values)]

# Group by patient_ID & sort read counts in a descending order 
df2 = data_bacteria.sort_values('Read_counts', ascending=False).groupby(['Patient_ID'])

# For each group on the column Unnamed:0 which represents the species replace each taxon name  from the 4rth row on with "others" 
df3 = pd.DataFrame(columns=data_bacteria.columns)
for patient, group in df2:
    group.iloc[3:, group.columns.get_loc('Unnamed: 0')] = 'Others'
    df3 = df3.append(group,ignore_index=True)
df3.sort_values('Read_counts', ascending=False)

#Sums the reads of each group based on the column name  
df4 = df3.groupby(['Patient_ID','Unnamed: 0'])['Read_counts'].sum().reset_index()

#Save the filtered dataframe to a temporary file 
df4.to_csv('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/mOTUs/topbacteria_1179_patient.csv', index=False)
