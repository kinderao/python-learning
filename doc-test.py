#  doctest
#  文档测试
#     写在注释里面的代码可以执行测试
#      doctest严格按照python交互式命令行的输入和输出来判断测试结果是否正确，只有测试正常时可以用...表示中间一段烦人的的输出



# class Dict(dict):
#     '''
#     Simple dict but also support access as x.y style.
#
#     >>> d1 = Dict()
#     >>> d1['x'] = 100
#     >>> d1.x
#     100
#     >>> d1.y = 200
#     >>> d1['y']
#     200
#     >>> d2 = Dict(a=1, b=2, c='3')
#     >>> d2.c
#     '3'
#     >>> d2['empty']
#     Traceback (most recent call last):
#         ...
#     KeyError: 'empty'
#     >>> d2.empty
#     Traceback (most recent call last):
#         ...
#     AttributeError: 'Dict' object has no attribute 'empty'
#     '''
#     def __init__(self, **kw):
#         super(Dict, self).__init__(**kw)
#
#     def __getattr__(self, key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
#
#     def __setattr__(self, key, value):
#         self[key] = value
#


def fact(n):
    '''
    tes
    >>> fact(1)
    1
    >>> fact(2)
    2
    >>> fact(0)
    Traceback (most recent call last):
      File "<pyshell#13>", line 1, in <module>
        fact(0)
      File "<pyshell#10>", line 3, in fact
        raise ValueError()
    ValueError
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)

if __name__=='__main__':
    import doctest
    doctest.testmod()

# 如果测试失败会抛出异常

