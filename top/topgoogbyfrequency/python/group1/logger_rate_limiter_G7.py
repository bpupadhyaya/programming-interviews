"""
Design a logger system that receives a stream of messages along with their timestamps. Each unique message should
only be printed at most every 10 seconds (i.e. a message printed at timestamp t will prevent other identical
messages from being printed until timestamp t + 10).
All messages will come in chronological order. Several messages may arrive at the same timestamp.
Implement the Logger class:
Logger() Initializes the logger object.
bool shouldPrintMessage(int timestamp, string message) Returns true if the message should be printed in the given
 timestamp, otherwise returns false.

Example 1:
Input
["Logger", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage",
"shouldPrintMessage", "shouldPrintMessage"]
[[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
Output
[null, true, true, false, false, false, true]

Explanation
Logger logger = new Logger();
logger.shouldPrintMessage(1, "foo");  // return true, next allowed timestamp for "foo" is 1 + 10 = 11
logger.shouldPrintMessage(2, "bar");  // return true, next allowed timestamp for "bar" is 2 + 10 = 12
logger.shouldPrintMessage(3, "foo");  // 3 < 11, return false
logger.shouldPrintMessage(8, "bar");  // 8 < 12, return false
logger.shouldPrintMessage(10, "foo"); // 10 < 11, return false
logger.shouldPrintMessage(11, "foo"); // 11 >= 11, return true, next allowed timestamp for "foo" is 11 + 10 = 21

Constraints:
0 <= timestamp <= 10^9
Every timestamp will be passed in non-decreasing order (chronological order).
1 <= message.length <= 30
At most 10^4 calls will be made to shouldPrintMessage.
"""


class Logger:
    # Hashmap, simple
    def __init__(self):
        self.history = {}  # stores past messages in the form {message: last print timestamp}

    def should_print_message(self, timestamp: int, message: str) -> bool:
        if message in self.history and timestamp - self.history[message] < 10:  # O(1)
            return False
        else:
            self.history[message] = timestamp  # O(1)
            return True


class Logger1:
    # Hashmap, modified / cleaned up
    def __init__(self):
        self.history = {}  # stores past messages in the form {message: last print timestamp}
        self.last_timestamp = 0

    def should_print_message(self, timestamp: int, message: str) -> bool:
        if timestamp != self.last_timestamp:  # every time we get a new timestamp ...
            for m, t in list(self.history.items()):  # ... purge the old messages, O(m10)
                if t <= timestamp - 10:
                    del self.history[m]
            self.last_timestamp = timestamp
        if message in self.history and timestamp - self.history[message] < 10:  # O(1)
            return False
        else:
            self.history[message] = timestamp  # O(1)
            return True


class Logger2:
    # Set and queue
    def __init__(self):
        self.history = set()  # set of past messages younger than 10 timestamps
        self.queue = list()  # ordered list of messages younger than 10 timestamp

    def should_print_message(self, timestamp: int, message: str) -> bool:
        while self.queue and self.queue[0][0] <= timestamp - 10:
            self.history.remove(self.queue[0][1])
            self.queue.pop(0)
        if message in self.history:
            return False
        else:
            self.history.add(message)
            self.queue.append((timestamp, message))
            return True


def main():
    logger = Logger2()
    print(logger.should_print_message(1, "foo"))  # return true, next allowed timestamp for "foo" is 1 + 10 = 11
    print(logger.should_print_message(2, "bar"))  # return true, next allowed timestamp for "bar" is 2 + 10 = 12
    print(logger.should_print_message(3, "foo"))  # 3 < 11, return false
    print(logger.should_print_message(8, "bar"))  # 8 < 12, return false
    print(logger.should_print_message(10, "foo"))  # 10 < 11, return false
    print(logger.should_print_message(11, "foo"))  # 11 >= 11, return true, next allowed timestamp for "foo"
    # is 11 + 10 = 21


if __name__ == "__main__":
    main()
