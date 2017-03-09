#  高阶函数

#  变量可以指向函数
print(abs(20))  # 20

print(abs)   # <built-in function abs>

f = abs
print(f)   # <built-in function abs>

print(f(-2))   # 2


# 函数名也是变量
abs = 10
# print(abs(10))  # TypeError: 'int' object is not callable


# 传入函数
#  既然函数可以看做变量，函数的参数可以接受变量，那么一个函数就可以接受另一个函数作为参数
def add(x, y, f):
    return f(x) + f(y)

def f(x):
    return x * x

print(add(2, 3, f))  # 13 = 2 * 2 + 3 * 3

# 编写高阶函数，让函数的参数可以接收别的函数