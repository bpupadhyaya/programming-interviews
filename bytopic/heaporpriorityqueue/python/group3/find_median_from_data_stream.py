"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle
value, and the median is the mean of the two middle values.
- For example, for arr = [2,3,4], the median is 3.
- For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:
- MedianFinder() initializes the MedianFinder object.
- void addNum(int num) adds the integer num from the data stream to the data structure.
- double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer
  will be accepted.

Example:
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]
Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    arr = [1]
medianFinder.addNum(2);    arr = [1, 2]
medianFinder.findMedian(); return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    arr[1, 2, 3]
medianFinder.findMedian(); return 2.0

Tag: 124/150
Tag: 295/2927, R304/2936 (overall frequency ranking)
Note: Program compiles but there is runtime error, debug and find out.
"""
from heapq import heappush, heappop


class MedianFinder:
    def __init__(self):
        self.lo = []
        self.hi = []

    def add_num(self, num: int) -> None:
        heappush(self.lo, -num)                 # lo is maxheap, so -1 * num
        heappush(self.hi, -self.lo[0])          # hi is minheap
        heappop(self.lo)
        if len(self.lo) < len(self.hi):
            heappush(self.lo, -self.hi[0])
            heappop(self.hi)

    def find_median(self) -> float:
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        else:
            return (self.hi[0] - self.lo[0]) / 2    # - as low has -ve values


def main():
    median_finder = MedianFinder()
    median_finder.add_num(1)                 # arr = [1]
    median_finder.add_num(2)                 # arr = [1, 2]
    print(median_finder.find_median())       # return 1.5 (i.e., (1 + 2) / 2)
    median_finder.add_num(3)                 # arr[1, 2, 3]
    print(median_finder.find_median())       # return 2.0


if __name__ == "__main__":
    main()
