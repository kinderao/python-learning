# 文件读写
#   读写文件是常见的IO，Pyhon内置读写文件的函数，与C用法是兼容的

#    读文件
f = open('.gitignore', 'r')  #如果文件不存在  FileNotFoundError: [Errno 2] No such file or directory: '.gitignoddre'
print(f.read())

# 文件打开成功后，可以用read()方法一次读取文件的全部内容，Python会把内容读到内存，用一个str对象表示
f.close()

# 最后一步是调用f.close()方法关闭文件，文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的

# 由于文件的读写都可能会参数IOError，一旦出错，后面的f.close()就不能调用了，所以，为了保证无论是否出错都能正确的关闭文件，我们可以使用try...finally...来实现
#   但是每次都要写try...finally...很麻烦，我们可以使用with语句来自动帮我们调用close(）方法

with open('.gitignore', 'r') as f:
    print(f.read())

# 调用read()方法会一次性读取文件的全部内容，如果文件有10g，内存就爆了，所以为了保险起见，可以反复调用read（size）方法，每次最多读取size个字节的内容
# 另外，调用readline()可以每次读取一行，调用readlines（）一次读取所有内容然后返回一个list，因此，要根据需要决定怎么调用


#
#
#   file-like  object
#
#
#   像open函数返回的这种有个read（）方法的对象，在python中统一称为file-like object，除了file以外，还可以是内存的直接流，网络流，自定义流等等
#      file-like object不要求从特定类继承，只要有个read方法就行
#   StringIO就是在内存中创建的file-like object，常用作临时缓冲

#   二进制文件
#     前面讲过的默认都是读取文本文件，并且都是utf0编码的文本，而如果要读取二进制文件，比如图片，视频等等，用'rb'模式打开文件即可

f = open('/Users/yanghao/Pictures/Snip20170217_1.png', 'rb')
print(f.read())  # b'\x89PNG\r\n\x1a\n\x00\x00\x.......


#   字符编码
#       要读取非UTF-8编码的文本文件，需要给open()方法传入encoding参数，例如读取ascii
f = open('README.md', 'r', encoding='ascii')
print(f.readline())
#    如果碰到一些不规范的文件，可能会遇到UnicodeDecodeError，因为在文本文件中可能会夹杂一些非法编码的字符，遇到这种情况，open(）函数还接收一个errors参数，便是如果遇到编码错误后怎么处理
#    最简单的方式是直接忽略
f = open('README.md', 'r', errors='ignore')
print(f.read())





#
#
#       写文件
#           读文件和写文件都是一样的，唯一的区别是调用open函数时，传入标识符'w'，或者'wb'表示写文本文件还是写二进制文件
#

f = open('abc.txt', 'w')
f.write('Hello World')
f.close()
#  通用可以反复调用write来写文件，但是务必要调用close来关闭文件，我们写文件时，操作系统不会马上将数据写入磁盘，而是放到内存中缓存起来，空闲的时候再慢慢写入，只有调用close方法时，
# 操作系统才把没有写入的数据全部写入磁盘。所以还是用with比较保险

with open('abc.txt', 'w') as f:
    f.write('hello world')

#  要写入特定编码的文件，需要给open函数传入encoding参数，将字符串自动转换成指定编码

#   在IO中，使用with是个好习惯