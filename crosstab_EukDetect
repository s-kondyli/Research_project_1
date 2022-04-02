import pandas as pd

data = pd.read_excel('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/Python/Results_python.xlsx', sheet_name='IMP3first_step')
data = data[['Sample_ID', 'Results_EukDetect']]
data = data[data['Sample_ID'].notna()] # drops NaN values from the column
data['Sample_ID'] = data['Sample_ID'].str.strip()
data['Results_EukDetect'] = data['Results_EukDetect'].str.strip() # cleaning up data by removing spaces from beginning and ending of string
data['patients'] = data.Sample_ID.str.extract('(\d+)') # extracts only the numbers out of each row of the x column (series object)
df = pd.crosstab(index=data.Results_EukDetect, columns=data.patients, margins=True, normalize=False)
df.to_csv('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/EukDetect/crosstab_EukDetect.csv')
data = pd.crosstab(index=data.Results_EukDetect, columns=data.patients, margins=True, normalize=True)
data.to_csv('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/EukDetect/crosstab_normalized_EukDetect.csv')
