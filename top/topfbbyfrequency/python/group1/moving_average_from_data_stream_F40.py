"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:
MovingAverage(int size) Initializes the object with the size of the window size.
double next(int val) Returns the moving average of the last size values of the stream.

Example 1:
Input
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output
[null, 1.0, 5.5, 4.66667, 6.0]

Explanation
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3

Constraints:

1 <= size <= 1000
-10^5 <= val <= 10^5
At most 10^4 calls will be made to next.

Tag: F40/50
"""
from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        self.length = 0
        self.max = size
        self.sum = 0
        self.queue = deque()

    def next(self, val: int) -> float:
        if self.length < self.max:
            self.length +=1
            self.queue.append(val)
            self.sum += val
        else:
            self.sum -= self.queue.popleft()
            self.queue.append(val)
            self.sum += val
        return self.sum/self.length


def main():
    moving_average = MovingAverage(3)
    print(moving_average.next(1))  # return 1.0 = 1 / 1
    print(moving_average.next(10))  # return 5.5 = (1 + 10) / 2
    print(moving_average.next(3))  # return 4.66667 = (1 + 10 + 3) / 3
    print(moving_average.next(5))  # return 6.0 = (10 + 3 + 5) / 3


if __name__ == "__main__":
    main()
