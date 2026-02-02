"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Constraints:
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.

Tag: 44/150, R1/145 (top interview frequency ranking)
Tag: 1/2927, R1/2936 (overall frequency ranking)
Cat: g1
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    # Implementation method: one-pass hash table
    num_map = {}
    n = len(nums)

    for i in range(n):
        complement = target - nums[i]
        if complement in num_map:
            return [num_map[complement], i]
        num_map[nums[i]] = i
    return []


def main():
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))


if __name__ == "__main__":
    main()


"""
Algo:
1. Create an empty hash table to store elements and their indices.
2. Iterate through the array from left to right.
3. For each element nums[i], calculate the complement by subtracting it from the target: complement = target - nums[i].
4. Check if the complement exists in the hash table. If it does, we have found a solution.
5. If the complement does not exist in the hash table, add the current element nums[i] to the hash table with its 
  index as the value.
6. Repeat steps 3-5 until we find a solution or reach the end of the array.
7. If no solution is found, return an empty array or an appropriate indicator.

Complexity:
This approach has a time complexity of O(n) since hash table lookups take constant time on average. 
It allows us to solve the Two Sum problem efficiently by making just one pass through the array.
"""
