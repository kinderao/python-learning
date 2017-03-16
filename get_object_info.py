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



#  如果要获得一个对象的所有方法和属性，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：

print(dir("abc"))  # ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '_
# _getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '_
# _ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
# 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal',
# 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition',
#  'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

# 类似__xx__的属性和方法在python中都是有特殊用途的，比如__len__方法返回长度，在Python中，如果你用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法

print(len('abc'))  # 3

print('abc'.__len__()) # 3

#  如果我们自己写的类想要用len(myObj)的话，就要自己写一个__len__()方法
class MyObj(object):
    def __len__(self):
        return 100
my = MyObj()
print(len(my))  # 100

#  把属性列出来是不够的，我们还可以配合getattr(), setattr(), hasattr()，我们可以直接操作一个对象的状态
class Myobj(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

a = Myobj()
print(hasattr(a, 'x'))  # True
print(getattr(a, 'x'))  # 9
setattr(a, 'x', 10)
print(a.x)   # 10

#  如果尝试获取不存在的属性，就会抛出AttributeError的错误
#  也可以传入一个default参数，如果属性不存在，就返回默认值

print(getattr(a, 'y', 100))  # 100

print(hasattr(a, 'power')) # True
fn = getattr(a, "power")
print(fn())  # 10 * 10  = 100
