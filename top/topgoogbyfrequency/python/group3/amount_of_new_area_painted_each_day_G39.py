"""
There is a long and thin painting that can be represented by a number line. You are given a 0-indexed 2D integer
array paint of length n, where paint[i] = [starti, endi]. This means that on the ith day you need to paint the
area between starti and endi.
Painting the same area multiple times will create an uneven painting so you only want to paint each area of the
painting at most once.
Return an integer array worklog of length n, where worklog[i] is the amount of new area that you painted on the ith day.

Example:
Input: paint = [[1,4],[4,7],[5,8]]
Output: [3,3,1]
Explanation:
On day 0, paint everything between 1 and 4.
The amount of new area painted on day 0 is 4 - 1 = 3.
On day 1, paint everything between 4 and 7.
The amount of new area painted on day 1 is 7 - 4 = 3.
On day 2, paint everything between 7 and 8.
Everything between 5 and 7 was already painted on day 1.
The amount of new area painted on day 2 is 8 - 7 = 1.

Constraints:
1 <= paint.length <= 10^5
paint[i].length == 2
0 <= starti < endi <= 5 * 10^4

Tag: G39/50
"""
import bisect


def amount_painted(paint: list[list[int]]) -> list[int]:
    ranges = [0, 0]

    def add_range(start, end):
        left = bisect.bisect_left(ranges, start)
        right = bisect.bisect_right(ranges, end)

        tmp_range = []
        if left % 2 == 0:
            tmp_range.append(start)
        if right % 2 == 0:
            tmp_range.append(end)

        ranges[left:right] = tmp_range

    def query_range(start, end):
        paint_part = 0
        left = bisect.bisect_right(ranges, start)
        right = bisect.bisect_left(ranges, end)

        if left == right and left % 2 == 0:
            paint_part += end - start
        if left % 2 == 0 and left != right:
            paint_part += ranges[left] - start
        if right % 2 == 0 and left != right:
            paint_part += end - ranges[right-1]

        # find paint_part between ranges
        left = left+1 if left % 2 == 0 else left
        for i in range(left, right-1, 2):
            paint_part += ranges[i+1] - ranges[i]

        add_range(start, end)
        return paint_part

    paint_per_day = []

    for start, end in paint:
        paint_part = query_range(start, end)
        paint_per_day.append(paint_part)

    return paint_per_day


def main():
    paint = [[1, 4], [4, 7], [5, 8]]
    print(amount_painted(paint))


if __name__ == "__main__":
    main()
