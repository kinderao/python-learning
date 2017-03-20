#  定制类

#    看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在python中是有特殊用途的
#    __slots__用于限制类绑定的属性，__len__()方法我们也知道是为了能让class作用于len(）函数
#    除此之外，python中的class中还有许多这样有特殊用途的函数，可以帮助我们定制类

#
#    __str__
#       定义输出的字符串
#
class Student(object):
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.__name

print(Student('kinderao'))  # Student object (name: kinderao)
# __str__()  返回用户看到的字符串
# __repr__()  返回程序开发者看到的字符串，是为调试服务的


#
#    __iter__
#         如果一个类想要被for ... in 循环，类似list和tuple那样，就必须要实现一个__iter__(）方法，该方法返回一个迭代对象，
#         然后Python就的for循环就会不断的调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误
#
class Fib(object):
    def __init__(self):
        self.a , self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000000:
            raise StopIteration
        return self.a

for n in Fib():
    print(n)


#
#       __getitem__
#            Fib实例虽然能作用于for循环，但是和list看起来有点像，但是，把它当成list来使用还是不行，比如，取第五个元素：
#              如果想要像list那样可以按照下标取出元素，需要实现__getitem__()方法
#
class Fib2(object):
    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a, b = b, a + b
        return a
# 现在就可以访问下标数列的任意一项了
f = Fib2()
print(f[5])  # 8
print(f[10])  # 89


# 但是list有一个可以切片方法
class Fib3(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            l = []
            for x in range(stop):
                if x >= start:
                    l.append(a)
                a, b = b, a + b
            return l

f = Fib3()
print(f[5:10])

# 但是没有对step参数进行处理, 也没有对负数做处理，所以要正确实现一个__getitem__()还有很多工作需要做
# 此外，如果把对象看成dict，__getitem()的参数也可能是一个可以作key的object，例如str
# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值，最后还有一个__delitem__()方法，用于删除某个元素
# 总之，通过上面的方法，我们可以自定义的类变现的和python自带的list，tuple， dict没什么区别，这完全归功于动态类型语言的'鸭子类型'， 不需要强制继承某个接口


#
#
#   __getattr__
#         正常情况下，调用类的方法或者属性时，不存在时就会报错，而如果我们写一个__getattr__()方法，动态返回一个属性，修改如下：
#
class Student2(object):
    def __init__(self, name):
        self._name = name

    def __getattr__(self, item):
        if item == 'age':
            return 22

s = Student2('kinderao')
print(s.age)  # 22
#  也可以返回函数  return lambda： 25
#  但是上述情况只是发生在没有找到该属性的情况下，如果实例本身有这个属性，就不会调用__getattr__()方法

# 通过__getattr__()方法可以把一个类的所有属性和方法都动态化处理，不需要任何特殊手段
class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().status.users.timeline.list)  # /status/users/timeline/list
# 通过getattr轻松实现链式调用，简洁明了，无论api怎么变，sdk都可以根据url实现完全动态的调用，而且部署api的增加而改变

# 而如果restful api中带有参数如  get /user/:user/repos
class Chain2(object):
    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, path):
        return
# print(Chain().users('kinderao').repos)


#
#
#   __call__
#         一个对象可以有自己属性和方法，当我们调用实例方法时我们用instance.method()来调用
#         也可以在类中定义__call__()方法，就可以直接对实例进行调用
#
class Student2(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print('my name is %s' % self.name)

s = Student2('kinderao')
s()   # my name is kinderao
# 还可以在call中定义参数，对视力进行调用和对函数进行调用一样，可以把对象看成函数，也可以把函数看成对象

# 那怎么判断一个变量是函数还是对象，其实我们应该判断一个对象是否可以被调用，能被调用的对象就是一个Callable对象，比如函数和我们上面定义的__call__()的类实例
print(callable(Student('kinderao')))  # False
print(callable(Student2('kinderao')))  # True




