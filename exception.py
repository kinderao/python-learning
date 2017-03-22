# 异常

#  错误处理： 错误代码（不便，不知道错误原因，。。）
#            try...except...finally...机制

try:
    print('try')
    r = 10 / 0
    print('result: %s' %r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally')
print('end')
# result:
    # try
    # except: division by zero
    # finally
    # end

#  发生错误后，后续代码不会执行，会被阻塞
#  使用except可以捕获到错误，执行except中的代码
#  不同类型的错误，多个except来捕获不同类型的错误
#  但是捕获的时候会将该类和它的所有子类错误一起"一网打尽"
#  调用堆栈：如果没被捕获，就会一直往上抛，直到被解释器捕获，然后打印错误，退出
#


#  记录错误
import logging
def foo(s):
    return 10/int(s)

def bar(s):
    return foo(s) * 2
def main():
    try:
        bar(0)
    except Exception as e:
        logging.exception(e)

main()
print('end')
#  使用logger记录错误


#  抛出错误 raise
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10/n

foo('0')
#
