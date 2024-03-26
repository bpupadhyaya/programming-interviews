from multiprocessing import Process, Queue
from time import sleep


def my_worker(queue):
    print('Worker - going to sleep')
    sleep(2)
    print('Worker - woken up and putting data on queue')
    queue.put('test message')


def main():
    print('Main - starting')
    queue = Queue()
    p = Process(target=my_worker, args=[queue])
    print('Main - waiting for data')
    p.start()
    print('in main: ', queue.get())
    print('Main - done')


if __name__ == '__main__':
    main()
