import pandas as pd
import sys
from pca import pca
import numpy as np
from sklearn.preprocessing import StandardScaler
from skbio.stats.composition import clr, multiplicative_replacement
#input is a excel file with muliple sheets (1 sheet & PCA per patient ID) 
sheet_dict = pd.read_excel(sys.argv[1], sheet_name=None)

for key, value in sheet_dict.items():
    samples = value['day'] #for the legend in the biplot
    value = value.drop(columns='day') #otherwise the column name 'day' is considered as feature (we don't want that)
    features = value.columns.tolist() #for plotting the features that explain the variance in the biplot
    X = value.to_numpy(dtype=np.float64) # very important for standarization of data
    X = multiplicative_replacement(X) #replaces 0 with small non-zero values, necessary for clr if we have 0 in our data
    X = clr(X) #because we have compositional data carrying relative (not absolute) information (proportion of reads sumed to a total)
    scaler = StandardScaler(with_mean=True, with_std=True)
    X = scaler.fit_transform(X)
    model = pca(normalize=True)
    results = model.fit_transform(X, row_labels=samples, col_labels=features) #results are a dictionary 
    print(type(results))
    model.biplot(n_feat=3, label=False, legend=True, cmap='tab10',figsize=(10,5), hotellingt2=True, title='PCA on bacterial taxa, patient'+ ' '+ key+'\n (points represent days related to HCT)')
