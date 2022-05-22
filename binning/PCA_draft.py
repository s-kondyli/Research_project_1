import pandas as pd
import sys
from pca import pca
from sklearn.preprocessing import StandardScaler
from skbio.stats.composition import clr, multiplicative_replacement
# Import our data
data = pd.read_excel(sys.argv[1],  header=None, names=['kmer','freq','taxon'])
data = data.pivot(index='taxon', columns='kmer', values='freq')
features = data.columns.tolist()
data = data.reset_index()
data['taxon'] = data['taxon'].replace(regex=r'^Candida_dubliniensis[0-9]$', value='Candida_dubliniensis')
data['taxon'] = data['taxon'].replace(regex=r'^Saccharomyces_cerevisiae[0-9]$', value='Saccharomyces_cerevisiae')
data['taxon'] = data['taxon'].replace(regex=r'^Malassezia_restricta[0-9]$', value='Malassezia_restricta')
samples = data['taxon']
X = data.drop('taxon', axis=1)
scaler = StandardScaler(with_mean=True, with_std=True)
X = scaler.fit_transform(X)
model = pca(normalize=True)
results = model.fit_transform(X, row_labels=samples, col_labels=features)
model.biplot(n_feat=3, label=False, legend=True)
