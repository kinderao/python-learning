# python内置很多函数，我们可以直接调用
print(abs(100))

# 调用一个函数，需要知道函数名称，以及参数的个数，类型
result = max(1, 2)
# 如果传递的参数个数不正确，会报TypeError
# abs(1, 2)
# 如果传递参数的类型不被接受，也会报TypeError
# sum('ab', 'cd')

# 数据类型转换
# int()
print(int('123'))
print(int(12.34))

# float()
print(float("12.33"))

# str()
print(str(123))
print(str(12.23))

# bool()
print(bool(1))
print(bool(''))

#
# 函数的定义：def语句，然后依次写出函数名，括号，括号中的参数和冒号
# 一旦执行到return，函数就执行完毕，并将结果返回，如果没有return语句，函数执行完毕也会返回结果，结果为None
# return None可以简写为return
def my_abs(x):
    if x > 0:
        return x
    else:
        return -x

#调用
print(my_abs(-2))

# 函数的跨文件调用
# 参见function2.py

# 空函数
def nop():
    pass
# 也可以使用pass来做占位符
a = 10
if a > 0:
    pass


# 参数检查  调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError
# my_abs(1, 2)

# 如果参数的类型不对，解释器就无法检查了
# >>> my_abs('A')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 2, in my_abs
# TypeError: unorderable types: str() >= int()
# >>> abs('A')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: bad operand type for abs(): 'str'

# 类型检查
def my_abs2(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# my_abs2('abc')


# 返回多个值
import math

def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny

x, y = move(0, 0, 100, math.pi / 4)
print(x, y) # 70.71067811865476 70.71067811865474
# 其实python的返回值认识单一值
r = move(0, 0, 100, math.pi / 4)
print(r)  #(70.71067811865476, 70.71067811865474)
# 返回的是一个元组tuple 不过返回tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值
# x, y, z = move(0, 0, 100, 0)  会报错

# 解一元二次方程
def quadratic(a, b, c):
    if not (isinstance(a, (int, float))
            and isinstance(b, (int, float))
            and isinstance(c, (int, float))):
        raise TypeError('bad parameter')
    else:
        if a == 0:
            if b == 0:
                return False
            else:
                return -c / b

        dert = b * b - 4 * a * c
        if dert > 0:
            return (-b + math.sqrt(dert)) / 2 * a, (-b - math.sqrt(dert)) / 2 * a
        elif dert == 0:
            return (-b + math.sqrt(dert)) / 2 * a
        else:
            return False


print(quadratic(1, -2, 1))

