import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
sheet_dict = pd.read_excel(sys.argv[1], sheet_name=None)
for key, value in sheet_dict.items():
    x = value.iloc[0, 0].split('_')
    patient = x[0]
    y = value['breadth_of_coverage'].sum().astype(int)
    value.loc[value['breadth_of_coverage']==1, '1'] = 1
    z = value['1'].sum().astype(int)
    print(z/y*100)
    plt.hist(value['breadth_of_coverage'],  log=False, edgecolor='black')
    plt.xticks(np.arange(0,1.1,0.1))  # caclulates a range for the xticks
    plt.title('Distribution of contig breadth of  coverage of  patient'+ ' ' + patient + '\n(Kraken)')
    plt.ylabel('Number of contigs')
    plt.xlabel('Breadth of coverage')
    plt.yscale('log')
    plt.tight_layout()
    plt.show()


