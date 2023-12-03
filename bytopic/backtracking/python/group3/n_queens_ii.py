
"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that
no two queens attack each other.
Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Note: Find visuals to understand

Tag: 105/150
Tag: 52/2927, R1500/2936 (overall frequency ranking)
"""


def total_n_queens(n: int) -> int:
    visited_cols = set()
    visited_diagonals = set()
    visited_anti_diagonals = set()

    def backtrack(r):
        if r == n:  # Valid solution state
            return 1

        cnt = 0
        for c in range(n):
            if not (c in visited_cols or (r-c) in visited_diagonals or (r+c) in visited_anti_diagonals):
                visited_cols.add(c)
                visited_diagonals.add(r - c)
                visited_anti_diagonals.add(r + c)
                cnt += backtrack(r + 1)  # count the overall tally from this current state

                visited_cols.remove(c)
                visited_diagonals.remove(r - c)
                visited_anti_diagonals.remove(r + c)
        return cnt
    return backtrack(0)


def main():
    n = 4
    print(total_n_queens(n))


if __name__ == "__main__":
    main()
