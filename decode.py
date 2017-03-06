# ord() 获取字符的编码
print(ord('A'))

# chr() 将编码转换成字符
print(chr(65))

# python 对bytes类型的数据用b''前缀表示
x = b'abc'
print(x)

# 以unicdoe表示的str可以通过encode()方法编码Wie指定的bytes
'abc'.encode('ascii')
'abc'.encode('utf-8')
'中文'.encode('utf-8')

# decode() 方法进行解码
b'abc'.decode('utf-8')
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')) # = 中文