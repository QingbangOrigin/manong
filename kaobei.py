import copy

a = [1,2,3,4,5,['a','b']]   #原始对象
b = a   #赋值，传对象的引用
c = copy.copy(a)    #对象浅拷贝
d = copy.deepcopy(a)    #对象深拷贝

print('a=',a,'  id(a)=',id(a),'id(a[5])=',id(a[5]))
print('b=',b,'  id(b)=',id(b),'id(b[5])=',id(b[5]))
print('c=',c,'  id(c)=',id(c),'id(c[5])=',id(c[5]))
print('d=',d,'  id(d)=',id(d),'id(d[5])=',id(d[5]))
print("*"*80)
#变换数值地址不变
a.append(6)
a[5].append('c')
print('a=',a,'  id(a)=',id(a),'id(a[5])=',id(a[5]))
print('b=',b,'  id(b)=',id(b),'id(b[5])=',id(b[5]))
print('c=',c,'  id(c)=',id(c),'id(c[5])=',id(c[5]))
print('d=',d,'  id(d)=',id(d),'id(d[5])=',id(d[5]))

