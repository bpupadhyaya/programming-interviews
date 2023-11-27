"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints
of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of
water (blue section) the container can contain is 49.
Note: Visualize to understand, blue section is the area covered between second and last vertical lines, in above array.

Tag: 28/150
Tag: 11/2927, R30/2936 (overall frequency ranking)
"""


def max_area(height: list[int]) -> int:
    left = 0
    right = len(height) - 1
    max_area_ = 0
    while left < right:
        current_area = min(height[left], height[right]) * (right - left)
        max_area_ = max(max_area_, current_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area_


def main():
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(max_area(height))


if __name__ == "__main__":
    main()
