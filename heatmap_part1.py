import sys 
import pandas as pd
data = pd.read_csv('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/mOTUs/topbacteria_1179_patient.csv')
data = data[data['Name'].notna()]
data = data[['Name', 'Day_related_to_HCT', 'Read_counts']]
data = data.pivot(index='Name', columns='Day_related_to_HCT', values='Read_counts')
data = data.fillna(0)
data.to_csv('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/mOTUs/1179_ordered.csv')