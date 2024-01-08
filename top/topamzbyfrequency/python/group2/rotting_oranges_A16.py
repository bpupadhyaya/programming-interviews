"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.
If this is impossible, return -1.

Example:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Note: Visualize to understand.

Tag: 994/2927 , R333/2935 , R16/50 (amz)
"""
from collections import deque


def oranges_rotting(grid: list[list[int]]) -> int:
    rows = len(grid)
    if rows == 0:
        return -1
    cols = len(grid[0])
    fresh_count = 0
    rotten = deque()

    # visit each cell in the grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                rotten.append((r, c))
            elif grid[r][c] == 1:
                fresh_count += 1

    # keep track of minutes passed.
    minutes_passed = 0

    while rotten and fresh_count > 0:
        # it is safe to update the minutes by 1, since we visit oranges level by level in BFS traversal.
        minutes_passed += 1

        # process rotten oranges in the current level
        for _ in range(len(rotten)):
            x, y = rotten.popleft()

            # visit all the adjacent cells
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                # calculate the coordinate of the adjacent cell
                xx, yy = x + dx, y + dy
                # ignore the cell if it is out of the grid boundary
                if xx < 0 or xx == rows or yy < 0 or yy == cols:
                    continue
                # ignore the cell if it is empty '0' or visited before '2'
                if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                    continue

                # update the fresh oranges count
                fresh_count -= 1

                # mark the current fresh orange rotten
                grid[xx][yy] = 2

                # add the current rotten to the queue
                rotten.append((xx, yy))

    return minutes_passed if fresh_count == 0 else -1


def main():
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    print(oranges_rotting(grid))


if __name__ == "__main__":
    main()

"""
Time complexity: O(rows * cols) -> each cell is visited at least once
Space complexity: O(rows * cols) -> in the worst case, if all the oranges are rotten
"""