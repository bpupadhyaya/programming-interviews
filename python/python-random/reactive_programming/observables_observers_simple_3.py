import rx


def number_reporter(value):
    print('Function received: ', value)


def main():
    observable = rx.from_list([1, 2, 3, 4, 5])
    # Check whether data is supplied by observable
    observable.subscribe(
                         on_next=lambda value: print('Received on_next', value),
                         on_error=lambda exp: print('Error occurred', exp),
                         on_completed=lambda: print('Received completed notification')
    )


if __name__ == '__main__':
    main()
