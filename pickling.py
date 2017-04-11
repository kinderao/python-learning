# 序列化

# 在程序中我们可以生成这样的变量，存在于内存中
d = dict(name='bog', age=20, score=88)
# 但是如果要持久化就需要就将其存到硬盘上
#     把变量从内存中变成可以存储或传输的过程称为序列化，在python中佳作pickling，在其他语言中也叫做serializetion等等


import pickle

print(pickle.dumps(d))  # b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x03\x00\x00\x00bogq\x02X\x03\x00\x00\x00ageq\x03K\x14X\x05\x00\x00\x00scoreq\x04KXu.'
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

# pickle.dumps()方法可以把任意对象虚拟化为一个bytes，然后用pickle.loads()方法来进行反序列化出对象，也可以直接用pickle.load()方法从一个file-like对象中直接反序列化
f = open('dump.txt', 'rb')
another_d = pickle.load(f)
f.close()

print(another_d)  # {'name': 'bog', 'age': 20, 'score': 88}


# pickle的问题和其他的编程语言一样，只适用于python，而且不同版本还彼此不兼容，因此只能用于保存不重要的数据


#
#
#  Json
#
#     假如要在不同的语言之间传递对象就需要用到json，可以被任何语言读取，也方便网络存储和传输，json不仅是标准格式，而且并xml更快
#
#     json类型            python类型
#       {}                  dict
#       []                  list
#     "String"              str
#       123.23              int或float
#     true/false            True/False
#       null                None
#   python内置json模块提供了非常完善的python对象到json格式的转换

import json

print(json.dumps(d))    # {"name": "bog", "age": 20, "score": 88}
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))   # {'age': 20, 'score': 88, 'name': 'Bob'}


#   Json 进阶
#  python的dict对象可以直接序列化为json的{}，不过很多时候，我们更喜欢用class来表示对象，比如定义student类，然后序列化：
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('bob', 20, 90)
# print(json.dumps(s))  # typeError,因为student对象不是一个可序列化对象

def student2dict(std):
    return {
        'name':std.name,
        'age': std.age,
        'score': std.score
    }

print(json.dumps(s, default=student2dict))  # {"name": "bob", "age": 20, "score": 90}

#  不过这样的话，下一次我们碰到一个Teacher类，也要为Teacher写一个转化方法，我们可以把任意class的实例变成dict
print(json.dumps(s, default=lambda obj: obj.__dict__))  # {"name": "bob", "age": 20, "score": 90}
#  因为class的实例通常都有一个__dict__属性，它就是一个dict，用来存储实例变量，也有不少例外，比如定义了__slots__的class

#  同样的道理，如果要把json反序列化为一个Student对象实例，loads()方法首先转化出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例
def dict2studnet(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2studnet))  # json_str = '{"age": 20, "score": 88, "name": "Bob"}'