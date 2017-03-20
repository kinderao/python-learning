# @property
#  在绑定属性的时候，如果我们把属性暴露出去，虽然写起来简单，但是没办法传递参数，导致可以把属性随便改

class Student(object):
    pass
s = Student()
s.score = 99

# 这时我们可以使用setter getter来设置和获取成绩，并且可以在setter里做相应的逻辑检查

class Student2(object):
    def get_score(self):
        return self._score
    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be an integer')
        if score < 0 or score > 100:
            raise ValueError('score must between 0 - 100')
        self._score = score

s = Student2()
s.set_score(90)
print(s.get_score())  # 90
# 这样我们就可以判断传入的属性值


#  但是上述的办法还是有些复杂，没有直接调用属性那么直接简单
#  我们可以通过使用python内置的@property装饰器来实现这个功能

class Student3(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value > 100 or value < 0:
            raise ValueError('score must between 0 -100')
        self._score = value

s = Student3()
s.score = 100
print(s.score) # 100
# 这样也可以实现不能随意修改score的值

# 还可以自定义只读属性，只定义getter，不定义setter方法就是一个只读属性
class Student4(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

# 上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来

# @property广泛应用于在类的定义中，可以让调用者写出剪短的代码，同时保证对参数进行必要的检查，减少程序出错的可能性



# 练习
class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height

s = Screen()
s.width = 3
s.height = 4
print(s.resolution)