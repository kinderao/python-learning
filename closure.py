# 函数作为返回值
#   实现一个求和函数，可以不返回求和的值，而是返回求和的函数

# 通常是这样定义的
def calc_sum(*args):
    ax = 0
    for x in args:
        ax = ax + x
    return ax

# 但是我们可以不返回值，而是返回计算的方法
def lazy_sum(*args):
    def sum():
        ax = 0
        for x in args:
            ax = ax + x
        return ax
    return sum

f = lazy_sum(1, 2, 3, 4, 5)
print(f)  # <function lazy_sum.<locals>.sum at 0x10d434730>
print(f())  # 15

# 在这个例子中，我们在函数lazy_sum()中定义了函数sum()， 并且内部函数sum可以引用外部函数的参数和变量，
#    当lazy_sum返回函数sum时，相关的参数和变量都保存在返回的函数中，这种称为闭包


f1 = lazy_sum(1, 2, 3, 4, 5)
f2 = lazy_sum(1, 2, 3, 4, 5)
print(f1 == f2)  # False
#  当再次调用lazy_sum函数的时候返回的又是另外一个新的函数

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs
f1, f2, f3 = count()

print(f1())  # 9
print(f2())  # 9
print(f3())  # 9
# 原因在于返回的函数应用了变量i，但他并非立即执行，等到三个函数都返回时，他们所引用的变量i已经变成了3，因此最终结果为9
#  使用闭包必须牢记有点： 返回函数不要应用任何循环变量，或者后续会变化的变量

# 如果一定要使用循环变量，可以再创建一个方法，用该函数的参数绑定循环变量当前的值，无论后续循环变量怎么修改，已绑定到函数参数上的值不变

def count():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count()
print(f1())   # 1
print(f2())   # 4
print(f3())   # 9

