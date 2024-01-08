"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and
return an array of the non-overlapping intervals that cover all the intervals in the input.

Example:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Tag: R15/145, F1/50 (fb)
"""


def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals = sorted(intervals, key=lambda x: x[0])
    ans = []
    for interval in intervals:
        if not ans or ans[-1][1] < interval[0]:
            # if the list of merged intervals is empty
            # or if the current interval does not overlap with the previous,
            # simply append it.
            ans.append(interval)
        else:
            # otherwise, there is overlap,
            # so we merge the current and previous intervals.
            ans[-1][1] = max(ans[-1][1], interval[1])

    return ans


def main():
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(merge(intervals))


if __name__ == "__main__":
    main()
