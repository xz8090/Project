def count_amino_acid(seq):
    amino_acid_dict = {}    #利用字典保存每个氨基酸的统计信息
    for amino_acid in seq:    #遍历每个氨基酸
        if amino_acid not in amino_acid_dict:    #该氨基酸不在统计字典中，则添加到字典中
            amino_acid_dict[amino_acid] = 1    #添加氨基酸名称作为key值，并且该key对应的value（氨基酸数量）初始为1
        else:
            amino_acid_dict[amino_acid] += 1    #氨基酸已经存在字典中则氨基酸数量在原基础上+1
    
    #打印所有氨基酸名称（key）和数量（value）
    for name in amino_acid_dict.keys():
        print('氨基酸：%s,数量：%s'%(name,amino_acid_dict[name]))

if __name__ == '__main__':
    seq = 'GIVEQCCTSICSLYQLENYCNFVNQHLCGSHLVEALYLVCGERGFFYTPKT'
    count_amino_acid(seq)