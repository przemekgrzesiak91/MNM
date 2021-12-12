new_vcf = []

with open('chr12.vcf') as vcf:
    for line in vcf:
        if line[0:1] != '#':
            value = int(line.split('\t')[1])
            if value >= 112204691 and value <= 112247789:
                new_vcf.append(line)

f = open('task3_chr12.vcf', "w")
f.writelines(["%s" % item for item in new_vcf])
f.close()

