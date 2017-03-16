# 模块
#  python中一个文件就是一个模块   sys.py就是一个模块
#  python 有内置模块  还有很多第三方的模块
#      如果模块名称相同，还可以通过包名来区分
#          例如： 包名为kinderao下的my.py文件的模块名就是：kinderao.my，这样就可以避免重名的问题
#      每一个包名下必须要有一个__init__.py文件，如果这个文件不存在，python会把当前目录当做普通目录
#           这个__init__.py文件可以是空文件，也可以是python代码，因为__init__.py就是一个模块，模块名就是包名
#
#
#  import: 使用import来导入模块，然后在代码中就能使用该模块
#
#
# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# ' a test module
#
# __author__ = 'Michael Liao'
#
# import sys
#
# def test():
#     args = sys.argv
#     if len(args)==1:
#         print('Hello, world!')
#     elif len(args)==2:
#         print('Hello, %s!' % args[1])
#     else:
#         print('Too many arguments!')
#
# if __name__=='__main__':
#     test()

# 上述就是一个引用示例

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('hello world')
    elif len(args) == 2:
        print('hello, %s' % args[1])
    else:
        print('too many arguments')
if __name__ == '__main__':
    test()


# sys模块有一个args变量，用list存储了命令行的所有参数，argv至少有一个元素，就是该py文件的名称
#   python3 hello.py 获得的sys.argv 就是 ['hello.py']
#   python3 hello.py kinderao  获得的sys.argv 就是['hello.py', 'kinderao']


# 最后两行代码  if __name__ == '__main__':
#                  test()
#   当我们在命令行运行hello模块文件时，python解释器会把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断会返回false
#       这种通过命令行运行时执行一些额外的代码，最常见的就是运行测试

# $ python3 hello.py
# hello world
# $ python3 hello.py kinderao
# hello kinderao

# 可以看到，在命令行中直接运行该模块时，test方法会执行， 而如果通过import在其他模块使用的话，test方法就不会执行



#
#
#    作用域
#        在一个模块中，会定义很多函数和变量，有的仅仅希望在模块内部使用，在Python中，通过_前缀来实现的
#
#           正常的函数和变量是公开的（public），可以直接被应用，比如：abc， x123， PI
#
#           类似__xxx__ 这样的变量就是特殊变量，可以直接应用，但是有特殊用途，比如上面的__author__,__name__就是特殊变量，模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名
#
#           类似 _xxx 和 __xxx这样的变量就是非公开的（private），不应该被直接引用
#
#        之所以我们说private变量和函数"不应该"被直接引用，而不是"不能"被直接引用，是因为Python中并没有一种方法可以完全限制访问private函数或变量，但是从编程习惯上不应该引用privae函数或变量
#
#
#   以上private和public就是封装的思想，需要外部调用的使用public，不需要的使用private，外部不需要知道内部的private函数细节


#
#   安装第三方的模块
#
#       包管理工具： pip    pip3 install module
#                然后在代码中import 使用即可
#
#       模块搜索路径： 当前目录 -> 所有已安装的内置模块 -> 第三方模块  搜索路径存放在sys模块的path变量中
#
print(sys.path)  # ['/Users/yanghao/PycharmProjects/python-learning', '/Users/yanghao/PycharmProjects/python-learning',
                 # '/usr/local/Cellar/python3/3.6.0/Frameworks/Python.framework/Versions/3.6/lib/python36.zip',
                 # '/usr/local/Cellar/python3/3.6.0/Frameworks/Python.framework/Versions/3.6/lib/python3.6',
                 # '/usr/local/Cellar/python3/3.6.0/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload', '/usr/local/lib/python3.6/site-packages']


#  如果需要添加自己的搜索目录：
#         1， 直接修改sys.path
#
#         2,  设置环境变量PYTHONPATH  该环境变量会自动添加到模块搜索路径中，设置方式和path类似。只需要添加自己的搜索路径，python自己本身的搜索路径不受影响
#