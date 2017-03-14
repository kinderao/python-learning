# 匿名函数
#  当我们在传入函数的时候，不需要显式地定义函数，直接传入匿名函数更方便

# 在python中，对匿名函数提供了有限的支持

print(list(map(lambda x: x * x, [1, 2, 3, 4, 5])))  # [1, 4, 9, 16, 25]

# 此处的匿名函数lambda x : x * x 实际上就是：
def f(x):
    return x * x

# 关键字lambda表示匿名函数，冒号前面的x表示函数参数
#  但是匿名函数有一个限制就是只能有一个表达式，不用写return。 返回值就是该表达式的结果, 不同于java的lambda， 匿名函数可以有多个表达式，多个表达式使用{}包起来即可
#  使用匿名函数有个好处就是不用考虑函数重名的问题，也可以将匿名函数赋值给另一个变量，再使用变量来调用该函数

f = lambda x : x * x
print(f)  #  <function <lambda> at 0x108081730>
print(f(3))   # 9

# 同样，也可以将匿名函数作为返回值返回
def build(x, y):
    return lambda: x * x + y * y

