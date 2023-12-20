"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1_,2_,2,3_,5,6] with the underscored elements coming from nums1.

Tag: R7/145
"""


def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    idx = 0
    for i in range(len(nums1)):
        if idx >= n:
            break
        if nums1[i] == 0:
            nums1[i] = nums2[idx]
            idx += 1
    nums1.sort()


def merge_1(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    i = m - 1  # Initialize nums1's index
    j = n - 1  # Initialize nums2's index
    k = m + n - 1  # Initialize a variable k to store the last index of the 1st array
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            k -= 1
            i -= 1
        else:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1


def main():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    merge_1(nums1, m, nums2, n)
    print(nums1)


if __name__ == "__main__":
    main()

