import rx


class PrimeNumberObserver:
    def on_next(self, value):
        print('Object received: ', value)

    def on_completed(self):
        print('Data stream completed')

    def on_error(self, error):
        print('Error occurred: ', error)


def main():
    observable = rx.from_list([1, 2, 3, 4, 5])
    # Pass observer object
    observable.subscribe(PrimeNumberObserver())


if __name__ == '__main__':
    main()
