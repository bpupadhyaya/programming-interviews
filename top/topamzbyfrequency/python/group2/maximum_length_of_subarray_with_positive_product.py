"""
Given an array of integers nums, find the maximum length of a subarray where the product of all its
elements is positive.
A subarray of an array is a consecutive sequence of zero or more values taken out of that array.
Return the maximum length of a subarray with positive product.

Example:
Input: nums = [0,1,-2,-3,-4]
Output: 3
Explanation: The longest subarray with positive product is [1,-2,-3] which has a product of 6.
Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.

Tag: 1567/2927 , R946/2935 , R34/50 (amz)
"""


def get_max_len(nums: list[int]) -> int:
    # Dynamic programming
    n = len(nums)
    pos, neg = [0] * n, [0] * n
    if nums[0] > 0:
        pos[0] = 1
    if nums[0] < 0:
        neg[0] = 1
    ans = pos[0]
    for i in range(1, n):
        if nums[i] > 0:
            pos[i] = 1 + pos[i - 1]
            neg[i] = 1 + neg[i - 1] if neg[i - 1] > 0 else 0
        elif nums[i] < 0:
            pos[i] = 1 + neg[i - 1] if neg[i - 1] > 0 else 0
            neg[i] = 1 + pos[i - 1]
        ans = max(ans, pos[i])
    return ans


def main():
    nums = [0, 1, -2, -3, -4]
    print(get_max_len(nums))


if __name__ == "__main__":
    main()

"""
Complexity
time: O(N)
space: O(N)
"""