# 生成器
#  通过列表生成式，可以直接创建一个列表，但是会受到内存限制，列表容量肯定有限
#  而如果列表的元素可以通过某种算法算出来，我们就可以推算出后面的元素，不必创建完整的list
#  在python中，这种一边循环一边计算的机制称为：生成器（generator）

# 把列表生成式中的中括号编程小括号即可 [] -> ()
var = (x * x for x in range(10))
print(var)  # <generator object <genexpr> at 0x10c934e08>

# 列表生成式可以直接打印出来，而生成器需要通过next()方法来进行获取
for x in range(10):
    print(next(var))
# 相当于生成器中保存的是算法，而每次需要下一个元素的时候，就是用next方法来计算出下一个元素的值，
#  直到没有更多元素的时候，抛出StopIteration的错误


# 菲波那切数列
def fib(max):
    n, curr, next_ = 0, 0, 1
    while n < max:
        print(next_)
        curr, next_ = next_, curr + next_
        n = n + 1
    return 'done'
fib(10)

# 用生成器生成菲波那切数列
def fib2(max):
    n, curr, next_ = 0, 0, 1
    while n < max:
        yield next_
        curr, next_ = next_, curr + next_
        n = n + 1
    return 'done'
# 此时的fib2不是普通函数，而是generator，在执行过程中遇到yield就会中断，下次又会继续执行

f = fib2(6)
for x in f:
    print(x)


# 生成器输入平方数列
def square(n):
    index = 1
    while index <= n:
        yield index * index
        index = index + 1
    return 'done'
for x in square(5):
    print(x)

# 打印杨辉三角
def triangles(n):
    a = [1]
    for x in range(n):
        a.append(0)
        a.insert(0, 0)
        a = [a[y] + a[y+1] for y in range(x + 1)]
        yield a
print('--------')
for index in triangles(10):
    print(index)

