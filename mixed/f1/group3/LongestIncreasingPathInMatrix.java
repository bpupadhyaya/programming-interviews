// Given an m x n integers matrix, return the length of the longest increasing path in matrix.
// Sample 1:
// Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
// Output: 4
// Explanation: Visualize, the longest increasing path is [1, 2, 6, 9].

class LongestIncreasingPathInMatrix {
    private static final int[][] dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    public static void main(String...args) {
        int[][] myMatrix = {{9,9,4},{6,6,8},{2,1,1}};
        System.out.println("Length of longest...: " + findLengthOfLongestIncreasingPathInMatrix(myMatrix));
    }

    static int findLengthOfLongestIncreasingPathInMatrix(int[][] mat) {
        if (mat.length == 0)
            return 0;
        int m = mat.length, n = mat[0].length;
        int[][] cache = new int[m][n];
        int max = 1;
        for(int i = 0; i < m; i++) {
            for (int j = 0; j <n; j++) {
                int len = dfs(mat, i, j, m, n, cache);
                max = Math.max(max, len);
            }
        }
        return max;
    }

    private static int dfs(int[][] matrix, int i, int j, int m, int n, int[][] cache) {
        if (cache[i][j] != 0)
            return cache[i][j];
        int max = 1;
        for (int[] dir: dirs) {
            int x = i + dir[0], y = j + dir[1];
            if (x < 0 || x >= m || y < 0 || y >= n || matrix[x][y] <= matrix[i][j])
                continue;
            int len = 1 + dfs(matrix, x, y, m, n, cache);
            max = Math.max(max, len);
        }
        cache[i][j] = max;

        return max;
    }
}

// Algo:
// 1. Do DFS from every cell
// 2. Compare every 4 direction and skip cells that are out of boundary or smaller
// 3. Get matrix max from every cell's max
// 4. Use matrix[x][y] <= matrix[i][j] so we don't need a visited[m][n] array
// 5. The key is to cache the distance because it's highly possible to revisit a cell