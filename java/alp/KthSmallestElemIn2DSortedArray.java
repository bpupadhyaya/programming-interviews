// Given an n x n matrix, where every row and column is sorted in non-decreasing order.
// Find the kth smallest element in the given 2D array. Example, Input: k = 3 and
// array = [10, 20, 30, 40
//          15, 25, 35, 45
//          24, 29, 37, 48
//          32, 33, 39, 50]
// Output: 20

class KthSmallestElem {
    public static void main(String...args) {
        int k = 3;
        int[][] myData = {{10, 20, 30, 40},
                            {15, 25, 35, 45},
                            {24, 29, 37, 48},
                            {32, 33, 39, 50}};

        int myResult = kthSmallestElem(myData, k);
        System.out.println(myResult);
    }

    private static int kthSmallestElem(int[][] myMatrix, int k) {
        int m = myMatrix.length;
        int begin = myMatrix[0][0], end = myMatrix[m-1][m-1];
        while (begin < end) {
            int middle = begin + (end - begin) / 2;
            int[] smallestLargestPair = {myMatrix[0][0], myMatrix[m-1][m-1]};
            int count = countLessEq(myMatrix, middle, smallestLargestPair);
            if (count == k)
                return smallestLargestPair[0];
            if (count < k)
                begin = smallestLargestPair[1];
            else
                end = smallestLargestPair[0];
        }
        return begin;
    }

    private static int countLessEq(int[][] myMatrix, int middle, int[] smallestLargestPair) {
        int count = 0;
        int m = myMatrix.length, row = m - 1, column = 0;
        while (row >= 0 && column < m) {
            if (myMatrix[row][column] > middle) {
                smallestLargestPair[1] = Math.min(smallestLargestPair[1], myMatrix[row][column]);
                row--;
            } else {
                smallestLargestPair[0] = Math.max(smallestLargestPair[0], myMatrix[row][column]);
                count += row + 1;
                column++;
            }
        }
        return count;
    }
}