import sys
import pandas as pd
# command line args: fasta sequence , k-mer size , output excel file
fastafile = open(sys.argv[1]) # requires fasta file without headers
readTF = fastafile.read()
sequence = "".join(readTF.split())  

# Defines a function that takes as args the fasta sequence and the kmersize (eg 2-mer,4-mer etc)
# and returns a dictionary with keys the unique k-mers and values how many times they were found in the sequence 
def k_merFreq(sequence, kmersize):  
    kFreq = {}
    for i in range(0, len(sequence) - kmersize +1):
        kmer = sequence[i:i + kmersize]
        if kmer in kFreq:
            kFreq[kmer] += 1
        else:
            kFreq[kmer] = 1

    return kFreq

kmer_dict = k_merFreq(sequence, int(sys.argv[2]))
data = pd.DataFrame(data=kmer_dict, index=[0]).T
# Write the dictionary in an excel file 
with pd.ExcelWriter(sys.argv[-1], engine='openpyxl') as writer:
    data.to_excel(writer, index=True)
