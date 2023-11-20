// Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
// Example:
// Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
// Output: 4
// Note: Visualize to understand
//
// Tag: 150/150
// Tag: 221/2927, R428/2936 (overall frequency ranking)

class MaximalSquare {
    public static void main(String[] args) {
        char[][] matrix = {
                {'1','0','1','0','0'},
                {'1','0','1','1','1'},
                {'1','1','1','1','1'},
                {'1','0','0','1','0'}
        };

        System.out.println("Maximal square: " + maximalSquare(matrix));
    }

    static int maximalSquare(char[][] matrix) {
        int r = matrix.length;
        if (r == 0) return 0;
        int c = matrix[0].length, edge = 0;
        int[][] dp = new int[r+1][c+1];
        for (int i = 1; i <= r; i++)
            for (int j = 1; j <= c; j++) {
                if (matrix[i-1][j-1] == '0') continue;
                dp[i][j] = 1 + Math.min(dp[i-1][j], Math.min(dp[i-1][j-1], dp[i][j-1]));
                edge = Math.max(edge, dp[i][j]);
        }

        return edge * edge;
    }
}

// Complexity
// O(mn)?