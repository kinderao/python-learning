# 理解变量
a = 'abc'
b = a
a = 'xyz'
print(b) # b = 'abc'

# python支持一种赋值运算，按位赋值
a, b = 1, 2
print(a)  # 1
print(b)  # 2
# 其实只不过是先将右边的组装为一个tuple
# 然后再讲tuple取出unpack给左边的元素，
#  t = (1, 2)
#  a = t[0]
#  b = t[1]


x, y = 1, 2
x, y = y ,x + y
print(x, y)  # 2, 3
#  t = (y, x + y)
#  x = t[0]
#  y = t[1]