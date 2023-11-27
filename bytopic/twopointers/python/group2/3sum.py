"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Tag: 29/150
Tag: 15/2927, R15/2936 (overall frequency ranking)
"""


def three_sum(nums: list[int]) -> list[list[int]]:
    res = set()
    # 1. Split nums into three lists: negative numbers, positive numbers, and zeros
    n, p, z = [], [], []
    for num in nums:
        if num > 0:
            p.append(num)
        elif num < 0:
            n.append(num)
        else:
            z.append(num)
    # 2. Create a separate set for negatives and positives for O(1) look-up times
    set_n, set_p = set(n), set(p)
    # 3. If there is at least one zero in the list, all all cases where -num exists in set_n and num exists in set_p
    # e. g. (-3, 0, 3) = 0
    if z:
        for num in set_p:
            if -1 * num in set_n:
                res.add((-1 * num, 0, num))
    # 3. If there are at least 3 zeroes in the list then also include (0, 0, 0) = 0
    if len(z) >= 3:
        res.add((0, 0, 0))
    # 4. For all pairs of negative numbers (-3, -1), check to see if their complement (4) exists
    # in the positive number set
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            target = -1 * (n[i] + n[j])
            if target in set_p:
                res.add(tuple(sorted([n[i], n[j], target])))
    # 5. For all pairs of positive numbers (1, 1), check to see if their complement (-2) exists in
    # the negative number set
    for i in range(len(p)):
        for j in range(i+1, len(p)):
            target = -1 * (p[i] + p[j])
            if target in set_n:
                res.add(tuple(sorted([p[i], p[j], target])))
    return res


def main():
    nums = [-1, 0, 1, 2, -1, -4]
    print(three_sum(nums))


if __name__ == "__main__":
    main()
