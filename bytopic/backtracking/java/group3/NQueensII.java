// The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that
// no two queens attack each other.
// Given an integer n, return the number of distinct solutions to the n-queens puzzle.
// Example:
// Input: n = 4
// Output: 2
// Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
// Note: Find visuals to understand
//
// Tag: 105/150
// Tag: 52/2927, R1500/2936 (overall frequency ranking)

import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;

class NQueensII {
    public static void main(String...args) {
        int n = 4;
        System.out.println("Num. of distinct solutions: " + totalNQueens(n));
    }

    static int totalNQueens(int n) {
        char board[][] = new char[n][n];
        for(char[] c : board)
            Arrays.fill(c, '.');
        return dfs(0, board);
    }

    private static int dfs(int col, char board[][]) {
        if(col == board.length) return 1;
        int count = 0;
        for(int row = 0; row < board.length; row++){
            if(isSafe(board, row, col)){
                board[row][col] = 'Q';
                count += dfs(col + 1, board);
                board[row][col] = '.';
            }
        }
        return count;
    }

    private static boolean isSafe(char board[][], int row, int col) {
        int dupRow = row;
        int dupCol = col;

        while(row >= 0 && col >= 0){
            if(board[row][col] == 'Q') return false;
            row--;
            col--;
        }

        row = dupRow;
        col = dupCol;
        while(col >= 0){
            if(board[row][col] == 'Q') return false;
            col--;
        }

        row = dupRow;
        col = dupCol;
        while(col >= 0 && row < board.length){
            if(board[row][col] == 'Q') return false;
            row++;
            col--;
        }
        return true;
    }
}