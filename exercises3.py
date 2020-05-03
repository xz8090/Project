import random

def count_GC():
    DNA_Length = random.randint(100,500)    #DNA序列长度在100到500之间
    ATCG = ['A','T','C','G']    #碱基
    DNASeq = ''    #DNA序列
    countCG = 0    #碱基CG数量
    for i in range(DNA_Length):
        random.seed(i)
        chosen = random.choice(ATCG)    #任意选择一个碱基
        if chosen == 'C' or chosen == 'G':
            countCG += 1 
        DNASeq += chosen
    
    print('DNA序列：\n%s \nGC含量：%s%%'%(DNASeq,countCG*100/DNA_Length))
            

if __name__ == '__main__':
    count_GC()