"""
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

Sample 1:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Tag: 121/150
Tag: 215/2927, R24/2936 (overall frequency ranking), fb R2/50
"""
import heapq


def find_kth_largest(nums: list[int], k: int) -> int:
    heap = nums[:k]
    heapq.heapify(heap)

    for num in nums[k:]:
        if num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)

    return heap[0]


def main():
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    print(find_kth_largest(nums, k))


if __name__ == "__main__":
    main()

"""
Note:
The idea is to break the list into two parts 0 to k and k (inclusive) to last element.
Compare each element in second partition with each element in first partition and if greater: remove smallest
from the first partition (note: heappop(<heap-name>) removes the smallest and maintains the order) and push the larger
one in the first partition (again order / heap invariant is maintained). Repeat until all elements in second partition
are covered. By that time, first partition will have k largest elements in sorted order. First element is the k
largest.
"""
