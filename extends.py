#  继承和多态
#     定义了一个类后，可以直接从这个类继承，新的这个类称为子类，被继承的称为父类

class Animal(object):
    def run(self):
        print('Animal is running')

class Dog(Animal):
    pass

class Cat(Animal):
    pass

aDog = Dog()
aDog.run()  # Animal is running

class Dog2(Animal):
    def run(self):
        print('Dog is runing')

aDog2 = Dog2()
aDog2.run()  # Dog is runing
aAnimal = Animal()
aAnimal.run()  # Animal is runing

#  当子类和父类方法一样时，子类方法会覆盖父类方法，


#
#   多态
#
#  定义一个class其实就是定义一种数据结构，我们定义的数据类型和Python自带的数据类型其实都一样
a = list()  # list类型
b = dict()  # dict类型
c = Dog()   #  Dog类型

# 我们可以通过isinstance来判断某个变量是否属于某个类型

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Dog2())
#  在这里我们定义了Anmial作为参数，新增一个Animal的子类时，不必对run_twice()做任何修改，任何依赖Animal作为参数的函数或方法都能运行，原因就在于多态
#  多态的好处就在于，当我们传入Dog, Cat时， 我们只需要接收Animal类型就可以，因为Dog，Cat都是Animal类型，并且会自动调用实际的run() 方法
#       不管原来的代码是怎么调用的，只要保证run（）方法正确，就能正确运行，这就是著名的开闭原则
#            对扩展开放：  允许修改Animal子类
#            对修改封闭：  不需要修改Animal类型的run_twice()等函数
#
#
#   静态语言vs动态语言；
#          对于静态语言（java）来说，如果需要传入Animal，则传入的必须是Animal的子类，否则将无法调用run方法
#          但是对于python这样的动态语言来说，不一定需要传入Animal类型，只要保证传入的对象有一个run(）方法就行
#                  这也就是动态语言的鸭子类型，并没有严格的继承体系，一个对象只要看起来像鸭子，那他就是可以看做鸭子
#


#
#   获取对象信息
#       当我们拿到一个对象的引用事，如何知道这个对象是什么类型的，有哪些方法
#   使用type()
print(type(123))  #<class 'int'>
print(type('abc'))  # <class 'str'>

# 如果一个变量指向函数或者类，也可以用type()来判断
print(type(abs))  # <class 'builtin_function_or_method'>

# >>> type(123)==type(456)
# True
# >>> type(123)==int
# True
# >>> type('abc')==type('123')
# True
# >>> type('abc')==str
# True
# >>> type('abc')==type(123)
# False

# 判断基本类型可以直接用int，str判断，但是如果要判断一个对象是否是函数怎么办？ 可以使用types模块中定义的常量：
import types
def fn():
    pass

print(type(fn) == types.FunctionType)  # True
print(type(abs) == types.BuiltinFunctionType)  # True
print(type(lambda x: x) == types.LambdaType)  # True
print(type(x for x in range(2)) == types.GeneratorType)  # True


# isinstance() 也可以判断class的类型
print(isinstance(aDog, Animal)) # True

# isinstance() 还可以判断一个变量是否是某些类型中的一种，比如下面的代码
print(isinstance([1, 2, 3], (list, tuple)))  # True
print(isinstance([1, 2, 3], (str, tuple)))  # False




