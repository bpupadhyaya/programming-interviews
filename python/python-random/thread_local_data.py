from threading import Thread, local, currentThread
from random import randint


def show_value(data):
    try:
        val = data.value
    except AttributeError:
        print('-> ', currentThread().name, 'No value yet')
    else:
        print('-> ', currentThread().name, 'Value = ', val)


def my_worker(data):
    show_value(data)
    data.value = randint(1, 100)
    show_value(data)


print('-> ', currentThread().name, ' - starting ')
local_data = local()
show_value(local_data)

for i in range(3):
    t = Thread(name='W' + str(i), target=my_worker, args=[local_data])
    t.start()

show_value(local_data)
print('-> ', currentThread().name, ' - done')
