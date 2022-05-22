import pandas as pd
import sys
df_list = []
for i in sys.argv[1:-1]:
    df_list.append(pd.read_excel(i))

data = pd.concat(df_list)
data.to_excel(sys.argv[-1], index=False)
