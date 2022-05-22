import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn import preprocessing
import sys
# Import our data
data = pd.read_excel(sys.argv[1],  header=None, names=['kmer','freq','taxon'])
 # drops NaN values from Name column
data = data.pivot(index='taxon', columns='kmer', values='freq')
data = data.fillna(0)
index = data.index.tolist() # creates a list of all indeces to be passed later when creating the pca_df
# Scale & center the data
scaled_data = preprocessing.scale(data) # expects samples to be rows which in our case is true because in data index=Day_related_to_HCT. Otherwise we would need to transpose the data like this: data.T
pca = PCA()
pca.fit(scaled_data)
pca_data = pca.transform(scaled_data)
per_var = np.round(pca.explained_variance_ratio_ * 100, decimals=1)
labels = ['PC' + str(x) for x in range(1, len(per_var)+1)]

# PCA plot

pca_df = pd.DataFrame(pca_data, index=list(index) , columns=labels)
plt.scatter(pca_df.PC1, pca_df.PC2, cmap='Pastel1')
plt.xlabel('PC1 - {0}%'.format(per_var[0])) # represents the percentage weight for each PC
plt.ylabel('PC2 - {0}%'.format(per_var[1]))
plt.title('PCA scatter plot for Patient 1179')
for day in pca_df.index:
    plt.annotate(day, (pca_df.PC1.loc[day], pca_df.PC2.loc[day]))

# Show plot
plt.tight_layout()
plt.show()
