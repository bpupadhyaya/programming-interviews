from concurrent.futures import ThreadPoolExecutor, as_completed
from time import sleep
from random import randint


def is_odd(n):
    print('Checking if', n, 'is odd')
    sleep(randint(1, 5))
    return str(n) + ' ' + str(n % 2 == 1)


def main():
    print('Started')
    data = [1, 2, 3, 4, 5]
    pool = ThreadPoolExecutor(5)
    futures = []

    for v in data:
        futures.append(pool.submit(is_odd, v))

    for f in as_completed(futures):
        print(f.result())

    print('\nDone')


if __name__ == '__main__':
    main()