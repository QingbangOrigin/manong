#coding=utf-8
list_s = ['a','b','c']
str_s = "{{}}()"
dict_s = {'小明':'90','小兰':'80'}
list_kong = []
'''
for i in str_s:
    print i
    print type(i)
for j in list_s:
    print j 
    print type(j)
'''
'''
for a in str_s:
    if a == '{' or a=='(':
        list_kong.append(a)
print list_kong'''
#while str_s != "":
#    if str_s[0]== '{' or str_s[0]=='(':
#        list_kong.append(str_s)
#print list_kong
for iterm in dict_s:
    print dict_s[iterm]
    print type(dict_s[iterm])
