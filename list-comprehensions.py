# 列表生成式

print(list(range(1, 11)))  #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 生成1x1, 2x2, 3x3...10x10
result = [x * x for x in range(1, 11)]
print(result)  #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 加上判断的筛选  筛选出偶数
result2 = [x * x for x in range(1, 11) if x % 2 == 0]
print(result2)   #[4, 16, 36, 64, 100]

# 两重循环
result3 = [m + n for m in 'abc' for n in 'xyz']
print(result3)  #['ax', 'ay', 'az', 'bx', 'by', 'bz', 'cx', 'cy', 'cz']


# 列出当前文件夹的内容

