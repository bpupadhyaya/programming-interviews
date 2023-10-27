// Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest
// element in the matrix.
// Note that it is the kth smallest element in the sorted order, not the kth distinct element.
// You must find a solution with a memory complexity better than O(n^2).
// Sample 1:
// Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
// Output: 13
// Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
// Soln: Time complexity: O(n)
// Auxiliary space complexity: O(1)
// Soln: best performance among three solutions.

import java.util.Arrays;
class KthSmallestElementInSortedMatrix2 {
    public static void main(String...args) {
        int[][] matrix = {
                {1,5,9},
                {10,11,13},
                {12,13,15}
        };
        int k = 8;

        System.out.println("Kth smallest element: " + kthSmallest(matrix, k));
    }

    static int kthSmallest(int[][] matrix, int k) {
        int rows = matrix.length, cols = matrix[0].length;

        int lo = matrix[0][0], hi = matrix[rows-1][cols-1];
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            int count = 0, maxNum = lo;

            for (int r = 0, c = cols -1; r < rows; r++) {
                while(c >= 0 && matrix[r][c] > mid)
                    c--;
                if (c >= 0) {
                    // count of nums <= mid in matrix
                    count += (c+1);
                    // mid might be the value not in matrix, so we need to record the actual max num;
                    maxNum = Math.max(maxNum, matrix[r][c]);
                } else { // c < 0
                    break;
                }
            }
            // adjust search range
            if (count == k)
                return maxNum;
            else if (count < k)
                lo = mid + 1;
            else
                hi = mid - 1;
        }
        return lo;
    }
}