# 操作文件和目录

import os

print(os.name)  # posix
print(os.uname())  #  posix.uname_result(sysname='Darwin', nodename='yanghaodeMacBook-Pro.local', release='16.4.0', version='Darwin Kernel Version 16.4.0: Thu Dec 22 22:53:21 PST 2016; root:xnu-3789.41.3~3/RELEASE_X86_64', machine='x86_64')

# 环境变量
print(os.environ)
# 读取某个环境变量的值
print(os.environ.get('HOME'))  # /Users/yanghao

# 操作文件和目录
print(os.path.abspath('.'))  # /Users/yanghao/PycharmProject/python-learning


os.path.join("/Users/yanghao/", "testdir")
os.mkdir("/Users/yanghao/testDir")
os.rmdir("/Users/yanghao/testDir")

# 把两个字符串拼接成一个的时候，不要直接连接，而是使用os.path.join()方法，这样可以正确的处理不同操作系统的路径分隔符
#  同样，要拆分路径的时候，也不要直接去拆字符串，而是通过os.path.split()函数，这样可以吧一个路径拆分为两部分，后一个部分总是最后级别的目录或文件名

print(os.path.split("/Users/yanghao/hello.text"))  #('/Users/yanghao', 'hello.text')

# os.path.splitext()可以让你直接拆分文件扩展名
print(os.path.splitext('/Users/yanghao/hello.py'))  # ('/Users/yanghao/hello', '.py')

# 路径的拆分合并并不需要真实的文件存在，他们只对字符串进行操作

#  文件的操作使用下面的方法
#     os.rename('test.py', 'test.java')
#     os.remove('test.java')
# 但是os中并没有文件的复制，原因是复制文件并非是由操作系统提供的系统调用
# 而是有shutil模块提供copyfile（）函数，你还可以在shutil中找到很多有用的函数，可以看做是对os模块的补充
listdir = [x for x in os.listdir('.') if os.path.isdir(x)]
print(listdir)  # 会列出当前目录下的文件夹





