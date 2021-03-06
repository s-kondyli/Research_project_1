import pandas as pd
data = pd.read_excel('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/Python/Results_python.xlsx', sheet_name='Table_with_patients')
data = data[['Name', 'Day_related_to_HCT', 'Read_counts', 'Patient_ID']]
data = data[data['Name'].notna()] # drops NaN values from the column
data['Name'] = data['Name'].str.strip()
data = data.loc[~data['Name'].str.contains('none')]
data['Patients'] = data.Patient_ID.str.extract('(\d+)') # extracts only the numbers out of each row of the x column (series object)
data = pd.crosstab(index=data.Name, columns=data.Patients, margins=True, normalize=False)
data.to_csv('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/EukDetect/crosstab_EukDetect_taxa.csv')
