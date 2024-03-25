from multiprocessing import Process
from multiprocessing import set_start_method
from time import sleep
import os


def my_worker(msg):
    print('Module name: ', __name__)
    print('Parent process: ', os.getppid())
    print('Process id: ', os.getpid())
    for i in range(0, 10):
        print(msg, end='', flush=True)
        sleep(1)


def main():
    print('Starting multiprocessing')
    print('Root application process id: ', os.getpid())
    set_start_method('spawn')
    t = Process(target=my_worker, args='A')
    t.start()

    print('\nDone')


if __name__ == '__main__':
    main()

