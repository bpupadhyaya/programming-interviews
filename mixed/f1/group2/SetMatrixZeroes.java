// Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
// You must do it in place.
// Sample 1:
// Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
// Output: [[1,0,1],[0,0,0],[1,0,1]]
// Note: visualize to understand

import java.util.Arrays;
class SetMatrixZeroes {
    public static void main(String...args) {
        int[][] matrix = {
                {1,1,1},
                {1,0,1},
                {1,1,1}
        };

        setMatrixZeroes(matrix);
        for (int i = 0; i < matrix.length; i++) {
            System.out.print("{");
            for (int j = 0; j < matrix[0].length; j++) {
                System.out.print(matrix[i][j] + ", ");
            }
            System.out.println("}");
        }
    }

    static void setMatrixZeroes(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        int rowsArray[] = new int[m];
        int colsArray[] = new int[n];

        Arrays.fill(rowsArray, 1);
        Arrays.fill(colsArray, 1);

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++){
                if (matrix[i][j] == 0) {
                    rowsArray[i] = 0;
                    colsArray[j] = 0;
                }
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (rowsArray[i] == 0 || colsArray[j] == 0)
                    matrix[i][j] = 0;
            }
        }
    }

}