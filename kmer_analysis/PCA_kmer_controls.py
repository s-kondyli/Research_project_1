import pandas as pd
import numpy as np
import sys
from pca import pca
from sklearn.preprocessing import StandardScaler
from skbio.stats.composition import clr, multiplicative_replacement
# takes as input the output txt file of kmer-counter and performs PCA analysis

input = pd.read_csv(sys.argv[1], sep='\t', header=None, names=['contig','kmers'])

# reshaping data from txt file to be correct for the PCA (samples as rows (contigs),features (kmers) as columns & kmerfreqs are the values
samples = input['contig'].tolist() # for PCA later
input = input['kmers'].str.split(' ', expand=True)

data = pd.DataFrame() # create an empty dataframe
# iterate over the dataframe's columns
for label, content in input.items():
    df = content.str.split(':', expand=True)
    kmer_name = df.loc[0].iat[0]
    s = pd.Series(name=kmer_name, data=df.iloc[:,1])
    data = data.append(s)

data = data.T
data['samples'] = samples
# rename the samples for visualization purposes (clustering is obvious with one color per taxon)
data['samples'] = data['samples'].replace(regex=r'.*Candida.*', value='Candida dubliniensis')
data['samples'] = data['samples'].replace(regex=r'.*Saccharomyces.*', value='Saccharomyces cerevisiae')
data['samples'] = data['samples'].replace(regex=r'.*Malassezia.*', value='Malassezia restricta')
samples = data['samples'].tolist() #yes I did it before but now I have the filtered sample names and it overrides the previous list
data = data.drop(columns='samples')
features = data.columns.tolist() #for the pca biplot
X = data.to_numpy(dtype=np.float64) #
X = clr(X)
scaler = StandardScaler(with_mean=True, with_std=True) #not sure if necessary if you have compositional data & you already did clr transformation
X = scaler.fit_transform(X)
model = pca(normalize=True)
results = model.fit_transform(X, row_labels=samples, col_labels=features)
model.biplot(n_feat=3, label=False, legend=True, cmap='tab10')
