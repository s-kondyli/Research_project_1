import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

#import file: kraken/Eukrep contig_breadth.xlsx
sheet_dict = pd.read_excel(sys.argv[1],sheet_name=None)
readsum = []
contig_sum = []
for key, value in sheet_dict.items():
    reads = value['number_of_mapping_reads'].sum()
    contig = value['contig'].nunique()
    contig_sum.append(contig)
    readsum.append(reads)

data = pd.DataFrame({'reads':readsum, 'contigs':contig_sum})
# Linear regression
x_data = data.reads.to_numpy().reshape(-1,1)
y_data = data.contigs.to_numpy()
x_data = np.log10(x_data)
y_data = np.log10(y_data)
X = linear_model.LinearRegression()
# Train the model using the data
X.fit(x_data, y_data)
# Make predicitons (I didn't have a testing set)
y_pred = X.predict(x_data)
# The coefficients
print("Coefficients: \n", X.coef_)
# The mean squared error
print('Mean squared error: %2.2f' % mean_squared_error(y_data, y_pred))
# The coefficient of determination: 1 is perfect prediction
print("Coefficient of determination: %.2f" % r2_score(y_data, y_pred))

# Scatter plot
plt.scatter(x_data, y_data, color="black")
plt.plot(x_data, y_pred, color="mediumslateblue", linewidth=1)
plt.title('EukRep assembly scatter plot \n (log10 scale)')
plt.xlabel('Number of reads')
plt.ylabel('Sum contigs')
plt.tight_layout()
plt.show()
#plt.savefig('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/Python/Plots/Linear_regression_sum',dpi=1200)
