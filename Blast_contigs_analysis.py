import pandas as pd
import sys
# for loop starts from the second element of the list which is the first input file & stops at the last element of the list which is the output file
for i in sys.argv[1:-1]:
    data = pd.read_csv(i, sep='\t')
    data = data[data['Contig'].notna()]
    data['HitName'] = data.HitName.str.split('|').str[9]  # splits the string where we have | and keep only the species name
    x = data.iloc[1,0].split('_') # from the second row and fisrt column split the string where _ is located & store substring in a list
    sheetname = x[0] # choose the first element of the list which in our case is the patient_ID to be used as sheetname later
    with pd.ExcelWriter(sys.argv[-1], mode='a', engine='openpyxl') as writer: #append an existing excel file which matches the output we gave in the command line 
        data.to_excel(writer, sheet_name=sheetname, index=False)

