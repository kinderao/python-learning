# dict 全称dictionary，其他语言中也称为map
d = {"tom": 15, "bob": 12, "sony": 10}
print(d['tom'])

# key-value的存储方式  放进去的时候就要根据key计算出value的存放位置，取得时候才能直接取到
# 通过key放入
d['tom'] = 111
print(d['tom'])

# 可以通过追加直接放入数据
d['jimmy'] = 'test'
print(d['jimmy'])
print(d)  #{'tom': 111, 'bob': 12, 'sony': 10, 'jimmy': 'test'}

# 一个key只能对应一个value，多次放入value，会被覆盖掉
d['tom'] = 23
print(d['tom']) #23

# 如果key不存在就会报错
# 我们可以通过 in 来判断key是否存在
if 'tom' in d:
    print(d['tom'])
# 也可以通过dict提供的get方法，如果key不存在的话，可以返回none，也可以返回自己指定的默认值
a = d.get('tt')
print(a) #None
b = d.get('tt', 'I am None')
print(b)

# dict内部存放顺序和key的放入时的顺序没有关系

# dict和list比较： dict： 查找插入的速度快，不会随着key的增加而变慢
#                       需要占用大量的内存，内存浪费多
#                 list: 查找和插入的时间随着元素的增加而增加
#                       占用空间小，浪费内存少

# dict可以用在需要使用高速查找的地方，
#  !!! dict中的key必须是不可变对象,因为通过哈希算法Hash来保存保存和取出时的位置一样
# 而在Python中，字符串，整数都是不可变的，所以可以放心使用做key，而list是可变的，就不能使用作为key
aList = [1, 2, 3]
# person = {aList, 'ddd'}   TypeError: unhashable type: 'list'
