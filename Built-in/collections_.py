#  collections是python内置的一个集合模块，提供了很多有用的集合类

#  namedtuple
#    我们知道tuple是表示不可变集合，例如一个点的二维坐标可以表示成：
p = (1, 2)
#  但是这是很难看出p表示的是一个点的坐标，定义一个class而又显得麻烦，这是nametuple就可以派上用场
from collections import namedtuple
Point = namedtuple('Point', ['x','y'])
p = Point(1, 2)
print(p.x, p.y)

print(isinstance(p, Point))  # True
print(isinstance(p, tuple))  # True

#  类似的，还可以使用namedtuple表示一个圆
Circle = namedtuple('Circle', ['x', 'y', 'r'])


#   deque
#    使用list存储的时候，按索引访问元素很快，但是插入和删除就很慢，因为list是线性存储，数据量大，插入和删除的效率很低
#    deque是为了搞笑的实现插入和删除操作的双向列表，适合用于队列和栈
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)   # deque(['y', 'a', 'b', 'c', 'x'])
#   deque除了实现list的append和pop外，还支持appendleft（）和popleft（），这样就能非常高效地往头部和尾部添加或删除元素



#   defaultdict
#     使用dict时，如果引用的key不存在，就会抛出KeyError，如果希望key不存在时，返回一个默认值，就可以用defaultdict
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])  # abc
print(dd['key2'])   # N/A


#  OrderedDict
#   使用dict时，key是无序的，在对dict做迭代时，我们无法确定key的顺序
#  如果要保持key的顺序，可以用OrderedDict
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)  # {'a': 1, 'c': 3, 'b': 2}
#  key是无序的
od = OrderedDict([('a',1), ('b',2), ('c',3), ('d', 4)])
print(od) # OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
#   OrderedDict的key会按照插入的顺序排列，而不是key本身排序
#   OrderedDict可以实现一个FIFO(先进先出）的dict，当容量超出限制时，先删除最早添加的key：

class LastUpdateOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdateOrderedDict, self).__init__()
        self._capacity = capacity
    def __setitem__(self, key, value):
        containtKey = 1 if key in self else 0
        if len(self) - containtKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containtKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


#   Counter
#   Counter是一个简单的计数器，例如，统计字符出现的个数：
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

print(c)  # Counter({'r': 2, 'g': 2, 'm': 2, 'p': 1, 'o': 1, 'a': 1, 'i': 1, 'n': 1})
#  Counter实际上也是dict的一个子类，上面的结果可以看出，字符'g'，'m'，'r'各出现了两次，其他的字符出现了一次


