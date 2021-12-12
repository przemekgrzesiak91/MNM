
chromosomes = list(range(1,22))
chromosomes.append('X')

count = 0

for chr in chromosomes:
    name = 'chr' + str(chr) + '.vcf'
    with open(name) as vcf:
        for line in vcf:
            if line[0:1] != '#':
                value= line.split('\t')[6]
                if value == "PASS":
                    info = line.split('\t')[7].split(';')
                    genotype = line.split('\t')[9][0:3]
                    if 'GoNLv5_AF' in info[-2] and float(info[-2].split('=')[1]) < 0.01 and genotype == '0/1':
                            count += 1

print(count)