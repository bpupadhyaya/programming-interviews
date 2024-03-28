import rx
from rx import operators as op


def main():
    source = rx.from_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
    pipe = source.pipe(
        op.filter(lambda i: i % 2 == 1),
        op.map(lambda value: "'" + str(value) + "'")
    )

    pipe.subscribe(lambda value: print('Received: ', value))


if __name__ == '__main__':
    main()
