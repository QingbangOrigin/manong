num = 'chejibadan'
def diGui(num):
    if len(num)<=1:
        return num 
    return diGui(num[1:])+num[0]
result = diGui(num)
print result

def str_num(num):
    print num[::-1]
    print "".join(reversed(num))
    print reversed(num),type(reversed(num))
str_num(num)


#def ce(num):
#    new_str=[]
#    index = len(num)
#    while index:
#        index = -1
#        new_str.append(num[index])
#    return ''.join(new_str)
