"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the
array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Tag: 46/150
Tag: 219/2927, R402/2936 (overall frequency ranking)
"""


def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    # Create hset for storing previous of k elements.
    hset = {}
    for idx in range(len(nums)):
        # If duplicate element is present at distance less than or equal to k, return true.
        if nums[idx] in hset and abs(idx - hset[nums[idx]]) <= k:
            return True
        hset[nums[idx]] = idx

    # If no duplicate element is found then return false
    return False


def main():
    nums = [1, 2, 3, 1]
    k = 3
    print(contains_nearby_duplicate(nums, k))


if __name__ == "__main__":
    main()
