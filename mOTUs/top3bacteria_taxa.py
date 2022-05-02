import pandas as pd
motus_df = pd.read_csv('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/mOTUs/bacteria_653_Patient.csv')

# Group by patient_ID & sort read counts in a descending order
data = motus_df.sort_values('Read_counts', ascending=False).groupby(['Day_related_to_HCT'])

# For each group on the column Unnamed:0 which represents the species replace each taxon name  from the 4rth row on with "others"
df = pd.DataFrame(columns=motus_df.columns)
for patient, group in data:
    group.iloc[3:, group.columns.get_loc('Name')] = 'Others'
    df = df.append(group,ignore_index=True)
df.sort_values('Read_counts', ascending=False)

#Sums the reads of each group based on the column name
df = df.groupby(['Day_related_to_HCT','Name'])['Read_counts'].sum().reset_index()

#Save the filtered dataframe to a desired file 
df.to_csv('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/mOTUs/topbacteria_653_patient.csv', index=False)
