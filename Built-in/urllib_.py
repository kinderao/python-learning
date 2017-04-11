# urllib
#   urllib提供了一系列用于操作url的功能

#    Get
#      utllib的request模块可以非常方便的抓取url内容，也就是发送一个get请求到指定的页面，然后返回http的响应
from urllib import request
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k,v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:',data.decode('utf-8'))

#   模拟request请求
from urllib import request
req = request.Request('http://www.douban.com')
req.add_header('User-Agent', 'Mozilla/6.0 ((iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))


#    Post
#     要以post发送一个请求，只需要把参数data以bytes形式传入
#     我们模拟一个微博登录，先读取登录的邮箱和口令，然后按照weibo.cn的登录页的格式以usernmae=xxx&password=xxx的编码传入
from urllib import request, parse
print('Login to weibo.cn...')
email = input('Emial:')
passwd = input('Password:')
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])
req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k,v in f.getheaders():
        print('%s: %s' % (k,v ))
    print('Data:', f.read().decode('utf-8'))


#   handler
#   如果还需要更复杂的控制，比如通过一个proxy去访问网站，我们需要利用ProxyHandler来处理，示例代码如下：
proxy_handler = request.ProxyHandler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = request.build_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
    pass
