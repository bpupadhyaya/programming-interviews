// Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
// You must do it in place.
// Example:
// Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
// Output: [[1,0,1],[0,0,0],[1,0,1]]
// Note: Visualize to understand
// Tag: 37/150

import java.util.Arrays;
class SettingMatrixElemToZeroes {
    public static void main(String[] args) {
        int[][] matrix = {
                {1,1,1},
                {1,0,1},
                {1,1,1}
        };

        setZeroes(matrix);
        for(int[] row: matrix)
            System.out.println(Arrays.toString(row));
    }

    static void setZeroes(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        int rowsArray[] = new int[m];
        int colsArray[] = new int[n];

        Arrays.fill(rowsArray, 1);
        Arrays.fill(colsArray, 1);

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
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

// Method:
// we can use two separate arrays one for rows (rowsArray) and one for columns (colsArray) and initialize them to 1
// while traversing the given matrix whenever we encounter 0 at (i,j), we will set rowsArray[i]=0 and colsArray[j]=0
// After completion of step 2, again iterate through the matrix and for any (i,j), if rowsArray[i] or colsArray[j]
// is 0 then update matrix[i][j] to 0.
// Complexity:
// Time complexity ~ O(mn)
// Space complexity ~ O(m+n)