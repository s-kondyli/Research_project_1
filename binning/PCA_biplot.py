import pandas as pd
import sys
from pca import pca
from sklearn.preprocessing import StandardScaler
from skbio.stats.composition import clr, multiplicative_replacement

data = pd.read_excel(sys.argv[1],  header=None, names=['kmer','freq','taxon'])
data = data.pivot(index='taxon', columns='kmer', values='freq')
data = data.drop(columns='kmer') # probably has to do with the file
features = data.columns.tolist()
data = data.reset_index()
data = data.drop(index=26) # probably has to do with the file

data['taxon'] = data['taxon'].replace(regex=r'^Candida\d+$', value='Candida_dubliniensis')
data['taxon'] = data['taxon'].replace(regex=r'^Saccharomyces\d+$', value='Saccharomyces_cerevisiae')
data['taxon'] = data['taxon'].replace(regex=r'^Malassezia\d+$', value='Malassezia_restricta')

samples = data['taxon']
# Scaling & modeling
X = data.drop(columns='taxon')
scaler = StandardScaler(with_mean=True, with_std=True)
X = scaler.fit_transform(X)
model = pca(normalize=True)
results = model.fit_transform(X, row_labels=samples, col_labels=features)
model.biplot(n_feat=3, label=False, legend=True, cmap='Set3')
