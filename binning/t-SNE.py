import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
import seaborn as sns
from sklearn.manifold import TSNE
from skbio.stats.composition import clr
#not quite the same results as PCA
data = pd.read_excel(sys.argv[1],  header=None, names=['kmer','freq','taxon'])
data = data.pivot(index='taxon', columns='kmer', values='freq')
data = data.drop(columns='kmer') # probably has to do with the file
data = data.reset_index()
data = data.drop(index=26) # probably has to do with the file

data['taxon'] = data['taxon'].replace(regex=r'^Candida\d+$', value='Candida dubliniensis')
data['taxon'] = data['taxon'].replace(regex=r'^Saccharomyces\d+$', value='Saccharomyces cerevisiae')
data['taxon'] = data['taxon'].replace(regex=r'^Malassezia\d+$', value='Malassezia restricta')

samples = data['taxon'] #for labeling later
X = data.drop(columns='taxon', axis=1)
X = X.to_numpy(dtype=np.float64)
X = clr(X)
model = TSNE(n_components=2, verbose=1, random_state=123)
results = model.fit_transform(X)
df = pd.DataFrame()
df['samples'] = samples
df['comp1'] = results[:,0]
df['comp2'] = results[:,1]
sns.scatterplot(x='comp1', y='comp2', hue=df.samples.tolist(), data=df).set(title='t-SNE kmer scatter plot')
plt.show()
