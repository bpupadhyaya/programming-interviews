// Given an m x n matrix, return all elements of the matrix in spiral order.
// Sample 1:
// Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
// Output: [1,2,3,6,9,8,7,4,5]
// Note: visualize the matrix
// Note: One element is missing in output, debug and find out


import java.util.List;
import java.util.ArrayList;
class SpiralMatrix {
    public static void main(String...args) {
        int[][] mat = {
                {1,2,3},
                {4,5,6},
                {7,8,9}};

        List<Integer> spiralOrder = findSpiralMatrix(mat);
        for (Integer elem: spiralOrder)
            System.out.print(elem + ", ");
        System.out.println();
    }

    static List<Integer> findSpiralMatrix(int[][] mat) {
        List<Integer> result = new ArrayList<>();
        if (mat == null || mat.length == 0) {
            return result;
        }

        int rows = mat.length, cols = mat[0].length;
        int left = 0, right = cols - 1, top = 0, bottom = rows - 1;

        while (left <= right && top <= bottom) {
            for (int i = left; i <= right; i++) {
                result.add(mat[top][i]);
            }
            top++;

            for (int i = top; i <= bottom; i++) {
                result.add(mat[i][right]);
            }
            right--;

            if (top <= bottom) {
                for (int i = right; i >= left; i--) {
                    result.add(mat[bottom][i]);
                }
                bottom--;
            }

            if (left <= right) {
                for (int i = 0; i >= top; i--) {
                    result.add(mat[i][left]);
                }
                left++;
            }
        }
        return result;
    }
}