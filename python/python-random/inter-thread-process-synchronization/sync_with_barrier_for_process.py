from multiprocessing import Barrier, Process
from time import sleep
from random import randint


def print_it_1(msg, barrier):
    print('print_it for: ', msg)
    for i in range(0, 10):
        print(msg, end='', flush=True)
        sleep(1)
    sleep(randint(1, 6))
    print('Wait for barrier with: ', msg)
    barrier.wait()
    print('Returning from print_it for: ', msg)


def callback():
    print('Callback executing')


def main():
    print('Main - starting')

    b = Barrier(3, callback)
    t1 = Process(target=print_it_1, args=('A', b))
    t2 = Process(target=print_it_1, args=('B', b))
    t3 = Process(target=print_it_1, args=('C', b))
    t1.start()
    t2.start()
    t3.start()

    print('Main - done')


if __name__ == '__main__':
    main()
