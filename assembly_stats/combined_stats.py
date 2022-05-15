import sys
import pandas as pd
contig_sums = []
patients = []
N50list = []
kraken_classified_contigs = []
total_assemblylength =[]
readsum = []

sheet_dict = pd.read_excel(sys.argv[1], sheet_name=None)
for key, value in sheet_dict.items():
    contig_sum = value['contig_length'].sum()
    contig_sums.append(contig_sum)
    patients.append(key)

sheet_dict2 = pd.read_excel(sys.argv[2], sheet_name=None)
for k, v in sheet_dict2.items():
    N50 = v.at[23,'number']
    N50list.append(N50)
    kraken_classified = v.at[30, 'number']
    kraken_classified_contigs.append(kraken_classified)
    total_assembly_length = v.at[22,'number']
    total_assemblylength.append(total_assembly_length)
    paired_reads = v.at[15, 'number']
    readsum.append(paired_reads)



data = pd.DataFrame({'patients': patients, 'contigs_sums': contig_sums, 'reads_sum': readsum,'N50': N50list,'total_assembly_length':total_assemblylength,'kraken_classified_contigs':kraken_classified_contigs})
data.to_excel(sys.argv[3], index=False)
