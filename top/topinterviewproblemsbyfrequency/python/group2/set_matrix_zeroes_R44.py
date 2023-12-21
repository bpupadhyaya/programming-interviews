"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

Example:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Note: Visualize to understand

Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-2^{31} <= matrix[i][j] <= 2^{31} - 1

Follow up:
A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

Tag: R44/145
"""


def set_zeroes(matrix: list[list[int]]) -> None:
    # Space O(m+n)
    if not matrix:
        return []

    m = len(matrix)
    n = len(matrix[0])

    zeroes_row = [False] * m
    zeroes_col = [False] * n
    for row in range(m):
        for col in range(n):
            if matrix[row][col] == 0:
                zeroes_row[row] = True
                zeroes_col[col] = True
    for row in range(m):
        for col in range(n):
            if zeroes_row[row] or zeroes_col[col]:
                matrix[row][col] = 0


def set_zeroes_1(matrix: list[list[int]]) -> None:
    # Space O(1)
    m = len(matrix)
    n = len(matrix)

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
Note on implementation for O(1) space:
Most optimized using O(1) space: But, we can do even better, O(1) - initial ask of the problem. What if instead of 
having a separate array to track the zeroes, we simply use the first row or col to track them and then go back 
to update the first row and col with zeroes after we're done replacing it? The approach to get constant space is 
to use first row and first col of the matrix as a tracker.

At each row or col, if you see a zero, then mark the first row or first col as zero with the current row and col.
Then iterate through the array again to see where the first row and col were marked as zero and then set 
that row/col as 0.
After doing that, you'll need to traverse through the first row and/or first col if there were any zeroes there 
to begin with and set everything to be equal to 0 in the first row and/or first col.
Time complexity for all three progression is O(m * n).

Space: O(1) for modification in place and using the first row and first col to keep track of zeros instead of 
zeroes_row and zeroes_col

Note on O(m+n) space implementation:
Note: m = number of rows, n = number of cols

Brute force using O(m*n) space: The initial approach is to start with creating another matrix to store the result. 
From doing that, you'll notice that we want a way to know when each row and col should be changed to zero. 
We don't want to prematurely change the values in the matrix to zero because as we go through it, we might change 
a row to 0 because of the new value.

More optimized using O(m + n) space: To do better, we want O(m + n). How do we go about that? Well, we really
 just need a way to track if any row or any col has a zero, because then that means the entire row or col has to 
 be zero. Ok, well, then we can use an array to track the zeroes for the row and zeros for the col. Whenever we see 
 a zero, just set that row or col to be True.

Space: O(m + n) for the zeroes_row and zeroes_col array
"""