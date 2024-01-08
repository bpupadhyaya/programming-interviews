"""
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

Example:
Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Note: Visualize to understand.

Tag: fb R42/50, 766/2927, R1232/2936
"""


def is_toeplitz_matrix(matrix: list[list[int]]) -> bool:
    r_len, c_len = len(matrix), len(matrix[0])

    for r in range(1, r_len):
        for c in range(1, c_len):
            if matrix[r][c] != matrix[r-1][c-1]:
                return False

    return True


def main():
    matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    print("Is Toeplitz? ", is_toeplitz_matrix(matrix))


if __name__ == "__main__":
    main()