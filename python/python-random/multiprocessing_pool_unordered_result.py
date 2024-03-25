from multiprocessing import Pool


def my_worker(x):
    print('In worker with: ', x)
    return x * x


def main():
    with Pool(processes=3) as pool:
        for result in pool.imap_unordered(my_worker, [0, 1, 2, 3, 4, 5, 6, 7, 8]):
            print(result)


if __name__ == '__main__':
    main()
