import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
sheet_dict = pd.read_excel(sys.argv[1], sheet_name=None)
for key, value in sheet_dict.items():
    value['patient'] = value['Patient_ID'].str.extract('(\d+)')
    patient = value.at[0,'patient']
    value = value.loc[(value['Day_related_to_HCT'] <=40)&(value['Day_related_to_HCT'] >=0)]
    value['Read_counts'] = value['Read_counts'].fillna(0)
    plt.plot(value['Day_related_to_HCT'], value['Read_counts'],linestyle='solid', color= 'lightgreen')
    mean = value['Read_counts'].mean()
    plt.axhline(mean, color='salmon', label='Mean')
    plt.legend()
    x = np.arange(-10,45,5) #Return evenly spaced values within a given interval args: start, stop, step
    y = np.arange(0,953,50)
    plt.xticks(x)
    plt.yticks(y)
    plt.title('Timeseries plot of patient \n'+ patient)
    plt.ylabel('Reads')
    plt.xlabel('Day related to HCT')
    plt.tight_layout()
    plt.show()
