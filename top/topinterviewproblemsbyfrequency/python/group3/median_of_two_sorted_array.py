"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10^6 <= nums1[i], nums2[i] <= 10^6

Tag: R11/145
"""


def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    # Binary search method
    n1 = len(nums1)
    n2 = len(nums2)

    # Ensure nums1 is the smaller array for simplicity
    if n1 > n2:
        return find_median_sorted_arrays(nums2, nums1)

    n = n1 + n2
    left = (n1 + n2 + 1) // 2  # Calculate the left partition size
    low = 0
    high = n1

    while low <= high:
        mid1 = (low + high) // 2  # Calculate mid index for nums1
        mid2 = left - mid1  # Calculate mid index for nums2

        l1 = float('-inf')
        l2 = float('-inf')
        r1 = float('inf')
        r2 = float('inf')

        # Determine values of l1, l2, r1, and r2
        if mid1 < n1:
            r1 = nums1[mid1]
        if mid2 < n2:
            r2 = nums2[mid2]
        if mid1 - 1 >= 0:
            l1 = nums1[mid1 - 1]
        if mid2 - 1 >= 0:
            l2 = nums2[mid2 - 1]

        if l1 <= r2 and l2 <= r1:
            # The partition is correct, we found the median
            if n % 2 == 1:
                return max(l1, l2)
            else:
                return (max(l1, l2) + min(r1, r2)) / 2.0
        elif l1 > r2:
            # Move towards the left side of nums1
            high = mid1 - 1
        else:
            # Move towards the right side of nums1
            low = mid1 + 1

    return 0  # If the code reaches here, the input arrays were not sorted.


def main():
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(find_median_sorted_arrays(nums1, nums2))


if __name__ == "__main__":
    main()


"""
Approach:
Binary Search
Use binary search to partition the smaller of the two input arrays into two parts.
Find the partition of the larger array such that the sum of elements on the left side of the partition in both arrays 
is half of the total elements.
Check if this partition is valid by verifying if the largest number on the left side is smaller than the smallest 
number on the right side.
If the partition is valid, calculate and return the median.

Time Complexity:
O(logm/logn)
Space Complexity:
O(1)
"""



