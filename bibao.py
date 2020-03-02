def waiBu(name):
    def neiQian():
        def neiQian1():
            def neiQian2():
                print('my name is',name)
            return neiQian2()
        return neiQian1()
    return neiQian()
if __name__=='__main__':
    #输出'my name is tory'
    waiBu('tory')
