# 使用__slots__
#    正常情况下，我们定义了class，然后创建实例， 可以给实例绑定任何属性和方法，这就是动态语言的灵活性

class Student(object):
    pass

s = Student()
s.name = "kinderao"
print(s.name) # kinderao

# 还可以给实例绑定方法
def set_age(self, age):
    self.age = age

from types import MethodType

s.set_age = MethodType(set_age, s)
s.set_age(10)
print(s.age)  # 10

# 但是给实例绑定方法，对另一个实例是不起作用的

# 为了给所有实例都绑定方法，可以给class绑定方法

def set_score(self, score):
    self.score = score

Student.set_score = set_score

new_student = Student()
new_student.set_score(10)
print(new_student.score)  # 10

#  通常情况下 ，上面的set_score()方法可以定义在类中，但是动态绑定允许我们在程序运行期间动态给class加上功能，这在静态语言中是很难实现的

#
#   但是如果我们想要限制实例的属性怎么办呢？比如，只允许对Student实例添加name和age属性
#   为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制class实例能添加的属性
#
class NewStudent(object):
    __slots__ = ('name', 'age')
n = NewStudent()
# n.score = 100   # AttributeError: 'NewStudent' object has no attribute 'ge'

# 使用slots时应该注意，__slots__定义的属性仅对当前实例起作用，对继承的子类不起作用的

class GraduateStudent(NewStudent):
    pass

g = GraduateStudent()
g.score = 100
print(g.score)  # 100

#  除非在子类中也定义__slots__，这样子类实例允许定义的属性就是自身的__slots__加上父类的__slots__