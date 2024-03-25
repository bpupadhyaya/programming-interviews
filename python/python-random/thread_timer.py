from threading import Timer


def my_func():
    print('say something')


print('Starting timer thread')
t = Timer(5, my_func)
t.start()

print('\nDone')