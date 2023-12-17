"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water
it can trap after raining.

Example:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case,
6 units of rain water (blue section) are being trapped.
Note: Visualize to understand

Constraints:
n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5

Tag: Tag: R6/145
"""


def trap(height: list[int]) -> int:
    if len(height) <= 2:
        return 0
    ans = 0

    # Using two pointers i and j on indices 1 and n-1
    i = 1
    j = len(height) - 1

    # Initializing leftmax to the leftmost bar and rightmax to the rightmost bar
    lmax = height[0]
    rmax = height[-1]
    while i <= j:
        # Check lmax and rmax for current i, j positions
        if height[i] > lmax:
            lmax = height[i]
        if height[j] > rmax:
            rmax = height[j]

        # Fill water upto lmax level for index i and move i to the right
        if lmax <= rmax:
            ans += lmax - height[i]
            i += 1

        # Fill water upto rmax level for index j and move j to the left
        else:
            ans += rmax - height[j]
            j -= 1
    return ans


def main():
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trap(height))


if __name__ == "__main__":
    main()

"""
Approach:
Water units trapped in each index of the array is calculated and added individually.
Water level at an index is determined by the lower of max_left and max_right for any bar,i.e. essentially water 
trapped in bar i depends on min(max_left, right_left).
Water trapped in index i = min(max_left, max_right) - height[i].
Therefore if max_left < max_right, we fill the left index up to max_left, and advance the left pointer; 
and vice versa. If max_left equals max_right, moving either pointer would work.

Complexity:
Time complexity O(n)
Space complexity O(1)

"""