from concurrent.futures import ThreadPoolExecutor
from time import sleep


def my_worker(msg):
    for i in range(0, 10):
        print('msg', end='', flush=True)
        sleep(1)
    return i


def main():
    print('Setting up the ThreadPoolExecutor...')
    pool = ThreadPoolExecutor(1)

    # Submit the function to the pool to run
    # Concurrently, obtain a future from the pool
    print('Submitting the worker to the pool')
    future = pool.submit(my_worker, 'A')
    print('Obtained a reference to the future object ', future)

    # Get the result from the future, wait if necessary
    print('future.result()', future.result())
    print('\nDone')


if __name__ == '__main__':
    main()
