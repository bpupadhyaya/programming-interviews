import rx
from rx import operators as op


def main():
    source = rx.from_list([1, 2, 3, 4, 5, 6, 7, 8, 9]).pipe(
        op.filter(lambda value: value % 2 == 1)
    )

    source.subscribe(lambda value: print('Lambda received: ', value))


if __name__ == '__main__':
    main()