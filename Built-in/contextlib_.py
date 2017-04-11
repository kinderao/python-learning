#  contextlib
#     在python中，读写文件这样的资源要特别注意，必须在使用完成后正确的关闭他们，正确关闭文件资源的一个方法是try...finally...
# try:
#     f = open('/path/to/file', 'r')
#     f.read()
# finally:
#     if f:
#         f.close()

#  而以上的代码显得非常繁琐，Python的with语句允许我们可以方便的使用资源，而不必担心资源没有关闭
# with open('/path/to/file', 'r') as f:
#     f.read()

#  并不是只有open函数返回的fp对象才能使用with语句，实际上任何对象，只要正确的实现了上下文管理，都可以用于with语句
#   实现上下文管理是通过__enter__()和__exit__()两个方法实现的，例如:
class Query(object):
    def __init__(self, name):
        self._name = name

    def __enter__(self):
        print('begin..')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('error')
        else:
            print('end')

    def query(self):
        print('query info about %s...' % self._name)

with Query('bob') as q:
    q.query()
#
# begin..
# query info about bob...
# end


#   @contextmanager
#  编写__enter__()和__exit_()仍然很繁琐，因此python的标准库contextlib提供了更简单的写法，上面的代码可以改写如下：
from contextlib import contextmanager

class Query2(object):
    def __init__(self, name):
        self._name = name
    def query(self):
        print('query info about %s...' % self._name)

@contextmanager
def create_query(name):
    print('begin')
    q = Query2(name)
    yield q
    print('end')

with create_query('Bob') as q:
    q.query()

#  @contextmanager 这个decorator接受一个generator，用yield语句可以把with。。。as var把变量输出出去，然后，with语句就可以正常的工作了
#  很多时候我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现：
@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('</%s>' % name)

with tag('h1'):
    print('hello')
    print('world')
# <h1>
# hello
# world
# </h1>


#   代码的执行顺序是：
#      1，with语句首先执行yield之前的语句，打印出<h1>
#      2, yield调用执行with语句内部的所有语句，打印出hello和world
#      3，最后执行yield之后的语句，打印出</h1>
#   因此，@contextmanager让欧文们通过编写generator来简化上下文管理



#   @closeing
#     如果一个对象没有实现上下文，我们就不能用它用于with语句，这个时候，可以用closing()来把该对象变成上下文对象
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('http://www.python.org')) as page:
    for line in page:
        print(line)

#  closing也是一个经过@contextmanager装饰的generator，这个generator编写气力啊其实非常的简单
@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()


#  contextlib还有一些其他的decorator，便于我们编写更简洁的代码