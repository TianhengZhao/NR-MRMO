import cos_sim as cs
f = open("./data/nodes_example.txt", "r")
name_dic = {}
for line in f.readlines():
    name, id, type = line.strip().split('\t')
    name_dic[id] = name



def calSimVecs(inFile, outFile1, outFile2):
    fr = open(inFile, 'r')
    srna_rel = open("../../mycode/srna-srna对应关系.txt", "r")
    gene_rel = open("../../mycode/基因-基因对应关系.txt", "r")
    fw1 = open(outFile1, 'w')
    fw2 = open(outFile2, 'w')
    fw1.truncate()
    fw2.truncate()
    dic = {}
    # 嵌入的结点
    for line in fr:
        arr = line.strip().split(' ')
        arr1 = [float(i) for i in arr]
        dic[int(arr1[0])] = arr1[1:]
    # string中已知有关联的srna
    for line in srna_rel:
        [srna1, srna2] = line.strip().split('\t')
        #if srna1 not in dic or srna2 not in dic: continue
        v1 = dic[int(srna1)]
        v2 = dic[int(srna2)]
        sim = cs.cos(v1, v2)
        fw2.write(name_dic[str(srna1)] + '\t' + name_dic[str(srna2)] + '\t' + str(round(float(sim), 4)) + '\n')
    for line in gene_rel:
        [gene1, gene2] = line.strip().split('\t')
        #if gene1 not in dic or gene2 not in dic:continue
        v1 = dic[int(gene1)]
        v2 = dic[int(gene2)]
        sim = cs.cos(v1, v2)
        fw1.write(name_dic[str(gene1)] + '\t' + name_dic[str(gene2)] + '\t' + str(round(float(sim), 4)) + '\n')
    fr.close()
    fw1.flush()
    fw1.close()
    fw2.flush()
    fw2.close()
    srna_rel.close()
    gene_rel.close()


pre = '../data/000/'
calSimVecs(pre + 'emb.txt', pre + 'gene.txt', pre + 'srna.txt')


