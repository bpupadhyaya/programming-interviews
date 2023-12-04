"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number
of points that lie on the same straight line.

Example:
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Note: Visualization may be needed to understand

Tag: 136/150
Tag: 149/2927, R289/2936 (overall frequency ranking)
"""
from collections import defaultdict
from math import gcd


def max_points(points: list[list[int]]) -> int:
                                            #   points = [[1,0],[2,1],[3,4], [5,4]]

    points.sort()                           #   point1 point2 (dx,dy)    m     slope               mm
    slope, mm = defaultdict(int), 0         #   –––––– –––––– ––––––– –––––––  –––––––––––        –––––
                                            #   [1,0]  [2,1]   (1,1)   (1,1)   {(1,1):1}            1
    for i, (x1, y1) in enumerate(points):   #          [3,4]   (2,4)   (1,2)   {(1,1):1,(1,2):1}    1
                                            #          [5,4]   (4,4)   (1,1)   {(1,1):2,(1,2):1}    2
        slope.clear()                       #   [2,1]  [3,4]   (1,3)   (1,3)   {(1,3):1}            2
                                            #          [5,4]   (3,3)   (1,1)   {(1,3):1,(1,1):1}    2
        for x2, y2 in points[i + 1:]:       #   [3,4]  [5,4]   (3,0)   (1,0)   {(1,0):1}            2
            dx, dy = x2 - x1, y2 - y1
                                            #  mm + 1 = 2 + 1 = 3 <-- return
            gg = gcd(dx, dy)
            m = (dx//gg, dy//gg)

            slope[m] += 1
            if slope[m] > mm:
                mm = slope[m]

    return mm + 1


def main():
    points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    print(max_points(points))


if __name__ == "__main__":
    main()
