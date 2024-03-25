from multiprocessing import Pool


def my_worker(x):
    print('In worker with value: ', x)
    return x * x


def my_worker_2(x):
    print('In worker with value: ', x)
    return x * x * x


def main():
    with Pool(processes=4) as pool:
        print(pool.map(my_worker, [0, 1, 2, 3, 4, 5, 6, 7]))
        print(pool.map(my_worker_2, [0, 1, 2, 3, 4, 5, 6, 7]))


if __name__ == '__main__':
    main()
