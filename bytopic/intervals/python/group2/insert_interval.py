"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [start_i, end_i] represent
the start and the end of the i^{th} interval and intervals is sorted in ascending order by start_i. You are also
given an interval newInterval = [start, end] that represents the start and end of another interval.
Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i and intervals
still does not have any overlapping intervals (merge overlapping intervals if necessary).
Return intervals after the insertion.

Example:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Tag: 50/150
Tag: 57/2927, R412/2936 (overall frequency ranking)
"""


def insert(inervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    result = []
    for interval in inervals:
        if interval[1] < new_interval[0]:
            result.append(interval)
        elif interval[0] > new_interval[1]:
            result.append(new_interval)
            new_interval = interval
        elif interval[1] >= new_interval[0] or interval[0] <= new_interval[1]:
            new_interval[0] = min(interval[0], new_interval[0])
            new_interval[1] = max(new_interval[1], interval[1])
    result.append(new_interval)
    return result


def main():
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    new_interval = [4, 8]
    print(insert(intervals, new_interval))


if __name__ == "__main__":
    main()
