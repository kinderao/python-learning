# 迭代器
#    可以直接使用for循环的数据结构有：
#               list，tuple， dict， set， str
#               还有一类是generator，包括生成器和带yield的generator function
#         这些可以直接使用for循环的对象统称为可迭代对象：Iterable
#         可以使用instance()方法来判断一个对象是否是Iterable对象

from collections import Iterable

a = [1, 2, 3]
print(isinstance(a, Iterable))  # True

print(isinstance({}, Iterable))  # True

print(isinstance('abc', Iterable))  # True

print(isinstance((x for x in range(10)), Iterable))  # True

print(isinstance(100, Iterable))  # False

# 而生成器不但可以作用于for循环，还可以使用next()方法调用
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器： Iterator
# 可以使用isinstance()来判断一个对象是否是Iterator对象

from collections import Iterator

print(isinstance((x for x in range(10)), Iterator))  # True

print(isinstance([], Iterator))  # False

print(isinstance({}, Iterator))  # False

#  生成器都是Iterator对象，但list，dict str等数据类型不是Iterator
#   这是因为Iterator对象表示的是一个数据流，Iterator对象可以被next()方法调用并不断返回下一个值
#   知道没有数据时抛出StopIteration错误，可以把这个数据流看成是一个有序序列，但我们不能提前知道这个序列的长度，
#   只能不断的使用next函数
#   Iterator甚至可以表示一个无限大的数据流，例如全体自然数，而使用list是永远不可能存储全体自然数的

#  总结：  凡是可以使用for循环的都是Iterable类型
#         凡是可以使用next()方法的对象的都是Iterator类型
#     list，dict， str等是Iterable而不是Iterator，但是可以使用iter()函数获得一个Iterator对象

aList = [1, 2, 3]
print(isinstance(iter(aList), Iterator))  # True

