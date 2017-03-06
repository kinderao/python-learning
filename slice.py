# 切片
l = ['jack', 'tom', 'bob', 'marry']

# startIndex:endIndex 从开始索引取，直到结束索引，但不包括结束索引
#   0:2  l[0], l[1] 两个元素
print(l[0:2])  #['jack', 'tom']

# 如果第一个索引为0，可以省略
print(l[:2])   #['jack', 'tom']

# 同样支持倒数索引
print(l[-2:-1])   #['bob']

# 指定切片的间隔
print(l[0:-1:2])  #['jack', 'bob']
# 前后索引都没有，指所有元素
print(l[::3])   #['jack', 'marry']
print(l[::])
# 什么都不写只写一个冒号：，可以原样复制一个list
another = l[:]
print(another)   #['jack', 'tom', 'bob', 'marry']

#
# tuple 也可以切片，只是操作的结果还是tuple

# 字符串也可以看做是list，每个元素都是一个字符，字符串也可以使用切片操作，结果认识字符串
aStr = 'helle world'
print(aStr[1:3])  #el

# 有了切片，原来需要很多循环才能实现的，使用切片就能搞定   一行代码完成多行循环才能完成的操作