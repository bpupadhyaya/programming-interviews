"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must
 appear as many times as it shows in both arrays and you may return the result in any order.

Example:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements
into the memory at once?

R129/145
"""


def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    sorted_arr1 = sorted(nums1)
    sorted_arr2 = sorted(nums2)
    # Use two pointers i and j for the two arrays and initialize both with zero.
    i = 0
    j = 0

    output = []
    while i < len(sorted_arr1) and j < len(sorted_arr2):
        # If sortedArr1[i] is less than sortedArr2[j]
        # Leave the smaller element and go to next(greater) element in nums1
        if sorted_arr1[i] < sorted_arr2[j]:
            i += 1
        # If sortedArr1[i] is greater than sortedArr2[j]
        # Go to next(greater) element in nums2 array
        elif sorted_arr2[j] < sorted_arr1[i]:
            j += 1
        # If both the elements intersected
        # Add this element to output & increment both i and j
        else:
            output.append(sorted_arr1[i])
            i += 1
            j += 1
    return output


def intersect_1(nums1: list[int], nums2: list[int]) -> list[int]:
    # Create a hash map to count the frequency of each number in nums1
    freq_map = {}
    for num in nums1:
        freq_map[num] = freq_map.get(num, 0) + 1

    # Create an empty list to store the intersection of the two arrays
    result = []

    # Loop through each element in nums2
    for num in nums2:
        # If num exists in the hash map and its frequency is greater than 0
        if num in freq_map and freq_map[num] > 0:
            # Add it to the result list and decrement its frequency in the hash map
            result.append(num)
            freq_map[num] -= 1

    return result


def main():
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(intersect_1(nums1, nums2))


if __name__ == "__main__":
    main()
