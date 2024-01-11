"""
Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of
the ith balloon.
Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she
asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer
 array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.
Return the minimum time Bob needs to make the rope colorful.

Example:
Input: colors = "abaac", neededTime = [1,2,3,4,5]
Output: 3
Explanation: In the above image, 'a' is blue, 'b' is red, and 'c' is green.
Bob can remove the blue balloon at index 2. This takes 3 seconds.
There are no longer two consecutive balloons of the same color. Total time = 3.

Constraints:
n == colors.length == neededTime.length
1 <= n <= 105
1 <= neededTime[i] <= 104
colors contains only lowercase English letters.

Tag: M50/50
"""


def min_cost(colors: str, needed_time: list[int]) -> int:
    total_time = 0
    i = 0
    j = 0

    while i < len(needed_time) and j < len(needed_time):
        curr_total = 0
        curr_max = 0

        while j < len(needed_time) and colors[i] == colors[j]:
            curr_total += needed_time[j]
            curr_max = max(curr_max, needed_time[j])
            j += 1

        total_time += curr_total - curr_max
        i = j

    return total_time


def main():
    colors = "abaac"
    needed_time = [1, 2, 3, 4, 5]
    print(min_cost(colors, needed_time))


if __name__ == "__main__":
    main()

"""
Explanation:
-The function minCost calculates the minimum cost needed for removing balloons of different colors within their groups.
-It uses two pointers (i and j) to traverse the neededTime array and analyze groups of balloons with the same color.
-Inside the while loop, it accumulates the total removal time for each color group (currTotal) and identifies the 
maximum removal time within that group (currMax).
-It subtracts the maximum removal time from the total removal time within each color group and adds this cost to 
the totalTime.
-Finally, it returns the computed totalTime.

Complexity
Time complexity: O(n)
Space complexity: O(1)
"""
