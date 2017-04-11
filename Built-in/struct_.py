#  struct
#     准确的讲，python没有专门的处理字节的数据类型，但由于b'str'可以表示字节，所以字节数组=二进制str
#     而在C语言中，我们可以方便地用struct，union来处理字节，自己字节和int，float的转换

#    在python中，比方说要把一个32位无符号整数编程字节，也就是4个长度的bytes，
n = 10240099
b1 = (n & 0xff000000) >> 24
b2 = (n & 0xff0000) >> 16
b3 = (n & 0xff00) >> 8
b4 = (n & 0xff)
bs = bytes([b1, b2, b3, b4])
print(bs)  # b'\x00\x9c@c'

#  非常麻烦，如果换成浮点数就无能为力
#  Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换
# struct的pack函数可以把任意数据类型变成bytes
import struct

print(struct.pack('>I', 10240099))  #  b'\x00\x9c@c'
#   > 表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数

print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))  # (4042322160, 32896)

# 根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数
# 所以尽管python不适合写底层操作系统字节流的代码，但对性能不高的地方，利用struct就方便多了


