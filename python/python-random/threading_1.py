from threading import Thread
from time import sleep


def my_worker():
    for i in range(0, 10):
        print('.', end='', flush=True)
        sleep(1)


print('starting thread...')
t1 = Thread(target=my_worker)
t1.start()
t1.join()
print('\nDone')

print(t1.getName())
print(t1.ident)



