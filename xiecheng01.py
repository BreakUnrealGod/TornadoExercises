import time


def a():
    for i in range(3):
        print('---->A')
        yield
        time.sleep(0.5)


def b(gen):
    for i in range(3):
        print('---->B')
        yield
        next(gen)
        time.sleep(0.5)


def c(gen):
    for i in range(3):
        print('---->C')
        next(gen)
        time.sleep(0.5)


if __name__ == '__main__':
    gen1 = a()
    gen2 = b(gen1)
    c(gen2)
