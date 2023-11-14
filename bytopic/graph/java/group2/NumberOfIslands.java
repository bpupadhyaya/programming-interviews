// Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
// An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all
// four edges of the grid are all surrounded by water.
// Sample 1:
// Input: grid = [
//  ["1","1","0","0","0"],
//  ["1","1","0","0","0"],
//  ["0","0","1","0","0"],
//  ["0","0","0","1","1"]
// ]
// Output: 3
//
// Tag: 89/150
// Tag: 200/2927, R23/2936 (overall frequency ranking)
class NumberOfIslands {
    private static int m;
    private static int n;
    public static void main(String...args) {
        char[][] grid = {
                {'1','1','0','0','0'},
                {'1','1','0','0','0'},
                {'0','0','1','0','0'},
                {'0','0','0','1','1'}
        };

        System.out.println("Number of islands: " + numOfIslands(grid));
    }

    static int numOfIslands(char[][] grid) {
        int count = 0;
        n = grid.length;
        if (n == 0)
            return 0;
        m = grid[0].length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++)
                if (grid[i][j] == '1') {
                    dfsMarking(grid, i, j);
                    ++count;
                }
        }
        return count;
    }

    private static void dfsMarking(char[][] grid, int i, int j) {
        if ( i < 0 || j < 0 || i >= n || j >= m || grid[i][j] != '1')
            return;
        grid[i][j] = '0';
        dfsMarking(grid, i+1, i);
        dfsMarking(grid, i-1, j);
        dfsMarking(grid, i, j+1);
        dfsMarking(grid, i, j-1);
    }
}