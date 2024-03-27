import rx
from rx.subject import Subject
from datetime import datetime

class TimeStampSubject(Subject):
    def on_next(self, value):
        print('Subject received: ', value)
        super().on_next((value, datetime.now()))

    def on_completed(self):
        print('Data stream completed')
        super().on_completed()

    def on_error(self, error):
        print('In subject - error occurred', error)
        super.on_error(error)


def prime_number_reporter(value):
    print('Function received', value)


def main():
    print('Main - setting up')
    observable_source = rx.from_list([2, 3, 5, 7])
    subject = TimeStampSubject()

    # Set up multiple subscribers / observers for the subject
    subject.subscribe(prime_number_reporter)
    subject.subscribe(lambda value: print('Lambda received: ', value))
    subject.subscribe(
       on_next=lambda value: print('Received on_next: ', value),
       on_error=lambda exp: print('Error occurred: ', exp),
       on_completed=lambda: print('Received completed notification')
    )

    # Subscribe the Subject to the Observable source
    observable_source.subscribe(subject)


if __name__ == '__main__':
    main()



