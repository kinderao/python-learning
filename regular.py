#  正则表达式

#   \d 数字
#   \w 字母
#
#   . 匹配任意字符

#   * 任意个字符
#   + 一个或多个字符
#   ? 一个或零个字符
#   {m,n} m-n个字符
#   \ 转义字符

#  A|B 可以匹配A或B
#  ^ 表示行的开头
#  $ 表示行的结束

#  re模块
import re
s = r'ABC\-001'
if re.match(r'^\d{3}\-\d{3,8}$', '010-12345'):
    print('ok')
else:
    print('failed')


# 切分字符串
print('a b   c'.split(' '))  # ['a', 'b', '', '', 'c']
# 无法识别连续的空格
print(re.split(r'\s+', 'a b   c'))  # ['a', 'b', 'c']
print(re.split(r'[\s\,\;]+', 'a,b,,,   c'))
#  可以使用正则分割将不规范的输入转化为正确的数组

#  分组
m = re.match(r'(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0))  # 010-12345
print(m.group(1))  # 010
print(m.group(2))  # 12345
# 使用group将Match对象取出子串来， group（0）永远是原始字符串，group（1），group（2）表示第一个，第二个子串



#  贪婪匹配
#  正则默认是贪婪匹配，也就是尽可能的匹配多的字符，举例如下，匹配出数字后面的0
print(re.match(r'^(\d+)(0*)$', '102300').groups())


#  编译
#    当我们在python中使用正则表达式时，re模块内部会干两件事情
#      1，编译正则表达式，如果正则表达式的字符串本身不合法，会报错
#      2，用编译后的正则表达式去匹配字符串
#   如果一个正则表达式可以重复使用千次，处于效率的考虑，我们可以预编译该正则表达式
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('101-2134').groups())  # ('101', '2134')
print(re_telephone.match('010-8086').groups())   #  ('010', '8086')
