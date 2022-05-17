import sys
import pandas as pd
sheet_dict = pd.read_excel(sys.argv[1], sheet_name=None, names=['name','id','reads','day'])
topbacteria = pd.read_excel(sys.argv[2], names=['taxa'])
topbacteria['taxa'] = topbacteria['taxa'].str.strip().drop_duplicates()
for key, value in sheet_dict.items():
    value['patient'] = value['id'].str.extract('(\d+)')
    patient = value.at[0,'patient']
    value = value.loc[(value['day'] <= 40) & (value['day'] >= 0)]
    value = value[value['name'].isin(topbacteria['taxa'])]
    value = value.pivot(index='name', columns='day', values='reads')
    value = value.fillna(0)
    with pd.ExcelWriter(sys.argv[-1], mode='a', engine='openpyxl') as writer:  # append an existing excel file which matches the output we gave in the command line
        value.to_excel(writer, sheet_name=patient)

