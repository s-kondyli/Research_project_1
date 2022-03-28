import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
import re
data = pd.read_excel('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/Python/Results_Python2.xlsx', sheet_name='Table_with_patients')
data = data[data['Name'].notna()]
#Sort by taxon
unique_taxa = data.Name.unique().tolist()
df = data[['Name', 'Read_counts']]
df_total_marker = data[['Name', 'Total_marker_coverage']]
df_total_marker['Total_marker_coverage%'] = df_total_marker.Total_marker_coverage.transform(lambda y: y*100)
df_total_marker = df_total_marker[['Name', 'Total_marker_coverage%']]
df_total_marker = df_total_marker.groupby(['Name']).describe().unstack(1).reset_index().pivot(index='Name', columns='level_1', values=0).reset_index()
df = df.groupby(['Name']).describe().unstack(1).reset_index().pivot(index='Name', columns='level_1', values=0).reset_index()
df1 = data.loc[data['Name'].str.contains('Saccharomyces cerevisiae S288C')]
df2 = data.loc[data['Name'].str.contains('Malassezia restricta')]
df3 = data.loc[data['Name'].str.contains('Candida dubliniensis CD36')]
df4 = data.loc[data['Name'].str.contains('Candida albicans SC5314')]
df5 = data.loc[data['Name'].str.contains('Agaricus bisporus var. bisporus H97')]
df6 = data.loc[data['Name'].str.contains('Aspergillus')]
df7 = data.loc[data['Name'].str.contains('Hanseniaspora guilliermondii')]
df8 = data.loc[data['Name'].str.contains('Malassezia sympodialis ATCC 42132')]
df9 = data.loc[data['Name'].str.contains('Cyberlindnera jadinii NRRL Y-1542')]
df1['%'] = df1.Read_counts.transform(lambda x: x/x.sum()*100)
df1 = df1.sort_values(by=['%'], ascending=False)
print(unique_taxa)
df2['%'] = df2.Read_counts.transform(lambda x: x/x.sum()*100)
df2 = df2.sort_values(by=['%'], ascending=False)
df3['%'] = df3.Read_counts.transform(lambda x: x/x.sum()*100)
df3 = df3.sort_values(by=['%'], ascending=False)
df4['%'] = df4.Read_counts.transform(lambda x: x/x.sum()*100)
df4 = df4.sort_values(by=['%'], ascending=False)
df5['%'] = df5.Read_counts.transform(lambda x: x/x.sum()*100)
df5 = df5.sort_values(by=['%'], ascending=False)
df6['%'] = df6.Read_counts.transform(lambda x: x/x.sum()*100)
df6 = df6.sort_values(by=['%'], ascending=False)
df7['%'] = df7.Read_counts.transform(lambda x: x/x.sum()*100)
df7 = df7.sort_values(by=['%'], ascending=False)
df8['%'] = df8.Read_counts.transform(lambda x: x/x.sum()*100)
df8 = df8.sort_values(by=['%'], ascending=False)
df9['%'] = df9.Read_counts.transform(lambda x: x/x.sum()*100)
df9 = df9.sort_values(by=['%'], ascending=False)
plt.bar(df9.Patient_ID, df9['%'])
#plt.title('Saccharomyces cerevisiae % of read counts in patients')
plt.title('Candida dubliniensis % of read counts  in patients')
plt.ylabel('% of read counts')
#plt.show()
df = df[['Name', 'count', 'max', 'min', 'mean', 'std']]
df_total_marker.to_csv('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/EukDetect/stats_total_marker_coverage.csv', index=False)
df.to_csv('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/EukDetect/stats_read_counts.csv', index=False)
df1.to_csv('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/EukDetect/Saccharomyces.csv', index=False)
df2.to_csv('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/EukDetect/Malassezia_restricta.csv', index=False)
df3.to_csv('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/EukDetect/Candida_dubliniensis_CD36.csv', index=False)
df4.to_csv('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/EukDetect/Candida_albicans_SC5314.csv', index=False)
df5.to_csv('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/EukDetect/Agaricus_bisporus_var_bisporus_H97.csv', index=False)
df6.to_csv('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/EukDetect/Aspergillus.csv', index=False)
df7.to_csv('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/EukDetect/Hanseniaspora_guilliermondii.csv', index=False)
df8.to_csv('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/EukDetect/Malassezia_sympodialis_ATCC_42132.csv', index=False)
df9.to_csv('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/EukDetect/Cyberlindnera_jadinii_NRRL_Y_1542.csv', index=False)
#df10.to_csv('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/EukDetect/Debaryomyces_hansenii_CBS767.csv', index=False)
