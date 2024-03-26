from threading import Thread, Semaphore, currentThread
from time import sleep


def my_worker(semaphore):
    with semaphore:
        print(currentThread().getName() + ' - entered')
        print(currentThread().getName() + ' - exiting')


def main():
    print('Main thread - starting')
    semaphore = Semaphore(2)
    for i in range(0, 5):
        thread = Thread(name='T' + str(i), target=my_worker, args=[semaphore])
        thread.start()
    print('Main thread - done')


if __name__ == '__main__':
    main()
