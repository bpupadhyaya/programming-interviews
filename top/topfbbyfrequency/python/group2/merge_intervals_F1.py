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


def merge1(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []

    merged = []
    intervals.sort(key=lambda x: x[0])

    prev = intervals[0]

    for interval in intervals[1:]:
        if interval[0] <= prev[1]:
            prev[1] = max(prev[1], interval[1])
        else:
            merged.append(prev)
            prev = interval

    merged.append(prev)

    return merged


def main():
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(merge1(intervals))


if __name__ == "__main__":
    main()

"""
merge1 explanation:
Intuition
Sort intervals with start points. It takes advantage of the fact that the intervals are sorted by start point,
 which allows us to avoid comparing every interval to every other interval.

Approach
This is based on Python code. Other languages might be different.

The merge method takes a list of lists as an argument. Each inner list represents an interval, and the first
 element of the inner list is the start point, and the second element is the end point.

Check if the given list is empty, if yes, return an empty list.

Initialize an empty list named merged to store the merged intervals.

Sort the given list of intervals by the first element of each interval using the sort method and a lambda function.

Set the variable prev to the first interval of the sorted intervals list.

Iterate over the sorted intervals list, starting from the second interval.

Check if the start point of the current interval is less than or equal to the end point of the previous interval.

If yes, then update the end point of the previous interval with the maximum of the current interval's end point
 and the previous interval's end point.

If no, then append the previous interval to the merged list and set prev to the current interval.

After the loop, append the last interval (prev) to the merged list.
Return the merged list containing the merged intervals.

Complexity
This is based on Python code. Other languages might be different.

Time complexity: O(n log n)
n is the length of the input list 'intervals'. This is because the code sorts the intervals list in O(n log n) time
 using the built-in Python sorting algorithm, and then iterates over the sorted list once in O(n) time to merge
  overlapping intervals.

Space complexity: O(n)
n is the length of the input list 'intervals'. This is because the code creates a new list 'merged' to store the
 merged intervals, which can contain up to n elements if there are no overlapping intervals. Additionally, the
  code uses a constant amount of space to store the 'prev' variable and other temporary variables, which does not
   depend on the size of the input.
"""
