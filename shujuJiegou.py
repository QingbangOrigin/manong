#coding=utf-8

#实现堆栈，堆栈遵循后进先出原则。
letters = []

letters.append('c')
letters.append('a')
letters.append('t')
letters.append('g')

last_item = letters.pop()
print last_item

last_item = letters.pop()
print last_item

print letters



#队列，遵循先进先出原则
fruits = []

fruits.append('banana')
fruits.append('grapes')
fruits.append('mango')
fruits.append('orange')

first_item = fruits.pop(0)
print first_item

first_item = fruits.pop(0)
print first_item

print fruits
