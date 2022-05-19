import sys

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_excel(sys.argv[1], header=None, names=['kmer', 'freq'])


plt.hist(data['freq'])
# Plot and show the median read_count value



plt.title('Distribution of read counts')
plt.ylabel('Number of samples')
plt.xlabel('Read counts')
plt.tight_layout()
plt.show()
