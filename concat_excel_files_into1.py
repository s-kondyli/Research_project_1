import pandas as pd
import sys
# input files sys.argv[1:-1]
# output file the last sys.argv
# conctatenates excel files with single sheets into 1 excel workbook (1sheet)
data = pd.read_csv(sys.argv[1], sep='\t', header=None, names=['kmer'])
data[['kmer', 'freq']] = data['kmer'].str.split(' ',1,expand=True)  #split the column where you have space & save the second element of the list in another column called 'freq'
data.to_excel('Saccharomyces_cerevisiae .xlsx', index=False)

