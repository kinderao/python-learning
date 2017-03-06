#
# 函数的参数
#
#
#    1， 位置参数
#
#
# 求平方
def power(x):
    return x * x
# 求n次方
def power2(x, n):
    result = x
    while n > 1:
        result = result * x
        n = n - 1
    return result

# 同时可以直接求平方 和 n次方
#
#
#    2， 默认参数
#
#
def power3(x, n=2):
    result = x
    while n > 1:
        result = result * x
        n = n - 1
    return result
# 默认参数放在后面，多个默认参数时，既可以按照顺序提供默认参数，也可以直接指定提供部分默认参数
def enroll(name, gender, age=6, city='beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll('bob', 'M', )
enroll('bob', 'M', 7)
enroll('bob', 'M', 7, 'beijing')
enroll('bob', 'M', city='beijing')

# 默认参数必须指向不可变对象
def add_end(l=[]):
    l.append('end')
    return l

print(add_end()) # ['end']
print(add_end()) # ['end', 'end']
# 原因： 函数在定义的时候，默认参数就被计算出来了，默认参数也是一个变量
#        保存到一个变量中，指向对象[]，而每次调用函数都会去改变l的内容
#
#
#     3，可变参数————参数个数不定
#
#
# 有时由于参数的个数不确定，可以考虑使用一个list获取tuple将参数传进来
# 更方便的方法就是使用可变参数, 在参数的前面加一个*号，函数内部，参数接收到的是一个tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum
print(calc(1, 2, 3, 4, 5))
#
#
#     4，关键字参数
#
#
#  可变参数是自动将多个参数组装为tuple，而关键字参数允许将多个参数组装为一个dict
def person(name, age, **kw):
    print('name:', name, 'age:',age, 'other:', kw)

person('yanghao', 22, city='chegndu', job='java')
# 还可以先组装一个dict:
#                     然后直接传入dict
extra = {'city': 'chengdu', 'job': 'java'}
person('yanghoa', 22, **extra)
#                     按照key将value传入
person('yanghao', 22, city = extra['city'], job = extra['job'])
#
#
#    5，命名关键字参数
#
#       必须传入指定了的参数，限制关键字参数中传递的参数
#
def person2(name, age, *, city, job):   # 此处的*号 为分隔符， * 号后面的参数被视为命名关键字参数
    print(name, age, city, job)

# 调用
person2('Jack', 34, city='beijing', job='python')


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不在需要一个分隔符 * 了
def person3(name, age, *kw, city, job):
    print(name, age, kw, city, job)
# 调用
person3('jain', 20, '123', '11', city='chengdu', job='php') # 如果缺少命名参数，将报错

#
#     参数组合:
#           在python中定义函数，可以用比选参数，默认参数，可变参数，关键字参数， 命名关键字参数
#            这五种参数可以组合使用，但是注意参数的顺序必须是：必选参数，默认参数，可变参数，命名关键字参数， 关键字参数
#
