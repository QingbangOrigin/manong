#数据结构典型的栈问题  思路：明确目标、分析过程、逐步执行、代码实现;选用while循环代码块
'''
#()\[]\{}    返回True
#([{}])      返回True
#([)]        返回false
# (){}[]      返回True
#((])        返回false
stack = []
while str_raw != "":
    if ...:
    elif...:
        if...:
        else:
if stack == []:
    return True
else:
    return False
'''
def check_brase(str_raw):
    if str_raw == "":
        return True

    #定义一个空列表，模拟栈。
    stack = []
    
    while str_raw != "":
        thisChar = str_raw[0]
        #如果本次循环的第一个字符是左括号，将其压栈
        if thisChar == "(" or thisChar == "{" or thisChar == "[":
            stack.append()
        elif thisChar == ")" or thisChar == "}" or thisChar == ']':
            len_stack = len(stack)
            if len_stack == 0:
                return False
            else:
                if thisChar == "(" and stack[len_stack-1] == "(":
                    stack.pop(len_stack-1)
                elif thisChar == "]" and stack[len_stack-1] == "[":
                    stack.pop(len_stack-1)
                elif thisChar == "]" and stack[len_stack-1] == "{":
                    stack.pop(len_stack-1)
                else:
                    return False
    if stack == []:
        return True
    else:
        return False
print(check_brace('(){}[]{()}'))
