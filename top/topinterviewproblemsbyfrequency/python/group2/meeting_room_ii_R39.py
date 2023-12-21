"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number
 of conference rooms required.

Example:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Constraints:
1 <= intervals.length <= 10^4
0 <= starti < endi <= 10^6

Tag: R39/145
"""


def min_meeting_rooms(intervals: list[list[int]]) -> int:
    rooms = 0
    if not intervals:
        return 0
    endp = 0
    starts = sorted([i[0] for i in intervals])
    ends = sorted([i[1] for i in intervals])
    for i in range(len(starts)):
        if starts[i] >= ends[endp]:
            endp += 1
        else:
            rooms += 1
    return rooms


def main():
    intervals = [[0, 30], [5, 10], [15, 20]]
    print(min_meeting_rooms(intervals))


if __name__ == "__main__":
    main()
