# 偏函数 Partial function
#    functools模块提供了很多有用的功能，其中一个就是偏函数

# 介绍函数参数时，通过时候默认参数可以降低函数调用时的难度，而偏函数也可以做到这一点

# 将'12345'转化为int
print(int('12345'))
# 但是int函数还提供额外的base参数，默认值为10，如果传入base参数，就可以做到N进制的转换
print(int('12345', base=8))  # 5349

print(int('12345', base=16))  # 74565

# 而如果有大量的二进制需要转换，每次都要传入base=2,那将非常繁琐
#  我们可以定义一个函数
def f(x):
    return int(x, base=2)

print(f('10'))  # 2

#  也可以借助于偏函数，而不需要自己定义函数
import functools
int2 = functools.partial(int, base=2)
print(int2('100'))  # 4

# 简单总结，functools.partial的作用就是，把一个函数的某些参数给固定住，也就是设置默认值，返回一个新的函数，调用这个函数就会简单
