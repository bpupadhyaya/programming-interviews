from concurrent.futures import ProcessPoolExecutor
from time import sleep


def my_worker(msg):
    for i in range(0, 10):
        print(msg, end='', flush=True)
        sleep(1)
    return i


def main():
    print('Setting up the ThreadPoolExecutor...')
    pool = ProcessPoolExecutor(3)

    # Submit the function to the pool to run
    # Concurrently, obtain a future from the pool
    print('Submitting the worker to the pool')
    future1 = pool.submit(my_worker, 'A')
    future2 = pool.submit(my_worker, 'B')
    future3 = pool.submit(my_worker, 'C')
    future4 = pool.submit(my_worker, 'D')
    print('Obtained a reference to the future 4 object ', future4)

    # Get the result from the future, wait if necessary
    print('future4.result()', future4.result())
    print('\nDone')


if __name__ == '__main__':
    main()
