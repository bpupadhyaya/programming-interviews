"""
You are given an m x n binary matrix grid.
In one operation, you can choose any row or column and flip each value in that row or column (i.e., changing
all 0's to 1's, and all 1's to 0's).
Return true if it is possible to remove all 1's from grid using any number of operations or false otherwise.

Example:
Input: grid = [[0,1,0],[1,0,1],[0,1,0]]
Output: true
Explanation: One possible way to remove all 1's from grid is to:
- Flip the middle row
- Flip the middle column

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is either 0 or 1.

Tag: G49/50
"""


def remove_ones(grid: list[list[int]]) -> bool:
    r1, r1_invert = grid[0], [1-val for val in grid[0]]
    for i in range(1, len(grid)):
        if grid[i] != r1 and grid[i] != r1_invert:
            return False
    return True


def remove_ones1(grid: list[list[int]]) -> bool:
    return all(grid[i] == grid[0] or grid[i] == [1-val for val in grid[0]] for i in range(len(grid)))


def main():
    grid = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
    print(remove_ones1(grid))


if __name__ == "__main__":
    main()
