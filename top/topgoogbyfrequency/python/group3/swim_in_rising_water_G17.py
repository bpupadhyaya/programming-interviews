"""
You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another
 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can
  swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left
 square (0, 0).

Input: grid = [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.

Constraints:
n == grid.length
n == grid[i].length
1 <= n <= 50
0 <= grid[i][j] < n^2
Each value grid[i][j] is unique.

Tag: G17/50
"""
import heapq
import math
from heapq import heappush


def swim_in_water(grid: list[list[int]]) -> int:
    # Getting rows and cols
    r = len(grid)
    c = len(grid[0])

    # 2D array to store minimum elevation to reach there
    cache = [[math.inf for _ in range(c)] for _ in range(r)]

    # Directions to traverse
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Minheap storing (elevation,x co-ordinat, y co-ordinate)
    minheap = [(grid[0][0], 0, 0)]

    # Remains same, as this is start postion
    cache[0][0] = grid[0][0]

    while minheap:
        # Popping position with miniumm elevation
        elevation, i, j = heapq.heappop(minheap)

        # Base case to reach end
        if i == (r-1) and j == (c-1):
            return elevation

        # Traversing 4 directions
        for dx, dy in directions:
            nx, ny = i + dx, j + dy

            if 0 <= nx < r and 0 <= ny < c:

                # "new_elevation" keeping track of max encountered till now
                new_elevation = max(grid[nx][ny], elevation)

                # Update it in cache as well as add in heap if "new_elevation" is less
                # than one in cache
                if new_elevation < cache[nx][ny]:
                    cache[nx][ny] = new_elevation
                    heappush(minheap, (new_elevation, nx, ny))


def main():
    grid = [[0, 2], [1, 3]]
    print(swim_in_water(grid))


if __name__ == "__main__":
    main()
