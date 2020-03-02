
#快排算法
'''
快排利用递归思想，进行排序时间复杂度n*log2n
def kuaipai(num):
    if ...:
    piv = num[0]
    for i in range(len(num)):
        if...:
        elif..:
        else:
        more = kuaipai(da)
        less = kuaiipai(xiao)
        return more+piv+less

'''
def kuaipai(num):
    da,zhong,xiao = [],[],[]
    if len(num<)<1:
        return num
    pivo = num[0]
    for i in range(len(num)):
        if i > num[0]:
            da.append(i)
        elif i < num[0]:
            xiao.append(i)
        else:
            zhong.append(i)
        less = kuaiPai(xiao)
        more = kuaiPai(da)
        return less+zhong+more

