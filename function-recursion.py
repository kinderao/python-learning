# 递归
#  求阶乘

def fact(n):
    if n == 1:
        return 1
    return fact(n -1) * n

print(fact(4))

# 优化为尾递归
def fact2(n):
    return fact_iter(n, 1)

def fact_iter(n, result):
    if n == 1:
        return result
    return fact_iter(n - 1, result * n)

print(fact2(5))


# 汉诺塔
#     三个步骤：
#         1，将最大盘子上面的盘子移到b   move(n - 1, a, c, b)
#         2，将最大的那个盘子移到c      print(a, '->', c)
#         3，将b上的那些盘子移到c       move(n - 1, b, a, c)

def move(n, a, b, c):
    if n == 0:
        return
    move(n - 1, a, c, b)
    print(a, '->', c)
    move(n - 1, b, a, c)

move(4, 'A', 'B', 'C')