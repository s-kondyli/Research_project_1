import pandas as pd
import sys
df = pd.read_csv(sys.argv[1], sep='\t', header=None, names=['contigs']) # filter file
df = df[df['contigs'].notna()]
for i in sys.argv[2:-1]: # last one excluded from command line args
    data = pd.read_csv(i, sep='\t', header=None, names=['contig','contig_depth'])
    data = data.loc[data['contig'].isin(df['contigs'])]
    data_stats = data.describe()
    x = data.iloc[1,0].split('_')
    sheetname = x[0]
    with pd.ExcelWriter(sys.argv[-1], mode='a',engine='openpyxl') as writer:  # append an existing excel file which matches the output we gave in the command line
        data_stats.to_excel(writer, sheet_name=sheetname, index=True)
