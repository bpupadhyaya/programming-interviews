"""
The distance of a pair of integers a and b is defined as the absolute difference between a and b.
Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j]
where 0 <= i < j < nums.length.

Example 1:
Input: nums = [1,3,1], k = 1
Output: 0
Explanation: Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.

Example 2:
Input: nums = [1,6,1], k = 3
Output: 5

Tag: 719/2927 , R849/2935 , R31/50 (amz)
"""


def smallest_distance_pair(nums: list[int], k: int) -> int:
    def check(dist: int) -> bool:
        i = j = cnt = 0
        for i in range(n):      # Use two pointers to count pairs with distance no greater than k
            while j < n and nums[j] - nums[i] <= dist:
                cnt += j - i
                j += 1

        return cnt >= k         # Return whether at least k such pairs exist

    nums.sort()
    n, left, right = len(nums), 0, nums[-1] - nums[0]

    while left < right:         # Binary search
        mid = (left + right) // 2
        if check(mid):
            right = mid
        else:
            left = mid + 1

    return left


def main():
    nums = [1, 6, 1]
    k = 3
    print(smallest_distance_pair(nums, k))


if __name__ == "__main__":
    main()

