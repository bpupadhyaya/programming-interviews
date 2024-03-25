from multiprocessing import Pool
from time import sleep


def collect_results(result):
    print('In collect_results: ', result)


def my_worker(x):
    print('In worker with: ', x)
    return x * x


def main():
    with Pool(processes=2) as pool:
        # get based, blocking
        res = pool.apply_async(my_worker, [5])
        print('Result from async: ', res.get(timeout=1))

    with Pool(processes=2) as pool:
        # callback based, non-blocking
        pool.apply_async(my_worker, args=[3], callback=collect_results)


if __name__ == '__main__':
    main()
