"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how
much water it can trap after raining.

Example:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.
Noted: Visualize to understand. black sections are the bars, blue sections are the gaps between bars that can hold
water (could say that is water)

Tag: 42/2927 , R7/2935 , R2/50 (amz)
"""


def trap(height: list[int]) -> int:
    if len(height) <= 2:
        return 0

    ans = 0

    # Using two pointers i and j on indices 1 and n-1
    i = 1
    j = len(height) - 1

    # Initializing left_max to the leftmost bar and right_max to the rightmost bar
    left_max = height[0]
    right_max = height[-1]

    while i <= j:
        # Check left_max and right_max for current i, j positions
        if height[i] > left_max:
            left_max = height[i]
        if height[j] > right_max:
            right_max = height[j]

        # Fill water upto left_max level for index i and move it to the right
        if left_max <= right_max:
            ans += left_max - height[i]
            i += 1

        # Fill water upto right_max level for index j and move j t othe left
        else:
            ans += right_max - height[j]
            j -= 1

    return ans


def main():
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print("Water trapped: ", trap(height))


if __name__ == "__main__":
    main()

"""
- Water units trapped in each index of the array is calculated and added individually.
- Water level at an index is determined by the lower of max_left and max_right for any bar,i.e. essentially water 
  trapped in bar i depends on min(max_left, right_left).
- Water trapped in index i = min(max_left, max_right) - height[i].
- Therefore if max_left < max_right, we fill the left index up to max_left, and advance the left pointer; and 
  vice versa. If max_left equals max_right, moving either pointer would work.

Time complexity ~ O(n)
Space complexity ~ O(1)
"""