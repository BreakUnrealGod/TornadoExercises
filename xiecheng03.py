# gevent 默认底层依赖greenlet
# greenlet

import time
from greenlet import greenlet
from gevent import monkey

import gevent

monkey.patch_all()
'''
猴子补丁主要有以下几个用处：
    在运行时替换方法、属性等
    在不修改第三方代码的情况下增加原来不支持的功能
    在运行时为内存中的对象增加patch而不是在磁盘的源代码中增加

'''


def a(n):
    for i in range(n):
        print('---->A')
        time.sleep(0.5)  # sleep()  built-in    gevent:sleep


def b(n):
    for i in range(n):
        print('---->B')
        time.sleep(0.5)


def c(n):
    for i in range(n):
        print('---->C')
        time.sleep(0.5)


def d(n):
    for i in range(n):
        print('---->D')
        time.sleep(0.5)


if __name__ == '__main__':
    g1 = gevent.spawn(a, 5)
    g2 = gevent.spawn(b, 8)
    g3 = gevent.spawn(c, 6)
    g4 = gevent.spawn(d, 6)
    # 阻塞主线程
    g1.join()
    g2.join()
    g3.join()
    g4.join()

    print('----->main')
