import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_excel('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/Results from assembly step/contigs_reads.xlsx')
plt.scatter(data.reads, data.contigs)
plt.title('Assemblies scatter plot')
plt.ylabel('Number of contigs')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Number of reads')
plt.tight_layout()
plt.show()
plt.savefig('C:/Users/lilak/Documents/Master BMS-O/Research Project 1/Python/Plots/scatter_plot_assemblies.png', dpi=1200)
