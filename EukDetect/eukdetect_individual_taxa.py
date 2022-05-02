import pandas as pd

data = pd.read_excel('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/Python/Results_python.xlsx', sheet_name='Table_with_patients')
data = data[['Name', 'Day_related_to_HCT', 'Read_counts', 'Total_marker_coverage','Patient_ID']]
data = data[data['Name'].notna()] # drops NaN values from the column
data['Name'] = data['Name'].str.strip()
data = data.loc[~data['Name'].str.contains('none')]
data['Patient'] = data.Patient_ID.str.extract('(\d+)') # extracts only the numbers out of each row of the x column (series object)
df1 = data.loc[data['Name'].str.contains('Saccharomyces cerevisiae S288C')]
df1['percent_total_marker_coverage'] = df1.Total_marker_coverage.transform(lambda x: x/x.sum()*100)
df1 = df1.groupby(['Patient']).apply(lambda x: x.sort_values(by='Total_marker_coverage', ascending=False))
df1.to_csv('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/EukDetect/Saccharomyces cerevisiae S288C.csv', index=False)
