#  base64
#    Base64是一种用64字符来表示任意二进制的方法
#    原理： 准备一个包含64个字符的数组： ['A', 'B', 'C', ... 'a', 'b', 'c', ... '0', '1', ... '+', '/']
#          然后将需要处理的二进制数据按照每三个字节一组，一共3 x 8 = 24bit，划分为4组， 每组6个bit
#          这样得到4个数字作为索引，然后查表，获取相应的4个字符，就是编码后的字符串
#    这样，二进制数据编码为字符串后就可以直接在网页，邮件中直接显示了
#    如果二进制的位数不是刚好3的倍数，就在末尾用\x00补足，再在末尾加上一个或两个=号，解码的时候回自动去掉

#  python内置的base64可以直接进行base64的编解码
import base64

print(base64.b64encode(b'binary\x00string'))  # b'YmluYXJ5AHN0cmluZw=='
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))   # b'binary\x00string'

#   由于标准的Base64 编码后可能出现字符+和/，在url中不能直接作为参数，所以又有一种'URL safe'的base64编码，其实就是把字符+和/分别编程-和_
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))  # b'abcd++//'
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))   # b'abcd--__'


