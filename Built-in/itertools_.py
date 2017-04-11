#  itertools
#     Python的内置模块itertools提供了非常有用的用于操作迭代对象的函数
#    首先看看itertools提供的几个"无限"迭代器


#   count
import itertools
# natuals = itertools.count(1)
# for n in natuals:
#     print(n)
#  count()会创建无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来，只能ctrl c

#    cycle
#    会把传入的序列无限重复下去
# cs = itertools.cycle('ABC')
# for n in cs:
#     print(n)


#    repeat
#     repeat()负责把一个元素无限重复下去，不过如果体用第二个参数就可以限定重复次数
ns = itertools.repeat('A', 3)
for n in ns:
    print(n)

#  takewhile
#  无限序列只有在for迭代的时候才会无限迭代下去，如果只是创建了一个迭代对象，他不会事先把无限个元素生成出来
#  无限序列虽然可以无限迭代下去，但是通常我们都会通过takewhile（）等函数根据条件判断来截取一个有限的序列

natuals = itertools.count()
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



#  chain
#    chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('ABC', 'XYZ'):
    print(c)


#  groupby
#      groupby()把迭代器中相邻的重复对象跳出来放在一起
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))
    # A ['A', 'A', 'A']
    # B ['B', 'B', 'B']
    # C ['C', 'C']
    # A ['A', 'A', 'A']
#  实际上挑选规则都是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，而函数返回值作为组的key。
#   如果我们需要忽略大小写分组，就要让元素'A'和'a'都返回相同的key
for key,group in itertools.groupby('AAaBBbcCCCAAaa', lambda c: c.upper()):
    print(key, list(group))


###   itertools模块提供的都是处理迭代功能的函数，他们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算
