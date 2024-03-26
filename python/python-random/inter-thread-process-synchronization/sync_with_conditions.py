from threading import Thread, Condition, currentThread
from time import sleep
from random import randint


class DataResource:
    def __init__(self):
        print('DataResource - initializing the empty data')
        self.data = None
        print('DataResource - setting up th condition object')
        self.condition = Condition()

    def consumer(self):
        # Wait for the condition and use hte resource
        print('DataResource - starting consumer method in', currentThread().name)
        with self.condition:
            self.condition.wait()
            print('DataResource - resource is available to', currentThread().name)
            print('DataResource - data read in', currentThread().name, ':', self.data)

    def producer(self):
        # Setup th resource to be used by the consumer
        print('DataResource - starting producer method')
        with self.condition:
            print('DataResource - producer setting data')
            self.data = randint(1, 100)
            print('DataResource - producer notifying all waiting threads')
            self.condition.notify_all()


def main():
    print('Main - starting')
    print('Main - creating the DataResource object')
    resource = DataResource()

    print('Main - create the consumer threads')
    c1 = Thread(target=resource.consumer)
    c1.name = 'Consumer1'
    c2 = Thread(target=resource.consumer)
    c2.name = 'Consumer2'
    print('Main - create the producer thread')
    p = Thread(target=resource.producer)

    print('Main - starting consumer threads')
    c1.start()
    c2.start()
    sleep(1)

    print('Main - starting producer thread')
    p.start()

    print('\n Main - done')


if __name__ == '__main__':
    main()
