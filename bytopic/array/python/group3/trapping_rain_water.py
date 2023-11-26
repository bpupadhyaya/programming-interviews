"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

Example:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.
Note: visualize to understand.

Tag: 16/150
Tag: 42/2927, R7/2936 (overall frequency ranking)
"""


def trap_using_two_pointer(height: list[int]) -> int:
    ans = 0
    l, r = 0, len(height) - 1
    l_max, r_max = 0, 0
    while l < r:
        # case 1: lower_bound is from left.
        if height[l] < height[r]:
            if height[l] >= l_max:
                l_max = height[l]
            else:
                ans += l_max - height[l]
            l += 1
        # case 2: the lower_bound is from right.
        else:
            if height[r] >= r_max:
                r_max = height[r]
            else:
                ans += r_max - height[r]
            r -= 1
    return ans
    # Time complexity: O(n)
    # Space complexity: O(1)


def trap_using_dynamic_programming(height: list[int]) -> int:
    if not height:
        return 0
    n = len(height)
    max_left = [0]*n
    max_right = [0]*n
    max_left[0] = 0
    max_right[n-1] = 0
    for i in range(1, n):
        max_left[i] = max(max_left[i-1], height[i-1])
    for i in range(n-2, -1, -1):
        max_right[i] = max(max_right[i+1], height[i+1])
    output = 0
    for i in range(n):
        lower_boundary = min(max_left[i], max_right[i])
        max_trap_at_i = lower_boundary - height[i]
        if max_trap_at_i > 0:
            output += max_trap_at_i
    return output
    # Time complexity : O(n)
    # Space complexity: O(n)


def main():
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trap_using_dynamic_programming(height))


if __name__ == "__main__":
    main()
