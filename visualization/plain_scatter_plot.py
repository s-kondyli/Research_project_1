import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/Python/Results_python.xlsx', sheet_name='Table_with_patients')
data = data[data['Name'].notna()]
data['percent_marker'] = data['Total_marker_coverage'].transform(lambda x: x*100)
plt.scatter(data.percent_marker, data.Observed_markers, c='g', s=15)
plt.xlabel('Percentage of total marker coverage')
plt.ylabel('Number of observed markers')
plt.tight_layout()
#plt.show()
plt.savefig('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/Python/Plots/scatter_plot_total_marker_coverage.png', dpi=1200)
