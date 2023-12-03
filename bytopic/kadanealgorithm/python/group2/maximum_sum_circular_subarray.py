"""
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.
A circular array means the end of the array connects to the beginning of the array. Formally, the next element of
nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].
A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i],
nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

Example:
Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.

Tag: 113/150
Tag: 918/2927, R949/2936 (overall frequency ranking)
"""


def max_subarray_sum_circular_using_dynamic_programming(nums: list[int]) -> int:
    if max(nums) <= 0:
        return max(nums)

    max_dp = [i for i in nums]
    min_dp = [i for i in nums]

    for i in range(1, len(nums)):
        if max_dp[i-1] > 0:
            max_dp[i] += max_dp[i-1]
        if min_dp[i-1] < 0:
            min_dp[i] += min_dp[i-1]

    return max(max(max_dp), sum(nums) - min(min_dp))


def max_subarray_sum_circular_using_kadane(nums: list[int]) -> int:
    if max(nums) <= 0:
        return max(nums)
    max_sum = curr_max = min_sum = curr_min = nums[0]

    for i in range(1, len(nums)):
        curr_max = max(nums[i], curr_max + nums[i])
        max_sum = max(max_sum, curr_max)
        curr_min = min(nums[i], curr_min + nums[i])
        min_sum = min(min_sum, curr_min)
    return max(max_sum, sum(nums) - min_sum)


def main():
    nums = [5, -3, 5]
    print(max_subarray_sum_circular_using_kadane(nums))


if __name__ == "__main__":
    main()
