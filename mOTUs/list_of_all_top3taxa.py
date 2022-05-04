import sys
import pandas as pd

# Create a dictionary from the workbook with keys as the sheet_name and values each dataframe
sheets_dict = pd.read_excel(sys.argv[1], sheet_name=None)

all_sheets = [] # empty list
# For loop to create a  list whose elements are the dataframes
for key, value in sheets_dict.items():
    all_sheets.append(value)
    
# Concatenate all sheets into one dataframe (we created the all_sheets list because pd.concat takes a sequence of dataframes)
data = pd.concat(all_sheets, ignore_index=True)
data.iloc[:,0] = data.iloc[:,0].str.strip()
all_taxa = data.iloc[:,0]
all_taxa.to_frame()
all_taxa = all_taxa.drop_duplicates()
# Store your data in the output file 
all_taxa.to_csv(sys.argv[2],index=False)
