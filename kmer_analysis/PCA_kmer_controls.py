import pandas as pd
import numpy as np
import sys
from pca import pca
from sklearn.preprocessing import StandardScaler
from skbio.stats.composition import clr, multiplicative_replacement
## takes as input the output.txt file from kmer-counter & performs PCA analysis

## Reshaping the data in the correct form for PCA: samples(contigIDs) as rows & features (kmers) as columns
numpy_df = pd.read_csv(sys.argv[1], delimiter="\t", header=None).to_numpy()
index, keys_values = pd.Index(numpy_df[:, 0]), numpy_df[:, 1]
all_keys = list()
for row in keys_values:
    all_keys.extend([key_val.split(":")[0] for key_val in row.split()])
all_keys = list(set(all_keys))

keys_values = [{key_val.split(":")[0]: key_val.split(":")[1] for key_val in row.split()} for row in keys_values]
data = np.zeros((len(index), len(all_keys)))
index_of = {k: i for i, k in enumerate(all_keys)}
for i in range(len(index)):
    for k, v in keys_values[i].items():
        data[i][index_of[k]] = v

df_data = pd.DataFrame(data=data, index=index, columns=all_keys)
## Fixing the samples names & feature names for PCA visualization 
df_data = df_data.reset_index()
df_data = df_data.rename(columns={'index':'samples'})

# rename the samples for visualization purposes (clustering is obvious with one color per taxon)
df_data['samples'] = df_data['samples'].replace(regex=r'.*Candida dubliniensis.*', value='Candida dubliniensis')
df_data['samples'] = df_data['samples'].replace(regex=r'.*Candida albicans.*', value='Candida albicans')
df_data['samples'] = df_data['samples'].replace(regex=r'.*Candida parapsilosis.*', value='Candida parapsilosis')
df_data['samples'] = df_data['samples'].replace(regex=r'.*Saccharomyces.*', value='Saccharomyces cerevisiae')
df_data['samples'] = df_data['samples'].replace(regex=r'.*Malassezia.*', value='Malassezia restricta')
df_data['samples'] = df_data['samples'].replace(regex=r'.*1042.*', value='1042')
df_data['samples'] = df_data['samples'].replace(regex=r'.*1044.*', value='1044')
df_data['samples'] = df_data['samples'].replace(regex=r'.*1179.*', value='1179')
df_data['samples'] = df_data['samples'].replace(regex=r'.*653.*', value='653')
df_data['samples'] = df_data['samples'].replace(regex=r'.*1105.*', value='1105')
df_data['samples'] = df_data['samples'].replace(regex=r'.*1193.*', value='1193')
df_data['samples'] = df_data['samples'].replace(regex=r'.*1203.*', value='1203')
df_data['samples'] = df_data['samples'].replace(regex=r'.*1252.*', value='1252')
df_data['samples'] = df_data['samples'].replace(regex=r'.*1414.*', value='1414')
df_data['samples'] = df_data['samples'].replace(regex=r'.*2065.*', value='2065')
df_data['samples'] = df_data['samples'].replace(regex=r'.*2142.*', value='2142')

samples = df_data['samples'].tolist() # for labels in biplot
print(df_data.shape) # to see the number of contigs & features you have eventually 
# Standarizing and scaling for PCA
df_data = df_data.drop(columns='samples')
features = df_data.columns.tolist() #for the pca biplot (show the loadings with arrows)

X = df_data.to_numpy(dtype=np.float64) # very important for the clr & PCA 
X = multiplicative_replacement(X) #replaces zero with small non-zero values (pseudo count)
X = clr(X)
scaler = StandardScaler(with_mean=True, with_std=True) #not sure if necessary if you have compositional data & you already did clr transformation
X = scaler.fit_transform(X)
model = pca(normalize=True)
results = model.fit_transform(X, row_labels=samples, col_labels=features)
model.biplot(n_feat=3, label=False, legend=True, cmap='tab10', hotellingt2=True)

