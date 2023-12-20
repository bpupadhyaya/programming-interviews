"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of
the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area
of water (blue section) the container can contain is 49.
Note: Visualize to understand

Constraints:
n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4

Tag: Tag: R21/145
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

"""
Intuition:
The two-pointer technique starts with the widest container and moves the pointers inward based on the comparison 
of heights.
Increasing the width of the container can only lead to a larger area if the height of the new boundary is greater. 
By moving the pointers towards the center, we explore containers with the potential for greater areas.

Explanation:
Initialize the variables:

left to represent the left pointer, starting at the beginning of the container (index 0).
right to represent the right pointer, starting at the end of the container (index height.size() - 1).
maxArea to keep track of the maximum area found, initially set to 0.
Enter a loop using the condition left < right, which means the pointers have not crossed each other yet.

Calculate the current area:

Use the min function to find the minimum height between the left and right pointers.
Multiply the minimum height by the width, which is the difference between the indices of the pointers: (right - left).
Store this value in the currentArea variable.
Update the maximum area:

Use the max function to compare the currentArea with the maxArea.
If the currentArea is greater than the maxArea, update maxArea with the currentArea.
Move the pointers inward: (Explained in detail below)

Check if the height at the left pointer is smaller than the height at the right pointer.
If so, increment the left pointer, moving it towards the center of the container.
Otherwise, decrement the right pointer, also moving it towards the center.
Repeat steps 3 to 5 until the pointers meet (left >= right), indicating that all possible containers have been explored.

Return the maxArea, which represents the maximum area encountered among all the containers.

Update the maximum area:
The purpose of this condition is to determine which pointer to move inward, either the left pointer (i) or the 
right pointer (j), based on the comparison of heights at their respective positions.

Imagine you have two containers represented by the heights at the left and right pointers. The condition checks 
which container has a smaller height and moves the pointer corresponding to that container.

If height[i] > height[j]:

This means that the height of the left container is greater than the height of the right container.
Moving the right pointer (j) would not increase the potential area because the height of the right container is 
the limiting factor.
So, to explore containers with the possibility of greater areas, we need to move the right pointer inward 
by decrementing j.
If height[i] <= height[j]:

This means that the height of the left container is less than or equal to the height of the right container.
Moving the left pointer (i) would not increase the potential area because the height of the left container is 
the limiting factor.
So, to explore containers with the possibility of greater areas, we need to move the left pointer inward by 
incrementing i.
By making these pointer movements, we ensure that we are always exploring containers with the potential for 
larger areas. The approach is based on the observation that increasing the width of the container can only 
lead to a larger area if the height of the new boundary is greater.
By following this condition and moving the pointers accordingly, the algorithm explores all possible 
containers and finds the one with the maximum area.
"""
