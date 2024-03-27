import rx


class PrimeNumberObserver:
    def on_next(self, value):
        print('Object received: ', value)

    def on_completed(self):
        print('Data stream completed')

    def on_error(self, error):
        print('Error occurred: ', error)


def prime_number_reporter(value):
    print('Function received: ', value)


def main():
    observable = rx.from_list([2, 3, 5, 7])
    # Subscribe a lambda function
    observable.subscribe(lambda value: print('Lambda received: ', value))
    # Subscribe a named function
    observable.subscribe(prime_number_reporter)
    # Subscribe an observer object
    observable.subscribe(PrimeNumberObserver())
    # Use lambdas to set up all three functions
    observable.subscribe(
        on_next=lambda value: print('Received on_next: ', value),
        on_error=lambda exp: print('Error occurred: ', exp),
        on_completed=lambda: print('Received completed notification')
    )


if __name__ == '__main__':
    main()

