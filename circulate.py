# 循环
# 两种循环 ：1, for...in
#           2, while ...:

array = [1, 2, 3, 4]
for x in array:
    print(x)

# rangge()函数 可以生成一个整数序列
for y in list(range(10)):
    print(y)
    # 在此处还能访问到x，x的值为最后的一次遍历时的值

# while 循环
while len(array):
    print(array)
    array.pop()


# break 可以退出循环
for y in [1, 2, 3, 4, 5]:
    print(y)
    if y > 2:
        break


# continue 跳过本次循环
n = 0
while n < 10:
    n = n + 1
    if n == 3:
        continue
    print(n)
