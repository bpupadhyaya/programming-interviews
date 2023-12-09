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


def trap_using_two_pointer(height: list[int]) -> int:
    if len(height) <= 2:
        return 0
    ans = 0
    # Use two pointers i and j on indices 1 and n-1
    i = 1
    j = len(height) - 1
    # Initialize left max to the leftmost bar and right max to the rightmost bar
    left_max = height[0]
    right_max = height[-1]

    while i <= j:
        # Check left_max and right_max for current i, j positions
        if height[i] > left_max:
            left_max = height[i]
        if height[j] > right_max:
            right_max = height[j]

        # Fill water upto left_max level for index i and move i to the right
        if left_max <= right_max:
            ans += left_max - height[i]
            i += 1

        # Fill water upto right_max level for index j and move j to the left
        else:
            ans += right_max - height[j]
            j -= 1

    return ans


def main():
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trap_using_two_pointer(height))


if __name__ == "__main__":
    main()

"""
Implementation note for two pointer:
Time complexity O(n)
Space complexity O(1)

Water units trapped in each index of the array is calculated and added individually.
Water level at an index is determined by the lower of max_left and max_right for any bar,i.e. essentially water 
trapped in bar i depends on min(max_left, right_left).
Water trapped in index i = min(max_left, max_right) - height[i].
Therefore if max_left < max_right, we fill the left index up to max_left, and advance the left pointer; and 
vice versa. If max_left equals max_right, moving either pointer would work.
"""
