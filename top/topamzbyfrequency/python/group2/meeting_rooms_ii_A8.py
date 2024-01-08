"""
Given an array of meeting time intervals 'intervals' where intervals[i] = [starti, endi], return the minimum
number of conference rooms required.
Example:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Tag: 253/2927 , R70/2935 , R8/50 (amz)
"""

from heapq import heappush
from heapq import heappop


def min_meeting_rooms(intervals: list[list[int]]) -> int:
    rooms = 0
    if not intervals:
        return 0
    endp = 0
    starts = sorted([i[0] for i in intervals])
    ends = sorted(i[1] for i in intervals)

    for i in range(len(starts)):
        if starts[i] >= ends[endp]:
            endp += 1
        else:
            rooms += 1
    return rooms


def min_meeting_rooms_using_line_sweep(intervals: list[list[int]]) -> int:
    endpoints = []
    for start, end in intervals:
        endpoints.append((start, 1))
        endpoints.append((end, -1))
    endpoints.sort()
    res = need = 0
    for _, delta in endpoints:
        need += delta
        res = max(res, need)
    return res


def min_meeting_rooms_using_heap(intervals: list[list[int]]) -> int:
    # Heap solution (equivalent to sorting), time complexity O(nlogn), space complexity O(n)
    heap = []
    for interval in intervals:
        heappush(heap, (interval[0], 1))
        heappush(heap, (interval[1], -1))
    meetings = 0
    num_rooms = 0
    while heap:
        meetings += heap[0][1]
        num_rooms = max(num_rooms, meetings)
        heappop(heap)
    return num_rooms


def min_meeting_rooms_using_heap_2(intervals: list[list[int]]) -> int:
    intervals.sort()
    rooms = []
    for interval in intervals:
        s, e = interval
        heappush(rooms, e)
        if rooms[0] <= s:
            heappop(rooms)
    return len(rooms)


def main():
    intervals = [[0, 30], [5, 10], [15, 20]]
    print(min_meeting_rooms_using_line_sweep(intervals))


if __name__ == "__main__":
    main()
