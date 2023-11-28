"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Example:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Note: Visualize to understand

Tag: 37/150
Tag: 73/2927, R91/2936 (overall frequency ranking)
"""


def set_zeroes(matrix: list[list[int]]) -> None:
    m = len(matrix)
    n = len(matrix[0])
    first_row_has_zero = False
    first_col_has_zero = False
    # Iterate through matrix to mark the zero row and cols
    for row in range(m):
        for col in range(n):
            if matrix[row][col] == 0:
                if row == 0:
                    first_row_has_zero = True
                if col == 0:
                    first_col_has_zero = True
                matrix[row][0] = matrix[0][col] = 0
    # Iterate through matrix to update the cell to be zero if it's in a zero row or col
    for row in range(1, m):
        for col in range(1, n):
            matrix[row][col] = 0 if matrix[0][col] == 0 or matrix[row][0] == 0 else matrix[row][col]
    # Update the first row and col if they are zero
    if first_row_has_zero:
        for col in range(n):
            matrix[0][col] = 0
    if first_col_has_zero:
        for row in range(m):
            matrix[row][0] = 0


def main():
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    set_zeroes(matrix)
    print(matrix)


if __name__ == "__main__":
    main()

"""
Time complexity for all three progression is O(m * n).

Space: O(1) for modification in place and using the first row and first col to keep track of zeros instead of 
zeroes_row and zeroes_col
"""
