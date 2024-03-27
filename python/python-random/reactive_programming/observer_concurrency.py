import rx
from rx.scheduler import ThreadPoolScheduler,NewThreadScheduler, ImmediateScheduler


def main():
    observable = rx.from_list([2, 3, 5, 7])

    observable.subscribe(lambda v: print('Lambda1 received: ', v), scheduler=ThreadPoolScheduler(3))
    observable.subscribe(lambda v: print('Lambda2 received: ', v), scheduler=ImmediateScheduler())
    observable.subscribe(lambda v: print('Lambda3 received: ', v), scheduler=NewThreadScheduler())

    # As the observable runs in a separate thread, we need t make sure that the main thread
    # does not terminate.
    input('Press enter to finish')


if __name__ == '__main__':
    main()
