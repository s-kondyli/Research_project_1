import sys
import pandas as pd

sheet_dict = pd.read_excel(sys.argv[1], sheet_name=None)
patient = []
number_of_contigs = []
contig_len = []
for key, value in sheet_dict.items():
    patient.append(key)
    contigs = value.at[21,'number']
    contig_length = value.at[22,'number']
    number_of_contigs.append(contigs)
    contig_len.append(contig_length)


data = pd.DataFrame({'patients':patient,'contig_sum':number_of_contigs, 'contig_length':contig_len})
data.to_excel(sys.argv[-1], index=False)
