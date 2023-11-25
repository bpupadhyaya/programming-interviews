"""
You are given a 0-indexed integer array nums.
Swaps of adjacent elements are able to be performed on nums.
A valid array meets the following conditions:
- The largest element (any of the largest elements if there are multiple) is at the rightmost position in the array.
- The smallest element (any of the smallest elements if there are multiple) is at the leftmost position in the array.

Return the minimum swaps required to make nums a valid array.

Example:
Input: nums = [3,4,5,5,3,1]
Output: 6
Explanation: Perform the following swaps:
- Swap 1: Swap the 3rd and 4th elements, nums is then [3,4,5,3,5,1].
- Swap 2: Swap the 4th and 5th elements, nums is then [3,4,5,3,1,5].
- Swap 3: Swap the 3rd and 4th elements, nums is then [3,4,5,1,3,5].
- Swap 4: Swap the 2nd and 3rd elements, nums is then [3,4,1,5,3,5].
- Swap 5: Swap the 1st and 2nd elements, nums is then [3,1,4,5,3,5].
- Swap 6: Swap the 0th and 1st elements, nums is then [1,3,4,5,3,5].
It can be shown that 6 swaps is the minimum swaps required to make a valid array.

Tag: 2340/2927 , R1153/2935 , R38/50 (amz)
"""


def minimum_swaps(nums: list[int]) -> int:
    min_value = max_index = nums[0]
    min_index = max_value = 0
    for i, n in enumerate(nums):
        if n < min_value:
            min_value = n
            min_index = i

        if n >= max_value:
            max_value = n
            max_index = i

    return min_index + len(nums) - 1 - max_index - (min_index > max_index)


def minimum_swaps_1(nums: list[int]) -> int:
    min_ = min(nums)                                    # find minimum
    idx1 = nums.index(min_)                             # locate the first minimum from the left side

    nums = [nums[idx1]] + nums[:idx1] + nums[idx1+1:]   # make the swaps and update `nums`

    max_ = max(nums)                                    # find maximum
    idx2 = nums[::-1].index(max_)                       # locate the first max from the right side

    return idx1 + idx2                                  # return total swaps needed


def main():
    nums = [3, 4, 5, 5, 3, 1]
    print(minimum_swaps_1(nums))


if __name__ == "__main__":
    main()

"""
Explanation for 2nd implementation:
- When talking about swap, it's very likely to run into Greedy algorithm. In this case, we want to move the 
minimum to the leftmost side then find how many swaps need to move maximum to the rightmost side.
- See inline comment for more explanation
Complexity: t: O(N), s: O(1)
"""