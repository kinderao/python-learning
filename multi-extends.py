# 多重继承
#    单继承结构在类层次较多的时候，类的数量会层指数增加，为解决 这个问题，java引入了接口
#     而python中可以使用多继承来解决

class Anmial(object):
    pass
class Mammal(Anmial):
    pass
class Bird(Anmial):
    pass

class Dog(Mammal):
    pass
class Bat(Mammal):
    pass

class Parrot(Bird):
    pass
class Ostrich(Bird):
    pass

# 如果这时要加上Runnable，Flyable的功能，只需要先定义Runnable和Flyable的类
class Runnable(object):
    def run(self):
        print('runing...')
class Flyable(object):
    def fly(self):
        print('flying....')


# 现在，对于需要Runnable功能的动物，就多继承一个Runnable，例如dog
class Dog(Mammal, Runnable):
    pass

class Bat(Mammal, Flyable):
    pass

# 通过多继承，一个子类就可以同时获得父类的所有功能



#
#
#   Mixin
#       在设计类的继承关系的时候，通常，主线是通过单一继承下来的，如果混入其他的功能，如Runnable，通过多继承就可以实现了，通常这种设计成为Mixin
#          为了更好的看出继承关系，我们把Runnable和Flyable改为RunnableMixin，和FlyableMixin，类似你还可以定义肉食动物CarnivorousMixin和植实动物HerbivorseMixin
#       Mixin的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个Mixin的功能，而不是设计多层次的复杂的继承关系



