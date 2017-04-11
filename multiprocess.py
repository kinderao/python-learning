#  多进程
#     unix/linux系统提供一个fork()系统调用，它非常的特殊，普通的函数调用，返回一次，但是fork()调用一次返回两次
#    因为操作系统把当前进程（父进程）复制了一份（子进程），然后，分别在父进程，子进程里面返回

#     子进程永远返回0，父进程返回子进程的ID，这样是因为，一个父进程可以fork出很多子进程，所以，父进程要记下每一个子进程的id，而子进程只需要getppid（）就可以拿到父进程的Id
#     python中的os模块封装了常用的系统调用，其中就包括fork()，可以在python程序中轻松创建子进程

import os
print('Process (%s) start ...' % os.getpid())
# 仅在unix/linux/mac上可以执行
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s' %(os.getpid(), os.getppid()))
else:
    print('I (%s) just create a child process (%s).' % (os.getpid(), pid))

# Process (9718) start ...
# I (9718) just create a child process (9719).
# I am child process (9719) and my parent is 9718


#
#   multiprocessing
#
#   如果打算编写多进程的服务程序，unix/linux无疑是正确的选择
#   由于python是跨平台的，自然也提供了了跨平台的多进程支持，multiprocessing模块就是跨平台版本的多进程模块
#   multiprocessing模块提供一个Process类来代表一个进程对象,下面演示一下启动一个子线程并等地其结束

from multiprocessing import Process

def run_proc(name):
    print('Run child process %s (%s)...' %(name, os.getpid()))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start')
    p.start()
    p.join()
    print('Child process end.')

    # Parent process 9942.
    # Child process will start
    # Run child process test (9943)...
    # Child process end.
#  创建Process实例，用start方法启动，这样创建进程比fork()还要简单
#  join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步


#
#   Pool
#       如果要启动大量的子进程，可以使用进程池的方式批量创建子进程：
from multiprocessing import Pool
import time, random, os

def long_time_task(name):
    print('Run task %s (%s) ...'%(name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' %(name, (end - start)))

if __name__ == '__main__':
    print('Parent process %s .' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done....')
    p.close()
    p.join()
    print('All subprocesses done')

#  进程0，1，2，3是立即执行，而task 4 要等待前面某个task完成后才执行，这是因为Pool的默认大小在我的电脑上是4，因此，最多同时执行4个进程
#  p = Pool(5) 同时执行5个


#   子进程
#   很多时候子进程并不是自身，而是一个外部进程，我们创建了子进程后，还需要控制子进程的输入和输入
#   subprocess模块可以让我们可以方便的启动一个子进程，然后控制其输入和输出
import subprocess
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code', r)

    # $ nslookup www.python.org
    # Server:		192.168.199.1
    # Address:	192.168.199.1#53
    #
    # Non-authoritative answer:
    # www.python.org	canonical name = python.map.fastly.net.
    # Name:	python.map.fastly.net
    # Address: 151.101.88.223
    #
    # Exit code 0

# 如果子进程还需要输入，则可以通过communicate()方法输入：
import subprocess
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)

#  进程间的通信
# Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信，python的multiprocessing模块包装了底层的机制，提供了Queue，Pipes等多种方式来交换数据
#  我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个往Queue里读数据

from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码
def write(q):
    print('Process to write: %s ' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码
def read(q):
    print('Process to read : %s ' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__ == '__main__':
    # 父进程创建Queue
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入：
    pw.start()
    # 启动子进程pr，读取：
    pr.start()
    # 等待pw结束
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止
    pr.terminate()