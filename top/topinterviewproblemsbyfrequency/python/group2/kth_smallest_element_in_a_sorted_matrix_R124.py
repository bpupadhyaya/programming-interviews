"""
Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest
element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n^2).

Example:
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 300
-10^9 <= matrix[i][j] <= 10^9
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2


Follow up:

Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
Could you solve the problem in O(n) time complexity? The solution may be too advanced for an interview but you
may find reading this (http://www.cse.yorku.ca/~andy/pubs/X+Y.pdf) paper fun.

R124/145
"""
import heapq
from heapq import heappush, heappop


def kth_smallest(matrix: list[list[int]], k: int) -> int:
    if not matrix or not matrix[0]:
        return -1
    heap = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            next_val = -matrix[row][col]
            if len(heap) < k:
                heapq.heappush(heap, next_val)
            elif next_val > heap[0]:
                heapq.heappushpop(heap, next_val)
    return -heap[0]


def kth_smallest_1(matrix: list[list[int]], k: int) -> int:
    a, res = [], -1
    for r in matrix:
        for e in r:
            heappush(a, e)
    for _ in range(k):
        res = heappop(a)
    return res


def kth_smallest_2(matrix: list[list[int]], k: int) -> int:
    res = []
    for r in matrix:
        res += 1
    return sorted(res)[k-1]


def main():
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8
    print(kth_smallest_1(matrix, k))


if __name__ == "__main__":
    main()
