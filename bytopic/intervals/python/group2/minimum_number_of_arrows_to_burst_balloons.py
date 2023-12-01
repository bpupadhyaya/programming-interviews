"""
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are
represented as a 2D integer array points where points[i] = [x_start, x_end] denotes a balloon whose horizontal
diameter stretches between x_start and x_end. You do not know the exact y-coordinates of the balloons.
Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis.
A balloon with x_start and x_end is burst by an arrow shot at x if x_start <= x <= x_end. There is no limit to the
number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.
Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

Example:
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

51/150
Tag: 452/2927, R1291/2936 (overall frequency ranking)
"""


def find_min_arrow_shots(points: list[list[int]]) -> int:
    points.sort(key=lambda x: x[0])
    stack = []
    for sp, ep in points:
        if len(stack) > 0 and stack[-1][1] >= sp:
            last_sp, last_ep = stack.pop()
            stack.append([max(sp, last_sp), min(ep, last_ep)])
        else:
            stack.append([sp, ep])
    return len(stack)


def main():
    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    print(find_min_arrow_shots(points))


if __name__ == "__main__":
    main()
