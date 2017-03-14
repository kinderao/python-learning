# sorted
#  python内置的sorted函数可以对list进行排序

print(sorted([2, 5, 1, 4, 20, 23, 0]))  # [0, 1, 2, 4, 5, 20, 23]

# sorted 也是一个高阶函数，他可以接收一个key函数来实现自定义个排序

print(sorted([-1, 2, 4, -5], key=abs))  # [-1, 2, 4, -5]

# sorted() 将指定的函数作用于list上的每一个元素，并根据key函数返回的结果进行排序

# lower函数作用于每一个元素上，这样就可以忽略大小写进行排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)) #['about', 'bob', 'Credit', 'Zoo']

# 反向排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))  # ['Zoo', 'Credit', 'bob', 'about']


# 学生姓名成绩排名
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]
L2 = sorted(L, key=by_name)
print(L2)  #[('Adam', 92), ('Bart', 66), ('Bob', 75), ('Lisa', 88)]


def by_score(s):
    return s[1]
L3 = sorted(L, key=by_score, reverse=True)
print(L3)   #[('Adam', 92), ('Lisa', 88), ('Bob', 75), ('Bart', 66)]

