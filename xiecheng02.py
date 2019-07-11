# greenlet

import time
from greenlet import greenlet


def a():
    for i in range(3):
        print('---->A')
        g2.switch()
        time.sleep(0.5)


def b():
    for i in range(3):
        print('---->B')
        g3.switch()
        time.sleep(0.5)


def c():
    for i in range(3):
        print('---->C')
        g1.switch()
        time.sleep(0.5)


if __name__ == '__main__':
    # a()
    # b()
    # c()
    g1 = greenlet(a)
    g2 = greenlet(b)
    g3 = greenlet(c)

    g1.switch()