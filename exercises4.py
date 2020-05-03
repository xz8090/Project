import random

def reverse_complementarity_DNA():
    DNA_Length = random.randint(10,20)    #DNA序列长度在10到20之间
    ATCG = ['A','T','C','G']    #碱基
    DNASeq = ''    #DNA序列
    rcDNASeq = ''    #DNA反向互补序列
    for i in range(DNA_Length):
        random.seed(i)
        chosen = random.choice(ATCG)    #任意选择一个碱基
        if chosen == 'A':
            rcDNASeq = 'T' + rcDNASeq    #A替换T,并且往前添加新序列
        elif chosen == 'T':
            rcDNASeq = 'A' + rcDNASeq    #T替换A
        elif chosen == 'G':
            rcDNASeq = 'C' + rcDNASeq    #G替换C
        else:
            rcDNASeq = 'G' + rcDNASeq    #C替换G
        DNASeq += chosen
    
    print('DNA序列：\n%s \n反向互补序列：\n%s'%(DNASeq,rcDNASeq))           

if __name__ == '__main__':
    reverse_complementarity_DNA()