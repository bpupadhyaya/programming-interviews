"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
return the k closest points to the origin (0, 0).
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

Tag: 973/2927 , R595/2935 , R26/50 (amz)
"""
import heapq


def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    heap = []
    for (x, y) in points:
        dist = -(x*x + y*y)
        if len(heap) == k:
            heapq.heappushpop(heap, (dist, x, y))
        else:
            heapq.heappush(heap, (dist, x, y))

    return [[x, y] for (dist, x, y) in heap]


def main():
    points = [[3, 3], [5, -1], [-2, 4]]
    k = 2
    print(k_closest(points, k))


if __name__ == "__main__":
    main()

"""
Runtime:
Inserting an item to a heap of size k take O(logK) time.
And we do this for each item points.
So runtime is O(N * logK) where N is the length of points.

Space: O(K) for our heap.
"""