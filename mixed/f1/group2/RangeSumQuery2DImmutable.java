// Given a 2D matrix matrix, handle multiple queries of the following type:
// Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and
// lower right corner (row2, col2).
// Implement the NumMatrix class:
// NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
// int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle
// defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
// You must design an algorithm where sumRegion works on O(1) time complexity.
// Sample 1:
// Input
// ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
// [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
// Output
// [null, 8, 11, 12]
// Explanation:
// NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
// numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the rectangle (visualize matrix to understand))
// numMatrix.sumRegion(1, 1, 2, 2); // return 11 (visualize)
// numMatrix.sumRegion(1, 2, 2, 4); // return 12 (visualize)

class NumMatrix {
    private int[][] sums;
    public NumMatrix(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        sums = new int[m+1][n+1];
        for (int i = 1; i <= m; i++)
            for (int j = 1; j <=n; j++)
                sums[i][j] = sums[i-1][j] + sums[i][j-1] + matrix[i-1][j-1] - sums[i-1][j-1];
    }
    public int sumRegion(int row1, int col1, int row2, int col2) {
        int redRectangle = sums[row2+1][col2+1]; // visual reference for color
        int purpleRectangle =sums[row1][col2+1] + sums[row2+1][col1];
        int blueRectangle = sums[row1][col1];
        return redRectangle - purpleRectangle + blueRectangle;
    }
}

class RangeSumQuery2DImmutable {
    public static void main(String...args) {
        int[][] numMatrix = {
                {3,0,1,4,2},
                {5,6,3,2,1},
                {1,2,0,1,5},
                {4,1,0,1,7},
                {1,0,3,0,5}
        };
        int row1 = 2, col1 = 1, row2 = 4, col2 = 3;
        NumMatrix obj = new NumMatrix(numMatrix);
        int regSum = obj.sumRegion(row1, col1, row2, col2);
        System.out.println("Region sum: " + regSum);

        row1 = 1; col1 = 1; row2 = 2; col2 = 2;
        regSum = obj.sumRegion(row1, col1, row2, col2);
        System.out.println("Region sum: " + regSum);

    }
}
