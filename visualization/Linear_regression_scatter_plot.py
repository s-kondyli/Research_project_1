import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
data = pd.read_excel('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/Results from assembly step/contigs_reads.xlsx', sheet_name='contig_count')
x_data = data.reads.to_numpy().reshape(-1, 1)
y_data = data.contigs.to_numpy()
x_data = np.log(x_data)
y_data = np.log(y_data)
# Create linear regression model
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
plt.plot(x_data, y_pred, color="g", linewidth=2)
plt.title('Linear Regression scatter plot \n (log scale)')
plt.xlabel('Number of reads')
plt.ylabel('Sum of contigs')
plt.tight_layout()
plt.yticks(()) # don't show the ticks
plt.xticks(())
#plt.show()
plt.savefig('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/Python/Plots/Linear_regression_sum',dpi=1200)