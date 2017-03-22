# StringIO 和 BytesIO
#
#    StringIO：
#         很多时候，数据读写不一定在文件，也可以在内存中读写
#         StringIO就是在内存中读写str

from io import StringIO

f = StringIO('hello world')
while True:
    s  = f.readline()
    if s == '':
        break
    print(s.strip())


#     BytesIO：
#          BytesIO就是在内存中读写二进制数据
#          BytesIO和StringIO类似，不过操作的是二进制数据