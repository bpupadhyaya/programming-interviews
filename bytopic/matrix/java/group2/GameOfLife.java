// According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton
// devised by the British mathematician John Horton Conway in 1970."
// The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1)
// or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal)
// using the following four rules (taken from the above Wikipedia article):
// 1. Any live cell with fewer than two live neighbors dies as if caused by under-population.
// 2. Any live cell with two or three live neighbors lives on to the next generation.
// 3. Any live cell with more than three live neighbors dies, as if by over-population.
// 4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
// The next state is created by applying the above rules simultaneously to every cell in the current state, where
// births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.
// Example 1:
// Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
// Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
// Note: Visualize to understand
// Example 2:
// Input: board = [[1,1],[1,0]]
// Output: [[1,1],[1,1]]
// Note: Visualize to understand
// Tag: 38/150
// Note: program compiles but the output is not correct, debug and fix.

import java.util.Arrays;
class GameOfLife {
    public static void main(String[] args) {
       int[][] board = {
               {0,1,0},
               {0,0,1},
               {1,1,1},
               {0,0,0}
       };

       gameOfLife(board);
       for (int[] row: board)
           System.out.println(Arrays.toString(row));
    }

    static void gameOfLife(int[][] board) {
        if (board == null || board.length == 0) return;
        int m = board.length, n = board[0].length;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int lives = liveNeighbors(board, m, n, i, j);

                // In the beginning, eery 2nd bit is 0.
                // So we only need to care about when will the 2nd bit becomes 1.
                if (board[i][j] == 1 && lives >= 2 && lives <= 3) {
                    board[i][j] = 3; // Make the 2nd bit 1: 01 -> 11
                }
                if (board[i][j] == 0 && lives == 3) {
                    board[i][j] = 2; // Make the 2nd bit 1: 00 -> 10
                }
            }
        }

        for(int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                board[i][j] >>= 1; // Get the 2nd state.
            }
        }
    }

    private static int liveNeighbors(int[][] board, int m, int n, int i, int j) {
        int lives = 0;
        for (int x = Math.max(i-1, 0); x <= Math.min(i+1, m-1); x++) {
            for (int y = Math.max(j-1, 0); y < Math.min(j+1, n-1); y++) {
                lives += board[x][y] & 1;
            }
        }
        lives -= board[i][j] & 1;
        return lives;
    }
}