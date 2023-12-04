"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Tag: 120/150
Tag: 4/2927, R14/2936 (overall frequency ranking)
"""


def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    m, n = len(nums1), len(nums2)
    low, high = 0, m
    while low <= high:
        partition_x = (low + high) // 2
        partition_y = (m + n + 1) // 2 - partition_x

        max_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
        max_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
        min_x = float('inf') if partition_x == m else nums1[partition_x]
        min_y = float('inf') if partition_y == n else nums2[partition_y]

        if max_x <= min_y and max_y <= min_x:
            if (m + n) % 2 == 0:
                return (max(max_x, max_y) + min(min_x, min_y)) / 2
            else:
                return max(max_x, max_y)
        elif max_x > min_y:
            high = partition_x - 1
        else:
            low = partition_x + 1


def main():
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(find_median_sorted_arrays(nums1, nums2))


if __name__ == "__main__":
    main()
