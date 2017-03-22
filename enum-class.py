# 枚举类
#   当我们定义常量时，一个办法是用大写变量通过整数来定义，例如月份

JAN = 1
FEB = 2
MAR = 3

# 这样写好处是简单，缺点是类型是int，并且仍然是变量
# 更好的办法是为了这样的枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例，python提供了Enum类来实现这个功能

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', 'member', ',', member.value)

# Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较
