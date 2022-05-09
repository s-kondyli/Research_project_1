import pandas as pd
import sys
# Import tsv files
data = pd.read_csv(sys.argv[1],sep='\t')

# Keeps from the column x all the values that are not NaN (basically drops NaN from specific column)
data = data[data['K'].notna()]
data = data[data['D'].notna()]

# Keeps the rows of a column x that contain a specific name
df = data.loc[data['D'].str.contains('Eukaryota')]
df = data.loc[data['K'].str.contains('Fungi')]

# Keeps from the column S all the values that are not NaN (we need it because some rows are empty/not classified)
df = df.loc[df['S'].notna()]
# Reorder and keep only the columns you are interested in
#df = df[['contig', 'length', 'S']]
df = df[['length', 'S']]
# Get statistics for each group
df = df.groupby('S').describe().unstack(1).reset_index().pivot(index='S', columns='level_1', values=0).reset_index()

# Save to a file
df.to_csv(sys.argv[2],index=False)
