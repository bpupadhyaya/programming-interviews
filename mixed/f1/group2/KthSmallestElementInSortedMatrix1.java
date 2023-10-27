// Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest
// element in the matrix.
// Note that it is the kth smallest element in the sorted order, not the kth distinct element.
// You must find a solution with a memory complexity better than O(n^2).
// Sample 1:
// Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
// Output: 13
// Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
// Soln: Time complexity: n * log(k)
// Auxiliary space complexity: O(k)

import java.util.PriorityQueue;
import java.util.Collections;
class KthSmallestElementInSortedMatrix1 {
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
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        int n = matrix.length;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (pq.size() < k) {
                    pq.add(matrix[i][j]);
                } else { // equal to k
                    if (matrix[i][j] < pq.peek()) { // if incoming element is less than peek
                        pq.poll();
                        pq.add(matrix[i][j]);
                    }
                }
            }
        }

        return pq.peek();
    }
}