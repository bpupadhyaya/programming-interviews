"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return
the area of the largest rectangle in the histogram.

Example:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Note: Visualize to understand

Constraints:
1 <= heights.length <= 10^5
0 <= heights[i] <= 10^4

Tag: R36/145
"""


def largest_rectangle(heights: list[int]) -> int:
    st, res = [], 0
    for height in heights + [-1]: # add -1 to have an additional iteration
        step = 0
        while st and st[-1][1] >= height:
            w, h = st.pop()
            step += w
            res = max(res, step * h)
        st.append((step + 1, height))
    return res


def main():
    heights = [2, 1, 5, 6, 2, 3]
    print(largest_rectangle(heights))


if __name__ == "__main__":
    main()


"""
The idea is to use a monotonic stack. We iterate over bars and add them to the stack as long as the last element in 
the stack is less than the current bar. When the condition doesn't hold, we start to calculate areas by popping out 
bars from the stack until the last element of the stack is greater than the current. The area is calculated as the 
number of pops multiplied by the height of the popped bar. On every pop, the height of the bar will be less or equal 
to the previous (since elements in the stack are always monotonically increasing).

Now let's consider this example [2,1,2]. For this case the formula for the area (number of pops * current height) 
won't work because when we reach 1 we will pop out 2 from the stack and will not consider it later which is wrong 
since the largest area here is equal to 3 * 1, i.e we somehow need to remember the previously discarded bars that 
still can form areas. We solve this problem by storing in the stack the width of the bar as well. So for our 
example, after discarding 2, we push to the stack the 1 with the width equal to 2.

Time: O(n) - In the worst case we have 2 scans: one for the bars and one for the stack
Space: O(n) - in the wors case we push to the stack the whole input array
"""