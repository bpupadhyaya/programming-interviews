"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return
the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Example 1:
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.

Tag: fb R27/50, 973/2927, R595/2936
"""

import heapq


def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    heap = []
    for (x, y) in points:
        dist = -(x**2 + y**2)
        heapq.heappush(heap, (dist, x, y))
        if len(heap) > k:
            heapq.heappop(heap)

    return [x[1:] for x in heap]


def k_closest1(points: list[list[int]], k: int) -> list[list[int]]:
    return heapq.nsmallest(k, points, key=lambda x: x[0]**2 + x[1]**2)


def main():
    points = [[1, 3], [-2, 2]]
    k = 1
    print('Output: ', k_closest1(points, k))


if __name__ == "__main__":
    main()

"""
We keep a min heap of size K.
For each item, we insert an item to our heap.
If inserting an item makes heap size larger than k, then we immediately pop an item after inserting (heappushpop).

Runtime:
Inserting an item to a heap of size k take O(logk) time.
And we do this for each item points.
So runtime is O(n * logk) where N is the length of points.

Space: O(k) for our heap.
"""