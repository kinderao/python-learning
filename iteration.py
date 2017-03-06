# 迭代
# python 的for循环抽象程度高于java
# python的for循环不仅可以作用在list或tuple上，还可以作用在其他可迭代对象上 str， dict。。。

# 迭代str
aStr = 'hello world'
for x in aStr:
    print(x)

# 迭代dict  因为dict内部不是有序的，所以迭代结果顺序也可能是不一样的
aDict = {1 : 'hello', 2 : 'world', 3 : 'everyone'}
for x in aDict:
    print(aDict[x])

###   可迭代对象：
#         只要是可迭代对象就可以使用for循环来迭代
#         判断是否可迭代：collections模块的Iterable类型判断
from collections import Iterable

print(isinstance(aStr, Iterable))  # True

# 使用索引迭代list
for i, value in enumerate(['a', 'b', 'c', 'd', 'e']):
    print(i, value)

# 迭代中使用两个变量
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)