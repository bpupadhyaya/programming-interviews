from multiprocessing import Process, Event
from time import sleep


def wait_for_event(event):
    print('wait_for_event - entered and waiting')
    event_is_set = event.wait()
    print('wait_for_event - event is set', event_is_set)


def set_event(event):
    print('set_event - entered and about to sleep')
    sleep(5)
    print('set_event - waking and setting event')
    event.set()
    print('set_event - event set')


def main():
    print('Main - starting')
    event = Event()
    # Start a process to wait for the event notification
    p1 = Process(target=wait_for_event, args=[event])
    p1.start()

    # Set up a process to set the event
    p2 = Process(target=set_event, args=[event])
    p2.start()

    # Wait for the first process to complete
    p1.join()

    print('\nDone')


if __name__ == '__main__':
    main()
