def unique_list(oldlist):
    newlist = []    #新列表
    for item in oldlist:    #遍历旧列表查找找相同元素
        if item not in newlist:    #如果item在newlist中表示该元素是重复元素，如果不在则将该元素添加到新列表里
            newlist.append(item)    #将该元素添加到新列表里
    return newlist

if __name__ == '__main__':
    oldlist = [1,1,3,4,-2,5,6,0,-2,-1,6]
    newlist = unique_list(oldlist)
    print(newlist)