import rx
from rx import operators as op


def main():
    # Set up a source, integer to string conversion
    source = rx.from_list([2, 3, 5, 7]).pipe(op.map(lambda value: "'" + str(value) + "'"))

    # Subscribe a lambda function
    source.subscribe(lambda value: print('Lambda received: ', value,
                                         ' is a string', isinstance(value, str)))


if __name__ == '__main__':
    main()
