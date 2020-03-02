#coding=utf-8
def maoPao(num):
    for i in range(len(num)-1):
        for j in range(len(num)-1-i):
            if num[j]>num[j+1]:
                num[j],num[j+1] = num[j+1],num[j]
    return num
#print maoPao(num=[1,3,2,5,2,1])
if __name__=='__main__':
#    num = input('请输入输入无序数据：')
    shili = maoPao(num=[1,6,2,3,8])
    print shili
