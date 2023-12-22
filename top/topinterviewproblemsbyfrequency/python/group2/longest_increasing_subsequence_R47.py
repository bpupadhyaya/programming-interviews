"""
Given an integer array nums, return the length of the longest strictly increasing subsequence

Example:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Constraints:
1 <= nums.length <= 2500
-104 <= nums[i] <= 10^4

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?


Tag: R47/145
"""
from bisect import bisect_left


def length_of_longest_increasing_subs_1(nums: list[int]) -> int:
    # Binary search cheating
    arr = [nums.pop(0)]  # 1. Initial step
    for n in nums:  # 2. Iterate through nums
        if n > arr[-1]:  # 2.a
            arr.append(n)
        else:  # 2.b
            arr[bisect_left(arr, n)] = n
    return len(arr)  # 3. Return the length of arr


def length_of_longest_increasing_subs_2(nums: list[int]) -> int:
    # Method: DP
    total_number = len(nums)
    dp = [0 for _ in range(total_number)]
    for i in range(1, total_number):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp) + 1


def length_of_longest_increasing_subs_3(nums: list[int]) -> int:
    # Binary search
    tails = [0] * len(nums)
    result = 0
    for num in nums:
        left_index, right_index = 0, result
        while left_index != right_index:
            middle_index = left_index + (right_index - left_index) // 2
            if tails[middle_index] < num:
                left_index = middle_index + 1
            else:
                right_index = middle_index
        result = max(result, left_index + 1)
        tails[left_index] = num
    return result


def main():
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(length_of_longest_increasing_subs_3(nums))


if __name__ == "__main__":
    main()


"""
Explanation for length_of_longest_increasing_subs_1:
# Suppose, for example:
                    #           nums = [1,8,4,5,3,7],
                    # for which the longest strictly increasing subsequence is arr = [1,4,5,7],
                    # giving len(arr) = 4 as the answer
                    #
                    # Here's the plan:
                    #   1) Initiate arr = [num[0]], which in this example means arr = [1]
                    #     
                    #   2) Iterate through nums. 2a) If n in nums is greater than arr[-1], append n to arr. 2b) If 
                    #      not, determine the furthest position in arr at which n could be placed so that arr
                    #      remains strictly increasing, and overwrite the element at that position in arr with n.

                    #   3) Once completed, return the length of arr.

                    # Here's the iteration for the example:

                    #       nums = [ _1_, 8,4,5,3,7]     arr = [1]              (initial step)
                    #       nums = [1, _8_, 4,5,3,7]     arr = [1, 8]           (8 > 1, so    append 8)
                    #       nums = [1,8, _4_, 5,3,7]     arr = [1, 4]           (4 < 8, so overwrite 8)
                    #       nums = [1_8,4, _5_, 3,7]     arr = [1, 4, 5]        (5 > 4, so    append 5)
                    #       nums = [1_8,4,5, _3_, 7]     arr = [1, 3, 5]        (3 < 5, so overwrite 4)
                    #       nums = [1_8,4,5,3, _7_ ]     arr = [1, 3, 5, 7]     (7 > 5, so    append 7)    

                    # Notice that arr is not the sequence given above as the correct seq. The ordering for [1,3,5,7]
                    # breaks the "no changing the order" rule. Cheating? Maybe... However len(arr) = 4 is the 
                    # correct answer. Overwriting 4 with 3 did not alter the sequence's length.
"""
