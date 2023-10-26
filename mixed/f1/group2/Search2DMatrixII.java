// Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the
// following properties:
// Integers in each row are sorted in ascending from left to right.
// Integers in each column are sorted in ascending from top to bottom.
// Sample 1:
// Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
// Output: true
// Note: Program has bug, produces wrong result, debug and fix it.

class Search2DMatrixII {
    public static void main(String...args) {
        int[][] matrix = {
                {1,4,7,11,15},
                {2,5,8,12,19},
                {3,6,9,16,22},
                {10,13,14,17,24},
                {18,21,23,26,30}
        };
        int target = 5;

        System.out.println("Found? " + searchMatrix(matrix, target));
    }

    static boolean searchMatrix(int[][] matrix, int target) {
        int row = 0;
        int col = matrix[0].length - 1;

        while (col >= 0 && row < matrix.length) {
            if (matrix[row][col] == target)
                return true;

            if (matrix[row][col] < target)
                row++;
            else
                col--;
        }
        return true;
    }
}