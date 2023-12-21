"""
Given an unsorted integer array nums, return the smallest missing positive integer.
You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example:
Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.

Example:
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Constraints:
1 <= nums.length <= 10^5
-2^{31} <= nums[i] <= 2^{31} - 1

Tag: R37/145
"""


def first_missing_positive(nums: list[int]) -> int:
    """ Step 1 -> The main idea behind it is that the minimum number to be found will always be in the range [1....n]
    where 'n' is the length of list. So keep numbers in this range and mark others
    (here we are marking them with (n+1) value) in the list provided. """
    n = len(nums)
    for i in range(n):
        if nums[i] < 1 or nums[i] > n:
            nums[i] = n + 1
    """
    Step 2 -> Ignoring the values greater than 'n', mark the indexes of the numbers in the range [1...n]
    so as to ensure that this values are present. To mark the indexes, 
    I am negating the value present at that index.
    """
    for i in range(n):
        val = abs(nums[i])
        if val > n:
            continue
        val -= 1  # Since the list is zero indexed,so every value will be at position val - 1
        if nums[val] > 0:
            # For similar numbers, it will keep on fluctuating between negative and positive
            # which is not our motive here.
            nums[val] = -1 * nums[val]
    # Step 3 -> Return the first occurrence of the non-negative numbers from the list
    for i in range(n):
        if nums[i] >= 0:
            return i + 1  # list is zero indexed
    """
    Step 4 -> We will encounter this if no positives were found. This means that all the 
    numbers are in the range [1....n]. So the missing positive number will be n+1
    """
    return n + 1


def main():
    nums = [1, 2, 0]
    print(first_missing_positive(nums))


if __name__ == "__main__":
    main()
