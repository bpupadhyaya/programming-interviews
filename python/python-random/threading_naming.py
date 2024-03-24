import threading
from threading import Thread
from time import sleep


def my_worker(msg):
    for i in range(0, 10):
        print(msg, end='', flush=True)
        sleep(1)


t1 = Thread(name='my_worker', target=my_worker, args='A')
t2 = Thread(target=my_worker, args='B')
d = Thread(daemon=True, name='daemon', target=my_worker, args='C')

print('Starting threads...')
t1.start()
t2.start()
d.start()

print('\n')
for t in threading.enumerate():
    print('--->', t.name, t)



