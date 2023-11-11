// Given an m x n matrix, return all elements of the matrix in spiral order.
// Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
// Output: [1,2,3,6,9,8,7,4,5]
// Note: Visualize to understand
// Tag: 35/150

import java.util.ArrayList;
import java.util.List;
class SpiralMatrix {
    public static void main(String[] args) {
        int[][] matrix = {
                {1,2,3},
                {4,5,6},
                {7,8,9}
        };

        System.out.println("Spiral order: " + spiralOrder(matrix));
    }

    static List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();
        if (matrix == null || matrix.length == 0) {
            return result;
        }
        int rows = matrix.length, cols = matrix[0].length;
        int left = 0, right = cols - 1, top = 0, bottom = rows - 1;

        while (left <= right && top <= bottom) {
            for (int i = left; i <= right; i++) {
                result.add(matrix[top][i]);
            }
            top++;

            for (int i = top; i <= bottom; i++) {
                result.add(matrix[i][right]);
            }
            right--;

            if (top <= bottom) {
                for (int i = right; i >= left; i--) {
                    result.add(matrix[bottom][i]);
                }
                bottom--;
            }

            if (left <= right) {
                for (int i = bottom; i >= top; i--) {
                    result.add(matrix[i][left]);
                }
                left++;
            }
        }

        return result;
    }
}

// Logic/approach:
// -Use a while loop to traverse the matrix in a clockwise spiral order.
// -Define four variables: left, right, top, bottom to represent the four boundaries of the current spiral.
// -Use four for loops to traverse each edge of the current spiral in clockwise order and add the elements to
// the result list.
// -Update the boundaries of the current spiral and continue the process until all elements have been traversed.
//
// Steps:
// -We start with the outermost layer of the matrix and traverse it in a clockwise spiral order, adding the
// elements to the result list.
// -Then we move on to the next inner layer of the matrix and repeat the process until we have traversed all layers.
// -To traverse each layer, we need to keep track of the four boundaries of the current spiral.
// -We start at the top-left corner of the current spiral and move right until we hit the top-right corner.
// -Then we move down to the bottom-right corner and move left until we hit the bottom-left corner.
// -Finally, we move up to the top-left corner of the next spiral and repeat the process until we have traversed
// all elements in the matrix.