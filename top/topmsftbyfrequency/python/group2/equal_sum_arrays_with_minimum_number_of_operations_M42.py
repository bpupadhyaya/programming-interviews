"""
You are given two arrays of integers nums1 and nums2, possibly of different lengths. The values in the arrays are
 between 1 and 6, inclusive.
In one operation, you can change any integer's value in any of the arrays to any value between 1 and 6, inclusive.
Return the minimum number of operations required to make the sum of values in nums1 equal to the sum of values in
 nums2. Return -1 if it is not possible to make the sum of the two arrays equal.

Example 1:
Input: nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]
Output: 3
Explanation: You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed.
- Change nums2[0] to 6. nums1 = [1,2,3,4,5,6], nums2 = [6,1,2,2,2,2].
- Change nums1[5] to 1. nums1 = [1,2,3,4,5,1], nums2 = [6,1,2,2,2,2].
- Change nums1[2] to 2. nums1 = [1,2,2,4,5,1], nums2 = [6,1,2,2,2,2].

Constraints:
1 <= nums1.length, nums2.length <= 10^5
1 <= nums1[i], nums2[i] <= 6

Tag: M42/50
"""
from heapq import heapify, heapreplace


def min_operations0(nums1: list[int], nums2: list[int]) -> int:
    if 6*len(nums1) < len(nums2) or 6*len(nums2) < len(nums1):
        return -1

    if sum(nums1) < sum(nums2):
        nums1, nums2 = nums2, nums1
    s1, s2 = sum(nums1), sum(nums2)

    nums1 = [-x for x in nums1]  # max-heap
    heapify(nums1)
    heapify(nums2)

    ans = 0
    while s1 > s2:
        x1, x2 = nums1[0], nums2[0]
        if -1-x1 > 6-x2:  # change x1 to 1
            s1 += x1 + 1
            heapreplace(nums1, -1)
        else:
            s2 += 6 - x2
            heapreplace(nums2, 6)
        ans += 1
    return ans


def min_operations(nums1: list[int], nums2: list[int]) -> int:
    # Two pointer
    if 6*len(nums1) < len(nums2) or 6*len(nums2) < len(nums1):
        return -1  # impossible

    if sum(nums1) < sum(nums2):
        nums1, nums2 = nums2, nums1
    s1, s2 = sum(nums1), sum(nums2)  # s1 >= s2

    nums1.sort()
    nums2.sort()

    ans = j = 0
    i = len(nums1)-1

    while s1 > s2:
        if j >= len(nums2) or 0 <= i and nums1[i] - 1 > 6 - nums2[j]:
            s1 += 1 - nums1[i]
            i -= 1
        else:
            s2 += 6 - nums2[j]
            j += 1
        ans += 1
    return ans


def main():
    nums1 = [1, 2, 3, 4, 5, 6]
    nums2 = [1, 1, 2, 2, 2, 2]
    print(min_operations(nums1, nums2))


if __name__ == "__main__":
    main()
