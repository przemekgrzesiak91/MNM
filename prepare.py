headers = []
chr_data = []
i = '1'
with open('data\data.vcf', mode='r') as vcf:

    for line in vcf:
        if line[0:1].isdigit() or line[0:1] in ['X','Y']:
            if line[0:2].strip() == i:
                chr_data.append(line)
            else:
                print(i)
                name = 'chr' + i + '.vcf'

                f = open(name, "w")
                f.writelines(["%s\n" % item for item in headers])
                f.writelines(["%s\n" % item for item in chr_data])
                f.close()

                i = line[0:2].strip()
                chr_data = []
        else:
            headers.append(line)