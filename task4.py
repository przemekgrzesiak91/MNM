import matplotlib.pyplot as plt

chromosomes = list(range(1,22))
chromosomes.append('X')

for chr in chromosomes:
    name = 'chr' + str(chr) + '.vcf'
    chr_ins_tab = []
    chr_del_tab = []
    with open(name) as vcf:
        for line in vcf:
            if line[0:1] != '#':
                ref = len(line.split('\t')[3])
                alt = len(line.split('\t')[4])
                diff = alt - ref

                if diff > 0:
                    chr_ins_tab.append(diff)
                elif diff <0:
                    diff = abs(diff)
                    chr_del_tab.append(diff)
    #Insertions
    plt.hist(chr_ins_tab,bins=100)
    plt.title('Chr ' + str(chr) + ' insertions lengths')
    name = 'Plots\\'+'chr'+str(chr)+'ins'
    plt.savefig(name)
    #Deletions
    plt.hist(chr_del_tab,bins=100)
    plt.title('Chr ' + str(chr) + ' deletions lengths')
    name = 'Plots\\'+'chr'+str(chr)+'del'
    plt.savefig(name)

