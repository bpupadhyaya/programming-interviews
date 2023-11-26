"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are
at nums[i], you can jump to any nums[i + j] where:
0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach
nums[n - 1].

Example:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1,
then 3 steps to the last index.

Tag: 10/150
Tag: 45/2927, R258/2936 (overall frequency ranking)
"""


def jump(nums: list[int]) -> int:
    ans = 0
    end = 0
    farthest = 0
    # Implicit BFS
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if farthest >= len(nums) - 1:
            ans += 1
            break
        if i == end:    # Visited all the items on the current level
            ans += 1    # Increment the level
            end = farthest  # Make the queue size for the next level

    return ans


def main():
    nums = [2,3,1,1,4]
    print(jump(nums))


if __name__ == "__main__":
    main()
