from threading import Thread


def my_worker():
    print('hi')


t1 = Thread(target=my_worker)
t1.start()
