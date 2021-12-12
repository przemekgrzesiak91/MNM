import matplotlib.pyplot as plt
import pandas as pd

chromosomes = list(range(1,22))
chr_mean_DP = {}

for chr in chromosomes:
    chr_DP = []
    name = 'chr' + str(chr) + '.vcf'
    with open(name) as vcf:
        for line in vcf:
            if line[0:1] != '#':
                info = line.split('\t')[7].split(';')
                for x in info:
                    if x[0:2] == 'DP':
                        chr_DP.append(int(x.split('=')[1]))
    chr_mean_DP[chr] = sum(chr_DP) / len(chr_DP)

df = pd.DataFrame.from_dict(chr_mean_DP,orient='index',columns=['avg_DP'])
df.to_csv('DP_table.csv')
df.plot(kind='bar')
plt.savefig('Plots\\Avg_DP_plot')


