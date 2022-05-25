import os
import re
# renaming files that match to regex in the working directory
path = os.getcwd()
dir_list = os.listdir(path) # lists of all files in the path (in this case cwd)
var ='.fasta' # what we want to rename the files
p = re.compile('.*\d+$') # regex to filter only the files we want
fasta_list =[file for file in dir_list if p.match(file)] # create filtered list
for f in dir_list:
    if f in fasta_list:
        os.rename(f, f+var)
