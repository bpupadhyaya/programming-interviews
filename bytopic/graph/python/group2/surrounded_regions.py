"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.

Tag: 90/150
Tag: 130/2927, R804/2936 (overall frequency ranking)
"""
from collections import deque


def solve(board: list[list[str]]) -> None:
    o = "O"

    n = len(board)
    m = len(board[0])

    deq = deque()

    for i in range(n):
        if board[i][0] == o:
            deq.append((i, 0))
        if board[i][m-1] == o:
            deq.append((i, m-1))

    for j in range(m):
        if board[0][j] == o:
            deq.append((0, j))
        if board[n-1][j] == o:
            deq.append((n-1, j))

    def in_bounds(i, j):
        return (0 <= i < n) and (0 <= j < m)

    while deq:
        i, j = deq.popleft()
        board[i][j] = "#"

        for ii, jj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if not in_bounds(ii, jj):
                continue
            if board[ii][jj] != o:
                continue
            deq.append((ii, jj))
            board[ii][jj] = '#'

    for i in range(n):
        for j in range(m):
            if board[i][j] == o:
                board[i][j] = 'X'
            elif board[i][j] == '#':
                board[i][j] = o


def main():
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]]
    solve(board)
    print(board)


if __name__ == "__main__":
    main()
