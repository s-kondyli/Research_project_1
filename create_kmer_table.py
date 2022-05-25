import pandas as pd
import sys
import re
data = pd.read_csv(sys.argv[1], sep='\t', header=None, names=['contig','kmers'])
print(data)
#data = data['kmers'].str.split(' ', expand=True)

data2 = pd.DataFrame()
#for label, content in data.items():
    #df = content.str.split(':', expand=True)
    #kmer_name = df.loc[0].iat[0]
    #s = pd.Series(name=kmer_name, data=df.iloc[:,1])
    #data2 = data2.append(s)


