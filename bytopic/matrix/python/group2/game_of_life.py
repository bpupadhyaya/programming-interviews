"""
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton
devised by the British mathematician John Horton Conway in 1970."
The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1)
or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal)
using the following four rules (taken from the above Wikipedia article):
1. Any live cell with fewer than two live neighbors dies as if caused by under-population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by over-population.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where
births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

Example 1:
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
Note: Visualize to understand
Example 2:
Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
Note: Visualize to understand

Tag: 38/150
Tag: 289/2927, R720/2936 (overall frequency ranking)
Note: program compiles but the output is not correct, debug and fix.
"""


def game_of_life(board: list[list[int]]) -> None:
    directions = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
    for i in range(len(board)):
        for j in range(len(board[0])):
            live = 0
            for x, y in directions:
                if (len(board) > i + x >= 0) and (len(board[0]) > j + y >= 0) and abs(board[i + x][j + y]) == 1:
                    live += 1
            if board[i][j] == 1 and (live < 2 or live > 3):
                board[i][j] = -1
            if board[i][j] == 0 and live == 3:
                board[i][j] = 2
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] = 1 if (board[i][j] > 0) else 0


def main():
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    game_of_life(board)
    print(board)


if __name__ == "__main__":
    main()
