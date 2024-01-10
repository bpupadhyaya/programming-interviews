"""
Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships
on board.
Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of
the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal
 or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

Example:
Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2

Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is either '.' or 'X'.

Follow up: Could you do it in one-pass, using only O(1) extra memory and without modifying the values board?

"""


def count_battleships(board: list[list[str]]) -> int:
    count = 0

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == "X":
                if (i == 0 or board[i - 1][j] == ".") and (j == 0 or board[i][j - 1] == "."):
                    count += 1

    return count


def count_battleships1(board: list[list[str]]) -> int:
    return sum(1 for i, row in enumerate(board) for j, cell in enumerate(row) if
               cell == "X" and (i == 0 or board[i - 1][j] == ".") and (j == 0 or board[i][j - 1] == "."))


def main():
    board = [["X", ".", ".", "X"],
             [".", ".", ".", "X"],
             [".", ".", ".", "X"]]

    print(count_battleships1(board))


if __name__ == "__main__":
    main()

"""
O(nm) soln without modifying board.
"""
