import pandas as pd
import sys
from pca import pca
import numpy as np 
from sklearn.preprocessing import StandardScaler
from skbio.stats.composition import clr, multiplicative_replacement

data = pd.read_excel(sys.argv[1],  header=None, names=['kmer','freq','taxon']) #input file was the control kmer profiling (4mers)
data = data.pivot(index='taxon', columns='kmer', values='freq')
data = data.drop(columns='kmer') # probably has to do with the file (may need to remove in other files)
features = data.columns.tolist() #features we want to reduce dimensionality
data = data.reset_index() # because from the pivot function we had set index as taxon 
data = data.drop(index=26) # probably has to do with the file (may need to remove in other files)

# replaces sample names as you know you have 3 clusters (visualization purposes)
data['taxon'] = data['taxon'].replace(regex=r'^Candida\d+$', value='Candida_dubliniensis')
data['taxon'] = data['taxon'].replace(regex=r'^Saccharomyces\d+$', value='Saccharomyces_cerevisiae')
data['taxon'] = data['taxon'].replace(regex=r'^Malassezia\d+$', value='Malassezia_restricta')

samples = data['taxon'] #for coloring the dots & the legend 
# Scaling data 
X = data.drop(columns='taxon')
X = X.to_numpy(dtype=np.float64) # very important for proper data type for clr transformation(and not only)
X = clr(X)
scaler = StandardScaler(with_mean=True, with_std=True) #not sure if necessary if you have compositional data & you already did clr transformation
X = scaler.fit_transform(X)
model = pca(normalize=True)
results = model.fit_transform(X, row_labels=samples, col_labels=features)
model.biplot(n_feat=3, label=False, legend=True, cmap='Set3') #label false so you only see the legend and not the label of each point on the graph 
