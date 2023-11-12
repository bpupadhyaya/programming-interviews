// You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
// You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
// DO NOT allocate another 2D matrix and do the rotation.
// Example:
// Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
// Output: [[7,4,1],[8,5,2],[9,6,3]]
// Note: visualize to understand
// Tag: 36/150

import java.util.Arrays;
class ImageRotation {
    public static void main(String[] args) {
        int[][] matrix = {
                {1,2,3},
                {4,5,6},
                {7,8,9}
        };
        rotate(matrix);
        for (int[] row: matrix)
            System.out.println(Arrays.toString(row));
    }

    static void rotate(int[][] matrix) {
        int n = matrix.length, depth = n/2;
        for (int i = 0; i < depth; i++) {
            int len = n - 2 * i - 1, opp = n - 1 - i;
            for (int j = 0; j < len; j++) {
                int temp = matrix[i][i+j];
                matrix[i][i+j] = matrix[opp-j][i];
                matrix[opp-j][i] = matrix[opp][opp-j];
                matrix[opp][opp-j] = matrix[i+j][opp];
                matrix[i+j][opp] = temp;
            }
        }
    }
}
