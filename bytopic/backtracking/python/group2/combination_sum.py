"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations
of candidates where the chosen numbers sum to target. You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency of at least one of the chosen numbers is different.
The test cases are generated such that the number of unique combinations that sum up to target is less than 150
combinations for the given input.

Example:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Tag: 104/150
Tag: 39/2927, R360/2936 (overall frequency ranking)
"""


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    res = []

    def dfs(nums, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            dfs(nums, target - nums[i], i, path + [nums[i]], res)

    candidates.sort()
    dfs(candidates, target, 0, [], res)
    return res


def main():
    candidates = [2, 3, 6, 7]
    target = 7
    print(combination_sum(candidates, target))


if __name__ == "__main__":
    main()
