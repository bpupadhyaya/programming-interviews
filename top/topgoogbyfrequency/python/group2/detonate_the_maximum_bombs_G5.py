"""
You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is
in the shape of a circle with the center as the location of the bomb.

The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote
the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range.
 These bombs will further detonate the bombs that lie in their ranges.

Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate
 only one bomb.

Example :
Input: bombs = [[2,1,3],[6,1,4]]
Output: 2
Explanation:
The above figure (visualize to understand) shows the positions and ranges of the 2 bombs.
If we detonate the left bomb, the right bomb will not be affected.
But if we detonate the right bomb, both bombs will be detonated.
So the maximum bombs that can be detonated is max(1, 2) = 2.

"""
import collections
import math


def maximum_detonation(bombs: list[list[int]]) -> int:
    def is_connected(a, b):
        x1, y1, r1 = bombs[a]
        x2, y2, r2 = bombs[b]
        dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        return dist <= r1

    conn = collections.defaultdict(list)
    for i in range(len(bombs)):
        for j in range(len(bombs)):
            if i != j:
                if is_connected(i, j):
                    conn[i].append(j)

    def dfs(node):
        if node in visited:
            return 0

        visited.add(node)

        ans = 1

        if node in conn:
            for child in conn[node]:
                if child in visited:
                    continue
                ans += dfs(child)

        return ans

    max_count = 1
    for node in conn:
        visited = set()
        max_count = max(max_count, dfs(node))
    return max_count


def main():
    bombs = [[2, 1, 3], [6, 1, 4]]
    print(maximum_detonation(bombs))


if __name__ == "__main__":
    main()



"""
Intuition
there are three points
point 1 is located at x=2 with radius 5
point 2 is located at x=5 with radius 1
point 3 is located at x=10 with radius 6

union-find approach will build those three points as a graph. (max rank = 3)
but, in this scenario, the max value is 2 because the point 2 cannot detonate any bomb.

Approach
Building adjacency list
DFS with recursion

Complexity
Time complexity:
O(V + E)

Space complexity:
O(V)
"""