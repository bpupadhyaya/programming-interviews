from concurrent.futures import ThreadPoolExecutor
from time import sleep
from random import randint


def is_odd(n):
    print('Checking if', n, 'is odd')
    sleep(randint(1, 5))
    return str(n) + ' ' + str(n % 2 == 1)


def print_future_result(future):
    print('In callback future result: ', future.result())


def main():
    print('Starting...')
    data = [1, 2, 3, 4, 5]
    pool = ThreadPoolExecutor(5)
    for v in data:
        future = pool.submit(is_odd, v)
        future.add_done_callback(print_future_result)

    print('\nDone')


if __name__ == '__main__':
    main()
