import rx


def number_reporter(value):
    print('Function received: ', value)


def main():
    observable = rx.from_list([1, 2, 3, 4, 5])
    # Subscribe a named function
    observable.subscribe(number_reporter)


if __name__ == '__main__':
    main()
