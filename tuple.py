# tuple和list的区别： tuple为有序列表，称为元组
# 一旦初始化了  顺序就不能变了  不能append，insert
# 可以通过索引获取元素  classmate[1], classmate[2]
# 因为元素不可变，所以更安全，如果可能尽量使用tuple代替list

classmate = ('tom', 'bill', 'keven')

# 当只有一个元素的时候 代表的不是tuple， 而是指代数学运算中的括号
# t =（1）
# 所以只有一个元素的tuple，要在末尾添加一个逗号
t = (1,)

# tuple中可以存放list
aList = [1, 2, 3]
anotherList = [2, 3, 4]
aTuple = (aList, anotherList)
print(aTuple)