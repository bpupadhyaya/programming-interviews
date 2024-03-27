import rx
from rx import operators as op


def main():
    source = rx.from_list([2, 4, 6, 8]).pipe(op.sum())

    source.subscribe(lambda v: print(v))


if __name__ == '__main__':
    main()
