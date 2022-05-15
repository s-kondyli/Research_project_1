import pandas as pd
import sys
for i in sys.argv[1:-1]:
    data = pd.read_csv(i, sep='\t', header=None, names=['contig','contig_depth'])
    data_stats = data.describe()
    x = data.iloc[1,0].split('_')
    sheetname = x[0]
    print(data_stats)
    with pd.ExcelWriter(sys.argv[-1], mode='a',engine='openpyxl') as writer:  # append an existing excel file which matches the output we gave in the command line
        data_stats.to_excel(writer, sheet_name=sheetname, index=True) # index true cause it takes the count max mean etc as index and we want it 
