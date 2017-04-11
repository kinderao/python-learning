#  hashlib
#    Python的hashlist提供了常见的摘要算法，如MD5，SHA1等等
#

import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())  # d26a53750bc40b38b65a520292f69306

#   如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的
md5 = hashlib.md5()
md5.update('how to use md5 '.encode('utf-8'))
md5.update('in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())  # d26a53750bc40b38b65a520292f69306

#  改动其中的一个字符后生成的md5值都会变化

# 另一种常见的算法是sha1，调用和md5完全类似

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())  # 2c76b57293ce30acef38d98f6046927161b46a44

#   摘要算法的应用
#      任何允许用户登录的网站都会把用户名和密码存储到数据库中，如果数据库泄露，所有用户的口令就落入黑客的手里，此外，运维人员也可以查到数据库的
#      正确的方式是存储用户密码的摘要，比如MD5，当用户登录的时候，计算出用户输入的密码的MD5，然后和数据库存储的MD5相比较，如果一致，说明正确


#   摘要算法的反推表  应对方法； 加盐