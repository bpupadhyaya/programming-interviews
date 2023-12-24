"""
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.

Tag: R74/145
"""


def subsets(nums: list[int]) -> list[list[int]]:
    # Subsets with no duplicate
    res = []

    def dfs(nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            dfs(nums, i+1, path+[nums[i]], res)

    dfs(sorted(nums), 0, [], res)
    return res


def subsets_with_dup(nums: list[int]) -> list[list[int]]:
    # Subsets with  duplicate
    res = []

    def dfs(nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            dfs(nums, i+1, path+[nums[i]], res)

    nums.sort()
    dfs(nums, 0, [], res)
    return res


def main():
    nums = [1, 2, 3]
    print(subsets(nums))


if __name__ == "__main__":
    main()
