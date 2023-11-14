// You are given an m x n integer matrix matrix with the following two properties:
// Each row is sorted in non-decreasing order.
// The first integer of each row is greater than the last integer of the previous row.
// Given an integer target, return true if target is in matrix or false otherwise.
// You must write a solution in O(log(m * n)) time complexity.
// Sample 1:
// Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
// Output: false
//
// Tag: 115/150
// Tag: 74/2927, R236/2936 (overall frequency ranking)

class Search2DMatrix {
    public static void main(String...args) {
        int[][] matrix = {
                {1,3,5,7},
                {10,11,16,20},
                {23,30,34,60}
        };
        int target = 13;
        System.out.println("Search result: " + searchIn2DMatrix(matrix, target));
    }

    static boolean searchIn2DMatrix(int[][] matrix, int target) {
        int m = matrix.length;
        int n = matrix[0].length;
        int left = 0, right = m * n -1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            int mid_val = matrix[mid/n][mid % n];

            if (mid_val == target)
                return true;
            else if (mid_val < target)
                left = mid + 1;
            else right = mid - 1;
        }

        return false;
    }
}