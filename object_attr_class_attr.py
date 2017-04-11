#  实例属性和类属性
#     python是动态类型，根据类创建的实例可以绑定任意属性
#

class Student(object):
    def __init__(self, name):
        self.name = name


s = Student('bog')
s.score = 90


# 但是，如果Student本身就有这个属性，也就是这个属性属于类，而不属于实例
class Student2(object):
    name = 'Student'


s = Student2()
print(s.name)  # Student
print(Student2.name)  # Student

# 可以通过实例来访问，也可以通过类来访问
