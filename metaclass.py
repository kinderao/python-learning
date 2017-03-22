#  元类

# 动态语言和静态语言最大的区别，就是函数和类的定义，不是编译时定义，而是运行时动态创建的
class Hello(object):
    def hello(self, name='world'):
        print('hello, %s' % name)

#
h = Hello()
print(type(Hello))  # <class 'type'>
print(type(h))  # <class '__main__.Hello'>

# python解释器载入hello模块时，就会依次执行该模块的所有语句，执行结果就是动态创建一个Hello的class对象

# type函数可以看做一个类型或变量的类型，Hello是一个class， 他的类型就是type， 而h是一个实例，它的类型就是class Hello
# 而我们说的class的定义是运行时动态创建的，而创建class的方法就是使用type()函数

# type函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type(）函数创建出Hello类，而无需通过class Hello(object)的定义

def fn(self, name='world'):
    print('Hello %s' %name)

Hello2 = type('Hello', (object,), dict(hello=fn))  # 创建class
h2 = Hello2()
h2.hello('ddd')  # Hello ddd

print(type(Hello2))  # <class 'type'>
print(type(h2))   # <class '__main__.Hello'>
#
#   要创建一个class对象，type()函数需要依次传入三个参数：
#         1， class的名称
#         2， 继承的父类的集合，注意Python支持多继承，如果只有一个父类，别忘了tuple的单元素写法
#         3， class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上
#
#  通过type创建的类和直接写class是完全一样的，因为python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建class
#  正常情况下我们使用class来定义类，type()函数也允许我们动态创建出来，也就是说，动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同，
#     要在静态语言运行期间创建类，必须构造源代码字符串在调用编译器，或者借助工具生成字节码，本质上都是动态编译，会非常复杂



#
#
#       metaclass
#             除了使用type(）动态创建类以外，要控制类的创建行为，还可以使用metaclass
#         metaclass，直译为元类，简单的解释就是：我们定义了类以后，可以根据这个类创建出实例，所以先定义类，然后创建实例
#             但是我们如果想要创建出类，就必须要根据metaclass创建出类，所以：先定义metaclass，然后创建类
#             连接起来就是，先定义metaclass，然后创建类，最后创建实例
#
#             按照默认习惯，metaclass的类型总是以Metaclass结尾，以便清楚地表示这是一个metaclass:
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

# 有了ListMetaclass后，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass：
class MyList(list, metaclass=ListMetaclass):
    pass
# 当我们传入metaclass的时候，魔术就生效了，它指示python解释器在创建MyList的时候，要通过ListMetaclass.__new__()来创建，
# 再次我们可以修改类的定义，比如，加上新的方法，然后返回修改后的定义
# __new__()方法接收到的参数依次是：
#       1， 当前准备创建的类的对象
#       2， 类的名字
#       3， 类继承的父类集合
#       4， 类的方法集合
l = MyList()
l.add(1)
print(l)  # [1]

#  动态修改有什么意义，直接在MyList中写上add()方法不是更简单吗  但是在一些情况需要通过metaclass修改类定义的，ORM就是一个典型的例子

# eg：
#     class User(Model):
#         id = IntegerField('id')
#         name = StringField('username')
#         email = StringField('email')
#         passwor = StringField('password')
#
#     #  创建一个实例：
#     u = User(id=1234, name='kinderao', email='test@qq.com', password='my-pwd')
#     #  保存到数据库中
#     u.save()

# 其中父类Model和StringField， IntegerField是由orm提供的，剩下的魔方方法比如save()全部由metaclass来自动完成，虽然metaclass的编写特别复杂，但是orm的使用起来却很方便


