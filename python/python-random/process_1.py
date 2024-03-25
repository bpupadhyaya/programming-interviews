from multiprocessing import Process
from time import sleep


def my_worker(msg):
    for i in range(0, 5):
        print(msg, end='', flush=True)
        sleep(1)


def main():
    print('Starting processes ')
    t1 = Process(target=my_worker, args='A')
    t2 = Process(target=my_worker, args='B')
    t3 = Process(target=my_worker, args='C')

    t1.start()
    t2.start()
    t3.start()

    print('\nDone')


if __name__ == '__main__':
    main()

