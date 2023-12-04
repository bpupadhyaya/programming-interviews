"""
You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.
Define a pair (u, v) which consists of one element from the first array and one element from the second array.
Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

Example 1:
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

Example 2:
Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

Example 3:
Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [[1,3],[2,3]]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]

Tag: 123/150
Tag: 373/2927, R380/2936 (overall frequency ranking)
"""
import heapq


def k_smallest_pairs(nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
    res = []
    pq = []
    for x in nums1:
        heapq.heappush(pq, [x + nums2[0], 0])
    while k > 0 and pq:
        pair = heapq.heappop(pq)
        s, pos = pair[0], pair[1]
        res.append([s - nums2[pos], nums2[pos]])
        if pos + 1 < len(nums2):
            heapq.heappush(pq, [s - nums2[pos] + nums2[pos + 1], pos + 1])
        k -= 1
    return res


def main():
    nums1 = [1, 7, 11]
    nums2 = [2, 4, 6]
    k = 3
    print(k_smallest_pairs(nums1, nums2, k))


if __name__ == "__main__":
    main()
