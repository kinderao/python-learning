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
import os

print([d for d in os.listdir('.')])  #['.git', '.gitignore', '.idea', '__pycache__', 'circulate.py', 'data-type-boolean.py', 'data-type-string.py', 'decode.py', 'dict.py', 'function-call-in-other-file.py',
                                     # 'function-parameter.py', 'function-recursion.py', 'function.py', 'if-else.py', 'input.py', 'iteration.py', 'list-comprehensions.py', 'list.py',
                                     # 'print.py', 'README.md', 'set.py', 'slice.py', 'tuple.py', 'variable.py']


# for循环可以同时使用两个或多个变量 比如dict的item() 可以同时迭代key和value
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, v)
# 所以列表生成时可以使用两个变量来生成list
gen_result = [k + '=' + v for k, v in d.items()]
print(gen_result)    #['x=A', 'y=B', 'z=C']

# 把一个字符串中所有字母变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
gen_result2 = [s.lower() for s in L]
print(gen_result2)   #['x=A', 'y=B', 'z=C']
# 但是如果list中的不全是字符串，包含有整数的话，会出错
L2 = ['Hello', 'World', 'IBM', 123, 'Apple', None]
gen_result3 = [s.lower() for s in L2 if isinstance(s, str)]
print(gen_result3)