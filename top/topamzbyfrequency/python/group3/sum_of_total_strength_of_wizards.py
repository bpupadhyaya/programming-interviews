"""
As the ruler of a kingdom, you have an army of wizards at your command.

You are given a 0-indexed integer array strength, where strength[i] denotes the strength of the ith wizard.
For a contiguous group of wizards (i.e. the wizards' strengths form a subarray of strength), the total strength
is defined as the product of the following two values:
- The strength of the weakest wizard in the group.
- The total of all the individual strengths of the wizards in the group.

Return the sum of the total strengths of all contiguous groups of wizards. Since the answer may be very large,
return it modulo 10^9 + 7.

A subarray is a contiguous non-empty sequence of elements within an array.

Example:
Input: strength = [1,3,1,2]
Output: 44
Explanation: The following are all the contiguous groups of wizards:
- [1] from [1,3,1,2] has a total strength of min([1]) * sum([1]) = 1 * 1 = 1
- [3] from [1,3,1,2] has a total strength of min([3]) * sum([3]) = 3 * 3 = 9
- [1] from [1,3,1,2] has a total strength of min([1]) * sum([1]) = 1 * 1 = 1
- [2] from [1,3,1,2] has a total strength of min([2]) * sum([2]) = 2 * 2 = 4
- [1,3] from [1,3,1,2] has a total strength of min([1,3]) * sum([1,3]) = 1 * 4 = 4
- [3,1] from [1,3,1,2] has a total strength of min([3,1]) * sum([3,1]) = 1 * 4 = 4
- [1,2] from [1,3,1,2] has a total strength of min([1,2]) * sum([1,2]) = 1 * 3 = 3
- [1,3,1] from [1,3,1,2] has a total strength of min([1,3,1]) * sum([1,3,1]) = 1 * 5 = 5
- [3,1,2] from [1,3,1,2] has a total strength of min([3,1,2]) * sum([3,1,2]) = 1 * 6 = 6
- [1,3,1,2] from [1,3,1,2] has a total strength of min([1,3,1,2]) * sum([1,3,1,2]) = 1 * 7 = 7
The sum of all the total strengths is 1 + 9 + 1 + 4 + 4 + 4 + 3 + 5 + 6 + 7 = 44.


Tag: 2281/2927 , R347/2935 , R20/50 (amz)
"""
from itertools import accumulate


def total_strength(strength: list[int]) -> int:
    mod, n = 10 ** 9 + 7, len(strength)
    # Get the first index of the non-larger value to strength[]'s right.
    right_index = [n] * n
    stack = []
    for i in range(n):
        while stack and strength[stack[-1]] >= strength[i]:
            right_index[stack.pop()] = i
        stack.append(i)

    # Get the first index of the smaller value to strength[i]'s left.
    left_index = [-1] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and strength[stack[-1]] > strength[i]:
            left_index[stack.pop()] = i
        stack.append(i)

    # prefix sum of the prefix sum array of strength
    presum_of_presum = list(accumulate(accumulate(strength, initial=0), initial=0))
    answer = 0

    # For each element in strength, we get the value of R_term - L_term
    for i in range(n):
        # Get the left index and the right index
        left_bound = left_index[i]
        right_bound = right_index[i]

        # Get the left_count and right_count
        left_count = i - left_bound
        right_count = right_bound - i

        # Get positive presum and the negative presum
        neg_presum = (presum_of_presum[i+1] - presum_of_presum[i - left_count + 1]) % mod
        pos_presum = (presum_of_presum[i + right_count + 1] - presum_of_presum[i + 1]) % mod

        # The total strength of all subarray that have strength[i] as minimum.
        answer += strength[i] * (pos_presum * left_count - neg_presum * right_count)
        answer %= mod

    return answer


def main():
    strength = [1, 3, 1, 2]
    print(total_strength(strength))


if __name__ == "__main__":
    main()


"""
Interesting comment on this problem from internet:

There is really ONLY ONE way to do it in O(n) and on top of that you need to have 2-3 big intuitive leaps to 
get there. There seems to be no middle ground to solve this problem easily and no easy way to 
get from O(n^2) -> O(n log n) let alone O(n). There is no way to tradeoff more space to gain time unless you 
use a DP or combine other difficult concepts like Sparse Arrays and Binary trees which have overhead of their own. 
This problem allows for very little of that kind of thinking.

Unless you know of some of these ideas upfront there is no way you can solve this in < 40 mins in an interview.

Complexity
Time complexity: O(n) if you can manage to convince yourself and the interviewer of the prefix sum and 
monotonic stack approach

Space complexity: O(n)

"""