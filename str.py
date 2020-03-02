#coding=utf-8
str_num = 'abcd'

#字符串切片
str_s = 'Qihang'
print str_s[::-1],type(str_s[::-1])

#reversed()函数,入参内容可以是数组、字符串、列表、字典
print "".join(reversed(str_s)),type( "".join(reversed(str_s)))

#结合循环字符串反转
#def reverse_str(str):
#    new_str = []
#    index = len(str)
#    while index:
#        index -= 1
#        new_str.append(str[index])
#    return ''.join(new_str)

#递归思想,递归向里面往外扩展呈现出来的也就是从里到外的
#def func(str_num):#    
#if len(str_num) <1:
#        return str_num
#    return func(str_num[1:])+str_num[0]
#result = func(str_num)
#print result



##回文
def myPalindrmoe(strs):
    mystr = str(strs)
    if mystr == ''.join(reversed(mystr)):
        print 'True'
    else:
        print 'False'
#if __name__ == "__main__":
#    print"请输入字符串",
#    s = raw_input()
#    myPalindrmose(s)
#

##统计字符中字母个数
strs = input("请输入一串字符串：")
resoult = {}
for i in strs:
    resoult[i] = strs.count(i)
print result
