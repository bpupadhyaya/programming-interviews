"""
Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
You may assume the input array always has a valid answer.

Example:
Input: nums = [1,5,1,1,6,4]
Output: [1,6,1,5,1,4]
Explanation: [1,4,1,5,1,6] is also accepted.

Constraints:
1 <= nums.length <= 5 * 10^4
0 <= nums[i] <= 5000
It is guaranteed that there will be an answer for the given input nums.

Follow Up: Can you do it in O(n) time and/or in-place with O(1) extra space?

R140/145
"""


def wiggle_sort_0(nums: list[int]) -> None:
    tmp = nums.copy()
    tmp.sort()
    n = len(nums)
    i, j = 1, n - 1
    for _ in range(2):
        for k in range(i, n, 2):  # when i == 1 then gt elements and when i == 0 then sm elements with jump of 2
            nums[k] = tmp[j]  # sorted array tmp reverse order values assignment
            j -= 1
        i -= 1


def wiggle_sort(nums: list[int]) -> None:
    n = len(nums)
    nums.sort()
    mid = (n - 1) // 2
    nums[::2], nums[1::2] = nums[mid::-1], nums[:mid:-1]


def main():
    nums = [1, 5, 1, 1, 6, 4]
    wiggle_sort_0(nums)
    print(nums)


if __name__ == "__main__":
    main()

"""
wiggle_sort explanation:
Approach
We first sort the array nums in ascending order.
We then find the median of the array (i.e., the middle element if the array has odd length, or one of the two middle
 elements if the array has even length). We can use (n - 1) // 2 to find the index of the median element.
We then create two subarrays: one containing the larger half of the sorted nums array, and one containing the smaller
 half. We can use slicing to achieve this: nums[mid::-1] gives us the elements from the median index backwards to the
  start of the array, and nums[:mid:-1] gives us the elements from the median index forwards to the end of the array,
   in reverse order.
Finally, we use slicing again to interleave the elements of the two subarrays. We use nums[::2] to get every second
 element starting from the first element, and nums[1::2] to get every second element starting from the second element.
  We assign the elements from the larger subarray to the even indices, and the elements from the smaller subarray to
   the odd indices.
Here's a step-by-step explanation of how the code works:

n = len(nums): Gets the length of the input array nums.

nums.sort(): Sorts the array in ascending order. This is necessary because the algorithm needs to rearrange the array
 in a specific pattern.

mid = (n - 1) // 2: Calculates the index of the middle element in the sorted array.

nums[::2], nums[1::2] = nums[mid::-1], nums[:mid:-1]: This is where the main algorithm takes place.

nums[::2]: Slices the array starting from the first element and selects every second element (i.e. elements with even
 indices).
nums[1::2]: Slices the array starting from the second element and selects every second element (i.e. elements with 
odd indices).
nums[mid::-1]: Slices the array starting from the middle element and selects every element backwards (i.e. in
 descending order).
nums[:mid:-1]: Slices the array starting from the element after the middle element and selects every element
 backwards (i.e. in descending order).
By doing this slicing and reassignment, we're essentially rearranging the array in a "wiggle" pattern. Specifically,
 the even-indexed elements are the larger half of the sorted array, and the odd-indexed elements are the smaller half
  of the sorted array. This ensures that adjacent elements alternate between being larger and smaller.
The original array nums is now sorted in a wiggle pattern.
Overall, the time complexity of this solution is O(n log n) due to the sorting operation. The space complexity is
 O(n) due to the slicing and reassignment of nums.
 
wiggle_sort_0 explanation:
1. We have to copy array into temporary space
2. Sort temporary array in ascending order
3. Then run loop of size 2
4. During loop we have to swap elements of orignal array with temporary array
5. Swap temporary array values form end (j index point to last till i ! = end of array) and keep assigning value 
in orignal array start from i = 1 with jump of 2.
6. Then reduce i - 1 -> i = 0 and start filling value where we left the j and keep assigning values to original array
 from i = 0 index till end with jump of 2.

"""
