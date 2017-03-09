# map函数
# map函数接收两个参数，一个是函数，一个是Iterable，
#                       map将传入的函数作用到序列上的每一个元素，并将结果作为新的Iterator返回

# 实现一个f(x) = x^2
def f(x):
    return x * x

a = map(f, list(range(10)))
aList = list(a)
print(aList)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def add(x, y):
    return x + y

print(reduce(add, list(range(10))))  # 45


# 把序列[1, 3, 5, 7, 9]变换成整数13579
def fn(x, y):
    return x * 10 + y

print(reduce(fn, [1, 3, 5, 7])) # 1357

# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
aList = ['adam', 'LISA', 'barT']
def to_upper(x):
    result = ''
    result += x[0].upper()
    for index in range(1, len(x)):
        result = result + x[index].lower()
    return result

print(list(map(to_upper, aList)))


# 求积
def prod(x):
    return reduce(lambda x, y: x * y, x)

print(prod([1, 2, 3, 4, 5]))  # 120

# 字符串转浮点数
def str2float(s):
    n = len(s) - s.index('.') - 1
    number_list = map(fn, s)
    result = reduce(convert, number_list)
    result /= 10 ** n
    return result

def convert(x, y):
    if y == '.':
        return x
    else:
        return x * 10 + y

def fn(x):
    return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '.':'.'}[x]

print(str2float('12.23'))