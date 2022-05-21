import sys
import pandas as pd
sheet_dict = pd.read_excel(sys.argv[1], sheet_name=None)
sumlist = []
lengthsum = []
readsum = []
for key, value in sheet_dict.items():
    sumlist.append(value['contig'].count())
    lengthsum.append(value['contig_length'].sum())
    readsum.append(value['number_of_mapping_reads'].sum())

data = pd.DataFrame({'contigsum':sumlist,'lengthsum':lengthsum,'readsum':readsum})
data.to_excel(sys.argv[-1], index=False)
