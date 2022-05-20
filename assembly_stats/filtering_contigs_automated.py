import pandas as pd
import sys
#filter a dataframe based on a list of another file
df = pd.read_csv(sys.argv[1], sep='\t', header=None, names=['contigs'])
df = df[df['contigs'].notna()]
sheet_dict = pd.read_excel(sys.argv[2], sheet_name=None)
for key, value in sheet_dict.items():
    x = value.iloc[1, 0].split('_')
    sheetname = x[0]
    value = value.loc[value['contig'].isin(df['contigs'])]
    with pd.ExcelWriter(sys.argv[-1], mode='a', engine='openpyxl') as writer:  
        value.to_excel(writer, sheet_name=sheetname, index=False)  
