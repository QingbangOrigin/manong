#coding=utf-8
#from  functools import wraps
#def decorator_name(f):
#    @wraps(f)
#    def decorated(*args, **kwargs):
#        if not can_run:
#            return "Function will not run"
#        return f(*args, **kwargs)
#    return decorated
#                                         
#@decorator_name
#def func():
#    return("Function is running")
#                                             
#can_run = True
#print(func())
## Output: Function is running
#                             
#can_run = False
#print(func())
## Output: Function will not run


#from functools import wraps
# 
#def logit(func):
#    @wraps(func)
#    def with_logging(*args,**kwargs):
#        print(func.__name__ + " was called")
#        return func(*args,**kwargs)
#    return with_logging
#@logit
#def addition_func(x):
#    """Do some math."""
#    return x + x                                    
#                
#result = addition_func(0)
## Output: addition_func was called

#class Person(object):
#    def __init__(self,name,gender):
#        self.name = name
#        self.gender = gender
#    def __call__(self,friend):
#        print("my name is %s..."%self.name)
#        print("my name is %s..."%friend)
#p = Person('Bob','Tom')
#p('Tim')

#class Chinese:
#    def __init__(self,name,birth,region):
#        self.name = name
#        self.birth = birth 
#        self.region = region
#    def born(self):
#        print(self.name,'出生在'+self.birth)
#    def live(self):
#        print(self.name,'居住在'+ self.region)
#person = Chinese('wangjian','河北','霸州')
#person.born()
#person.live()

#coding = utf-8

#class A:
#    def add(self,x):
#        y = x+1
#        print(y)
#class B(A):
#    def add(self,x):
#        super().add(x)
#b = B()
#b.add(2)

#def ceshi():
#   print(__init__)
#Py2.py
#!/usr/bin/env python
#import logging
#def use_logging(func):
#    def wrapper():
#        logging.warn("%s is running" % func.__name__)
#        return func()
#    return wrapper 
#@use_logging
#def foo():
#    print("i am foo")
#foo()

#import test
#print("一条大树")

import requests

#def send_post(url='www.baidu.com',data=None):
#    result = requests.post(url,data).json()
#    res = json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)
#    return res
#print(send_post())

result = requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=60997426243444153&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0').json()
#res = json.load(result)
print type(result)
