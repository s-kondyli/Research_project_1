import pandas as pd
data = pd.read_csv("C:/Users/lilak/Documents/Master BMS-O/Research Project 1/Results from assembly step/mg.kraken.parsed_1203O.tsv", sep='\t')

data = data[data['K'].notna()]
data = data[data['D'].notna()]
df = data.loc[data['D'].str.contains('Eukaryota')]
df = data.loc[data['K'].str.contains('Fungi')]
df = df.loc[df['O'].notna()]
df = df[['O', 'length']]

df = df.groupby('O').describe().unstack(1).reset_index().pivot(index='O', columns='level_1', values=0).reset_index()

df.to_csv('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/Results from assembly step/assembly_stats_o1203O.csv', index=False)
