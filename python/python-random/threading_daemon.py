from threading import Thread
from time import sleep


def my_worker(msg):
    for i in range(0, 10):
        print(msg, end='', flush=True)
        sleep(1)


print('Starting thread...')
d = Thread(daemon=True, target=my_worker, args='C')
d.start()
sleep(5)
print('\nDone')