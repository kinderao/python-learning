# filter 过滤
#      和map，reduce一样，接收一个函数，一个序列，
#      不同的是，把函数作用于每一个元素，然后根据返回值True和False决定保留还是丢弃该元素


#  删掉偶数
def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1, 2, 3, 4, 5])))  # [1, 3, 5]

#  删除空字符
def not_empty(x):
    return x and x.strip()

print(list(filter(not_empty, ['ha', '', 'B', None, 'C', '   '])))  # ['ha', 'B', 'C']


# filter 返回的是一个Iterator，所以要强迫使用filter（）来计算结果，需要用list（）函数获得所有结果并返回list

# 素数数列
def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

for n in primes():
    if n < 1000:
        print(n)
    else:
        break


# 过滤掉 非 回数(1221,2332)
def is_palindrome(n):
    n = str(n)
    result = True
    for x in range((len(n) + 1)// 2):
        result = n[x] == n[len(n) - x - 1] and result
    return result

aList = list(filter(is_palindrome, [1232, 1221, 12321, 12333]))
print(aList)


