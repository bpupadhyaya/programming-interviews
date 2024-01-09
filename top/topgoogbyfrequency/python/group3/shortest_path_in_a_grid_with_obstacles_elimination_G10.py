"""
You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle).
 You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower
right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible
to find such walk return -1.

Example:
Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
Output: 6
Explanation:
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2)
 -> (1,2) -> (2,2) -> (3,2) -> (4,2).

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 40
1 <= k <= m * n
grid[i][j] is either 0 or 1.
grid[0][0] == grid[m - 1][n - 1] == 0

"""
import collections


def shortest_path(grid: list[list[int]], k: int) -> int:
    rows = len(grid)
    cols = len(grid[0])
    # Directions we'll use to change our location (down, up, right, left).
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    # We'll use a deque for our BFS traversal.
    q = collections.deque([])
    # Append our starting details to the q.
    # (row, col, steps, k)
    q.append((0, 0, 0, k))
    # Use a set (O(1) lookup) to track the locations we've visited to avoid revisiting.
    seen = set()
    while q:
        # Pop the next location from the q.
        r, c, steps, rk = q.popleft()
        # If we're at the finish location return the steps, given BFS this will be
        # guaranteed to be the first to hit this condition.
        if r == rows-1 and c == cols - 1:
            return steps
        # Otherwise we'll keep travelling through the grid in our 4 directions.
        else:
            for y, x in directions:
                nr = r + y
                nc = c + x
                # If the new location is on the board and has not been visited.
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc, rk) not in seen:
                    # If it's a blocker, but we still have k left, we'll go there and k -= 1.
                    if grid[nr][nc] == 1 and rk > 0:
                        seen.add((nr, nc, rk))
                        q.append((nr, nc, steps + 1, rk - 1))
                    # Otherwise continue on  if it's a 0 - free location.
                    elif grid[nr][nc] == 0:
                        seen.add((nr, nc, rk))
                        q.append((nr, nc, steps + 1, rk))
        # If we don't hit the end in our traversal we know it's not possible.
    return -1


def main():
    grid = [[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]]
    k = 1
    print(shortest_path(grid, k))


if __name__ == "__main__":
    main()

"""
Explanation:
Work our way through the grid one step at a time (multiple searches running at a time given we have 4 different
 directions to explore at any given step).
Each step we check if we're at the end of our our grid, if not we continue the search.
Continuing the search we look at the next step of our 4 directions and make sure its valid (on the board, can 
afford to move an object or it's a clear 0), we record the step taken deduct 1 from k if it was a 1 location and
 put it back on the q.
We repeat this until we hit the end or run out of locations to explore in which case we couldn't make it to the 
end so we return -1.
"""