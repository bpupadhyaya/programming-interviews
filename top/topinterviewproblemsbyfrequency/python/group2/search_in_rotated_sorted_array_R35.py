"""
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums,
or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.

Example:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Tag: R35/145
"""


def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        # Check if left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Otherwise, right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


def main():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(search(nums, target))


if __name__ == "__main__":
    main()


"""
Approach
Given the properties of the array, it's tempting to perform a linear search. However, that would result in a 
time complexity of O(n). Instead, we can use the properties of the array to our advantage and apply a 
binary search to find the target with time complexity of O(logn) only.

Treating the Rotated Array
Although the array is rotated, it retains some properties of sorted arrays that we can leverage. Specifically, 
one half of the array (either the left or the right) will always be sorted. This means we can still apply binary 
search by determining which half of our array is sorted and whether the target lies within it.

Binary Search
Binary search is an efficient algorithm for finding a target value within a sorted list. It works by repeatedly 
dividing the search interval in half. If the value of the search key is less than the item in the middle of the 
interval, narrow the interval to the lower half. Otherwise, narrow it to the upper half. Repeatedly check until 
the value is found or the interval is empty.

Initialization
We start with two pointers:

left- This represents the beginning of the array. We initialize it to 0, the index of the first element.
right - This represents the end of the array. It's set to n−1n - 1n−1, the index of the last 
element, where nnn is the length of the array.
Iterative Binary Search
We perform the binary search within a while loop until left exceeds right. 
In each iteration, we calculate the midpoint between left and right.

Deciding the Sorted Half:
At any point during the search in the rotated array, one half (either the left or the right) will always 
be sorted. Determining which half is sorted is crucial for our modified binary search.

If left half [low...mid][low...mid][low...mid] is sorted: We know this if the element at low
is less than or equal to the element at mid. In a normally sorted array, if the start is less 
than or equal to the midpoint, it means all elements till the midpoint are in the correct increasing order.

If the target lies within this sorted left half: We know this if the target is greater than or equal to the 
element at low and less than the element at mid. If this is the case, we then move 
our search to this half, meaning, we update high to mid−1.

Otherwise: The target must be in the right half. So, we update low to mid+1.

If right half [mid...high][mid...high][mid...high] is sorted: This is the else part. If the left half 
isn't sorted, the right half must be!

If the target lies within this sorted right half: We know this if the target is greater than the element 
at mid and less than or equal to the element at high. If so, we move our search 
to this half by updating low to mid+1.

Otherwise: The target must be in the left half. So, we update high to mid−1.

Rationale:
The beauty of this approach lies in its ability to determine with certainty which half of the array to 
look in, even though the array is rotated. By checking which half of the array is sorted and then using 
the sorted property to determine if the target lies in that half, we can effectively eliminate half of the 
array from consideration at each step, maintaining the O(logn) time complexity of the binary search.

Complexity
Time Complexity: The time complexity is O(logn) since we're performing a binary search over 
the elements of the array.

Space Complexity: The space complexity is O(1) because we only use a constant amount of space to store 
our variables (left, right, mid), regardless of the size of the input array.
"""
