# 装饰器
#   由于函数也是一个对象，而且函对象可以赋值给变量，所以通过变量也能调用函数

def now():
    print('2017-3-14')
f = now
f()   # 2017-3-14

# 函数对象有一个_name_属性，可以拿到函数的名字
print(now.__name__)  # now
print(f.__name__)  # now

# 假设我们现在要增强now()函数的功能，比如在函数调用前后自动打印日志，但是又不希望改变now函数的定义，
# 这种在代码运行期间动态增加功能的方式，称之为"装饰器"（Decorator）

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 因为上面的函数是一个Decorator，可以接收一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处：

@log
def prin_now():
    print('2017-3-14')

prin_now()   # call prin_now():
             # 2017-3-14

# 把@log放到now函数的定义处，相当于执行了语句：
# now = log(now)
# 由于log（）是一个decorator，返回一个函数，所以原来的now仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper函数

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2017-3-14')

now()   # execute now():
        # 2017-3-14

# 和两层嵌套的decorator相比，3层嵌套的想过是这样的
#  now = log('execute')(now)
#  首先执行log（'execute'），返回的是decorator函数，再调用返回到的函数，参数是now函数，返回值最终是wrapper函数

print(now.__name__)  # wrapper
#  now函数的__name__属性已经变成了'wrapper'
#  是因为返回的那个wrapper（）函数名字就是'wrapper'，所以需要把原始函数的__name__等属性复制到wrapper函数中，否则，有些依赖函数签名的代码执行就会出错
#  python内置的functools.wraps就是干这个事的，所以一个完整的wrapper写法如下

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2017-2-14')
now()  #  call now():
       # 2017-2-14

print(now.__name__)  # now


