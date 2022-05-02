#!/usr/bin/env python
import sys
from Bio.Blast import NCBIXML
import csv
infile = sys.argv[1]
outfile = sys.argv[2]
topPerc = float(sys.argv[3])
blast = NCBIXML.parse(open(infile))
with open(sys.argv[2], 'w') as csvfile:
	blapawriter = csv.writer(csvfile, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	blapawriter.writerow(['Contig', 'ContigLength', 'HitName', 'Rank', 'Bitscore', 'QueryCov', 'PercIdent'])
	for record in blast:
		if record.alignments:
			topBit = record.alignments[0].hsps[0].bits
			j = 0
			k = len(record.alignments)
			while (topBit * topPerc / 100) < record.alignments[j].hsps[0].bits:
				blapawriter.writerow([record.query, record.query_letters, record.alignments[j].title, j + 1,record.alignments[j].hsps[0].bits, (record.alignments[j].hsps[0].align_length - record.alignments[j].hsps[0].gaps) * 100 / record.query_letters, record.alignments[j].hsps[0].identities * 100 / record.alignments[j].hsps[0].align_length])
				j += 1
				if j == k:
					break
