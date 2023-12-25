"""
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed
from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings
collectively.

The geometric information of each building is given in the array buildings where buildings[i] =
[lefti, righti, heighti]:

lefti is the x coordinate of the left edge of the ith building.
righti is the x coordinate of the right edge of the ith building.
heighti is the height of the ith building.
You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

The skyline should be represented as a list of "key points" sorted by their x-coordinate in the
form [[x1,y1],[x2,y2],...]. Each key point is the left endpoint of some horizontal segment in the skyline except
the last point in the list, which always has a y-coordinate 0 and is used to mark the skyline's termination where
the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the
skyline's contour.

Note: There must be no consecutive horizontal lines of equal height in the output skyline. For instance,
 [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable; the three lines of height 5 should be merged into
 one in the final output as such: [...,[2 3],[4 5],[12 7],...]

Example:
Note: Visualize to understand
Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
Explanation:
Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the
output list.

R97/145
"""
import heapq
from bisect import bisect_left, bisect_right


def get_skyline(buildings: list[list[int]]) -> list[list[int]]:
    # Need debugging, incorrect output
    if len(buildings) == 0:
        return []

    buildings.sort(key=lambda v: v[2])
    pos, height = [0], [0]
    for left, right, h in buildings:
        i = bisect_left(pos, left)
        j = bisect_right(pos, right)
        height[i:j] = [left, right]
    print(height, pos)
    res = []
    prev = 0
    for v, h in zip(pos, height):
        if h != prev:
            res.append([v, h])
            prev = h
    return res


def get_skyline_1(buildings: list[list[int]]) -> list[list[int]]:
    # for the same x, (x, -H) should be in front of (x, 0)
    # For Example 2, we should process (2, -3) then (2, 0), as there's no height change
    x_height_right_tuples = sorted([(L, -H, R) for L, R, H in buildings]
                                   + [(R, 0, "doesn't matter") for _, R, _ in buildings])
    # (0, float('inf')) is always in max_heap, so max_heap[0] is always valid
    result, max_heap = [[0, 0]], [(0, float('inf'))]
    for x, negative_height, R in x_height_right_tuples:
        while x >= max_heap[0][1]:
            # reduce max height up to date, i.e. only consider max height in the right side of line x
            heapq.heappop(max_heap)
        if negative_height:
            # Consider each height, as it may be the potential max height
            heapq.heappush(max_heap, (negative_height, R))
        curr_max_height = -max_heap[0][0]
        if result[-1][1] != curr_max_height:
            result.append([x, curr_max_height])
    return result[1:]


def main():
    buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    print(get_skyline_1(buildings))


if __name__ == "__main__":
    main()
