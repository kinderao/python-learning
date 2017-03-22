# 单元测试
#   tdd：测试驱动开发
#   对一个模块，一个函数，一个类进行正确性效验的测试工作
#      比如对abs()函数，可以编写以下几个测试用例
#           1，输入正数，期待返回值与输入相同
#           2，输入负数，期待返回值与输入相反
#           3，输入0，期待返回0
#           4，输入非数值类型，期待抛出TypeError
#      以上的测试用例放到一个测试模块里，就是一个完整的单元测试了

#  我们来编写一个Dict类，这个类的行为和dict一直，但是可以通过属性来访问，用起来就像下面这样：
#     d = Dict(a=1, b=2)
#     d['a'] # 1
#     d.a  # 1

class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)
    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" %item)

    def __setattr__(self, key, value):
        self[key] = value


import unittest

class TestDict(unittest.TestCase):
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEquals(d.a, 1)
        self.assertEquals(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] ='value'
        self.assertEquals(d.key, 'value')

    def test_keyerror(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEquals(d['key'], 'value')

    def test_attribute(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

# 编写单元测试的时候，我们需要编写一个测试类，从unittest.TestCase继承
# 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会执行
#  对每一个类都需要编写一个test_xxx()方法，由于unittest.TestCase提供很多内置的条件判断，我们只需要判断这些方法就可以断言输出是否是我们说期望的，常用的断言就是assertEquals（）

#  另一种重要的断言就是期待输出指定类型的错误Error，比如通过d['empty']访问不存在的key时，断言就会抛出KeyError
# with self.assertRaise(KeyError):
#     value = d['empty']

# 一旦编写好单元测试，我们就可以开始单元测试，最简单的方法就是在mydict_test.py的最后加上两行代码
if __name__ == '__main__':
    unittest.main()
# 这样就可以把mydict_test.py当做正常的python脚本运行

# 另一种方法就是在命令行通过参数 -m unittest进行单元测试
# python3 -m unittest mydict_test


# setUp  tearDown
# 可以在单元测试中编写两个特殊的setUp()和tearDown()方法，这两个方法会分别在每调用一个测试方法的前后分别被执行
