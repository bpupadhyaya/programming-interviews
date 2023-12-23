"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Tag: R64/145
Tag: 103/150
Tag: 46/2927, R160/2936 (overall frequency ranking)
"""


def permute_using_dfs(nums: list[int]) -> list[list[int]]:
    def dfs(path, used):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if not used[i]:
                path.append(nums[i])
                used[i] = True
                dfs(path, used)
                path.pop()
                used[i] = False
    result = []
    dfs([], [False] * len(nums))
    return result


def permute_using_backtrack(nums: list[int]) -> list[list[int]]:
    def backtrack(nums, path):
        if not nums:
            result.append(path)
            return
        for i in range(len(nums)):
            backtrack(nums[:i] + nums[i+1:], path + [nums[i]])
    result = []
    backtrack(nums, [])
    return result


def main():
    nums = [1, 2, 3]
    print(permute_using_backtrack(nums))


if __name__ == "__main__":
    main()
