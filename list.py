# list
classmate = ['bob', 'john', 'bill']
print(classmate)

print(len(classmate))

# 使用索引访问list中的数据
print(classmate[0], classmate[1], classmate[2])

# 越界
# print(classmate[4])

# 可以使用-1来获取最后一个元素 -2 倒数第二个，  -3 倒数第三个
print(classmate[-1])

# 追加数据  append()
classmate.append('tom')
print(classmate)    #['bob', 'john', 'bill', 'tom']

# 添加到指定位置   insert(index, element)
classmate.insert(1, 'Jack')
print(classmate)   #['bob', 'Jack', 'john', 'bill', 'tom']

# 删除末尾的元素  pop()
classmate.pop()
print(classmate)  #['bob', 'Jack', 'john', 'bill']

# 删除指定位置的元素 pop(index)
classmate.pop(1)
print(classmate) #['bob', 'john', 'bill']

#替换指定位置元素，直接赋值：classmate[index] = element
classmate[1] = 'kinderao'
print(classmate)  #['bob', 'kinderao', 'bill']

# list中的元素可以不同类型
classmate[1] = 123
print(classmate) #['bob', 123, 'bill']

# list中的元素可以是list,类似的可以添加元素作为二维，三维。。。多维数组
list = [1, 2, 3, 4]
classmate[1] = list
print(classmate) #['bob', [1, 2, 3, 4], 'bill']

