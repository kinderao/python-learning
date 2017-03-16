# 面向对象
#   面向对象编程是一种程序设计思想，oop把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数
#   类  和  实例  的概念

#  类
#  在python中类的定义是通过class关键字
#
class Student(object):
    pass

# class 后面紧跟类名，类名通常是大写的单词，紧跟着是（object），表示类是从哪个类继承下来的，所有类都继承自object
bart = Student()
print(bart)  # <__main__.Student object at 0x10efc7630>
# bart变量指向的就是一个Student实例，后面的0x10efc7630是内存地址，每个object的地址都不相同
print(Student)  # <class '__main__.Student'>

# 可以给实例绑定属性，比如：
bart.name = 'bart simplson'
print(bart.name)  #bart simplson

#  由于类是模板的作用，比如我们在创建实例是希望绑定一些必要的属性，可以通过特殊的__init__方法，在创建实例的时候，把属性绑定上去
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
aPerson = Person('kinderao', 22)
print(aPerson.name) # kinderao
print(aPerson.age) # 22

# __init__方法的第一个参数是self，表示创建的实例本身，因此在__init__方法内部，就可以把各种属性绑定到self上，因为self就指向创建的实例本身
#  在使用构造方法的时候，不需要传入self，python解释器会把实例变量传进去

#  和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远为self，并且，调用的时候不用传入该参数，除此之外和类的方法和普通的函数没有什么区别
#  所以你仍然可以用默认参数，可变参数， 关键字参数和命名关键字参数

#
#
#   数据封装
#
#
class Person2(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_age(self):
        print(self.age)
aPerson2 = Person2('kinderao', 22)
aPerson2.print_age()   # 22
# 这样我们在定义Person2的时候讲name，age传入进去，而如何打印就是Person2内部定义的，外部不需要了解

#  和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然他们都是同一个类的不同实例，但是拥有的变量名称都可能不同




#
#
#      访问限制
#
#         在class内部可以用属性和方法，外部代码可以通过调用方法来操作数据（setter，getter），这样就隐藏了内部的复杂逻辑
#           但是在前面的类的定义来看，外部代码还是可以自由的修改一个实例的name，age属性
#           如果想要内部属性不被访问到，可以在属性的名称前加上两个下划线__,在python中，实例的变量名如果以__/开头，就变成了私有变量（private），自由内部可以访问，外部不能访问

class Person3(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def get_name(self):
        return self.__name

aPerson3 = Person3('kinderao', 233)
print(aPerson3.get_name())  # kinderao
#  如果访问私有变量就会报错
# print(aPerson3.__name)   # AttributeError: 'Person3' object has no attribute '__name'

# 添加setter
class Person4(object):
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name

aPerson4 = Person4()
# print(aPerson4.get_name())  AttributeError: 'Person4' object has no attribute '_Person4__name'
aPerson4.set_name('john')
print(aPerson4.get_name())  # john


#
#  再谈一下变量的权限  __name__,   _xxx, __xxx, xxx
#       在python中以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以访问的不是private变量
#       而 _name 这样的属性，这样的实例变量在外部是可以访问的，但是按照约定俗成的规定，当你看到这样的变量时，意思说"虽然我可以被访问，但是你应该把我视为私有变量，不要随意访问
#       双下划线开头的变量，其实也不是一定不能从外部访问，因为__name是因为python解释器会把__name 变量改变成_Student__name，所以仍然可以通过_Student__name 来访问__name属性（不建议，因为不同的python解释器会把__name改为不同的属性名）
#
#
#   附上网上看到的一段很污的解释：在一个实例里，
#       __girl表示“我是贞女，你不能上我”
#       _girl表示“你虽然可以上我，但你应该把我看做贞女”
#       girl表示“我是荡妇，谁都可以上我”
#       但是python仍然可以用_实例名__girl强上贞女



