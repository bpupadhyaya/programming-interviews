"""
Given a 2D matrix matrix, handle multiple queries of the following types:

Update the value of a cell in matrix.
Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1)
and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
void update(int row, int col, int val) Updates the value of matrix[row][col] to be val.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the
 rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Example:
Input
["NumMatrix", "sumRegion", "update", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3],
[3, 2, 2], [2, 1, 4, 3]]
Output
[null, 8, null, 10]

Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7],
[1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e. sum of the left red rectangle)
numMatrix.update(3, 2, 2);       // matrix changes from left image to right image
numMatrix.sumRegion(2, 1, 4, 3); // return 10 (i.e. sum of the right red rectangle)

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
-1000 <= matrix[i][j] <= 1000
0 <= row < m
0 <= col < n
-1000 <= val <= 1000
0 <= row1 <= row2 < m
0 <= col1 <= col2 < n
At most 5000 calls will be made to sumRegion and update.

R138/145
"""


class NumMatrix:
    def create_prefix_sum(self, row):
        prefix_sum = []
        sum = 0
        for val in row:
            sum += val
            prefix_sum.append(sum)
        return prefix_sum

    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix
        self.row_prefix_sum = []
        for row in matrix:
            prefix_sum = self.create_prefix_sum(row)
            self.row_prefix_sum.append(prefix_sum)

    def update(self, row: int, col: int, val: int) -> None:
        if row < 0 or row >= len(self.matrix):
            return
        if col < 0 or col >= len(self.matrix[0]):
            return
        self.matrix[row][col] = val
        # Update prefix sum
        self.row_prefix_sum[row] = self.create_prefix_sum(self.matrix[row])

    def sum_region(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Iterate through row1 to row2
        sum = 0
        for r in range(row1, row2+1):
            # Calculate prefix[col2] - prefix[col1] (this sum)
            if col1 == 0:
                sum += self.row_prefix_sum[r][col2]
            else:
                sum += self.row_prefix_sum[r][col2] - self.row_prefix_sum[r][col1-1]
        return sum


def main():
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    obj = NumMatrix(matrix)
    row1, col1, row2, col2 = 2, 1, 4, 3
    print(obj.sum_region(row1, col1, row2, col2))
    row, col, val = 3, 2, 2
    print(obj.update(row, col, val))
    row1, col1, row2, col2 = 2, 1, 4, 3
    print(obj.sum_region(row1, col1, row2, col2))


if __name__ == "__main__":
    main()
