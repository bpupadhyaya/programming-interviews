"""
You are given an integer array nums of 2 * n integers. You need to partition nums into two arrays of length n to
minimize the absolute difference of the sums of the arrays. To partition nums, put each element of nums into one of
the two arrays.
Return the minimum possible absolute difference.

Example 1:
Input: nums = [3,9,7,3]
Output: 2
Explanation: One optimal partition is: [3,9] and [7,3].
The absolute difference between the sums of the arrays is abs((3 + 9) - (7 + 3)) = 2.

Example 2:
Input: nums = [2,-1,0,4,-2,-9]
Output: 0
Explanation: One optimal partition is: [2,4,-9] and [-1,0,-2].
The absolute difference between the sums of the arrays is abs((2 + 4 + -9) - (-1 + 0 + -2)) = 0.

Constraints:
1 <= n <= 15
nums.length == 2 * n
-10^7 <= nums[i] <= 10^7

Tag: M10/50
"""
import bisect
from collections import defaultdict
from itertools import combinations


def minimum_difference(nums: list[int]) -> int:
    N = len(nums) // 2  # Note this is N/2, ie no. of elements required in each.

    def get_sums(nums_):  # generate all combinations sum of k elements
        ans = {}
        N = len(nums_)
        for k in range(1, N+1):  # takes k element for nums
            sums = []
            for comb in combinations(nums_, k):
                s = sum(comb)
                sums.append(s)
            ans[k] = sums
        return ans

    left_part, right_part = nums[:N], nums[N:]
    left_sums, right_sums = get_sums(left_part), get_sums(right_part)
    ans = abs(sum(left_part) - sum(right_part))  # the case when taking all N from left_part for left_ans,
    # and vice versa
    total = sum(nums)
    half = total // 2  # the best sum required for each, we have to find sum nearest to this
    for k in range(1, N):
        left = left_sums[k]  # if taking k no. from left_sums
        right = right_sums[N-k]  # then we have to take remaining N-k from right_sums.
        right.sort()  # sorting, so that we can binary search the required value
        for x in left:
            r = half - x  # required, how much we need to add in x to bring it closer to half.
            p = bisect.bisect_left(right, r)  # we are finding index of value closest to r, present in right,
            # using binary search
            for q in [p, p-1]:
                if 0 <= q < len(right):
                    left_ans_sum = x + right[q]
                    right_ans_sum = total - left_ans_sum
                    diff = abs(left_ans_sum - right_ans_sum)
                    ans = min(ans, diff)
    return ans


def minimum_difference1(nums: list[int]) -> int:
    # Time complexity: O(2**(n//2)log(2*(n//2)))
    # Space complexity: O(2**(n//2))
    def subset_sums(ans):
        d = defaultdict(set)

        for i in range(1, len(ans)):
            d[i] = sorted(set([sum(j) for j in combinations(ans, i)]))
        return d

    n = len(nums)

    total, l, r = sum(nums), nums[:n//2], nums[n//2:]
    d1, d2, min_diff = subset_sums(l), subset_sums(r), abs(sum(l)-sum(r))

    for k in d1:
        left, right = d1[k], d2[n//2-k]
        for x in left:
            i = bisect.bisect_left(right, total//2-x)

            if i < len(right):
                min_diff = min(min_diff, abs((right[i]+x)*2-total))
            if i > 0:
                min_diff = min(min_diff, abs((right[i-1]+x)*2-total))

    return min_diff


def main():
    nums = [3, 9, 7, 3]
    # nums = [2, -1, 0, 4, -2, -9]
    print(minimum_difference1(nums))


if __name__ == "__main__":
    main()
