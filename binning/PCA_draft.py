import pandas as pd
import matplotlib.pyplot as plt
from pca import pca
from skbio.stats.composition import clr, multiplicative_replacement
import sys
data = pd.read_excel(sys.argv[1], header=None, names=['kmer','freq','taxon'])

data = data.pivot(index='taxon', columns='kmer', values='freq')

data.to_csv('temp.csv')
data = pd.read_csv('temp.csv')

X = data.drop('taxon', axis=1)
#Replace all zeros with small non-zero values
X = multiplicative_replacement(X)
# Performs centre log ratio transformation
X = clr(X)
labels = data['taxon']
model = pca(n_components=2, normalize=True)
results = model.fit_transform(X)
model.biplot(n_feat=4, y=labels, legend=False)
plt.show()
