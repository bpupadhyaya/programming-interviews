import rx


def main():
    observable = rx.from_list([1, 2, 3, 4, 5])
    # Subscribe a lambda function
    observable.subscribe(lambda value: print('Lambda received:', value))


if __name__ == '__main__':
    main()
