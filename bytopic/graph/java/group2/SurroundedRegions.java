// Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
// A region is captured by flipping all 'O's into 'X's in that surrounded region.
// Example:
// Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
// Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
// Explanation: Notice that an 'O' should not be flipped if:
// - It is on the border, or
// - It is adjacent to an 'O' that should not be flipped.
// The bottom 'O' is on the border, so it is not flipped.
// The other three 'O' form a surrounded region, so they are flipped.
//
// Tag: 90/150
// Tag: 130/2927, R804/2936 (overall frequency ranking)

import java.util.Arrays;
class SurroundedRegions {
    public static void main(String...args) {
        char[][] board = {
                {'X','X','X','X'},
                {'X','0','0','X'},
                {'X','X','0','X'},
                {'X','0','X','X'}
        };

        solve(board);
        for (char[] row: board)
            System.out.print(Arrays.toString(row));
        System.out.println();
    }

    static void solve(char[][] board) {
        if (board.length == 0 || board[0].length ==0)
            return;
        if (board.length < 2 || board[0].length < 2)
            return;
        int m = board.length, n = board[0].length;
        // Any '0' connected to a boundry can't be turned to 'X'
        // Start from first and last column, turn 'O' to '*'.
        for (int i = 0; i < m; i++) {
            if (board[i][0] == '0')
                boundryDFS(board, i, 0);
            if (board[i][n-1] == '0')
                boundryDFS(board, i, n-1);
        }
        // Start from first and last row, turn '0' to '*'
        for (int j = 0; j < n; j++) {
            if (board[0][j] == '0')
                boundryDFS(board, 0, j);
            if (board[m-1][j] == '0')
                boundryDFS(board, m-1, j);
        }

        // Post-prcessing, turn 'O' to 'X', '*' back to 'O', keep 'X' intact.
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == '0')
                    board[i][j] = 'X';
                else if (board[i][j] == '*')
                    board[i][j] = '0';
            }
        }
    }

    private static void boundryDFS(char[][] board, int i, int j) {
        if (i < 0 || i > board.length -1 || i < 0 || j > board[0].length - 1)
            return;
        if (board[i][j] == '0')
            board[i][j] = '*';
        if (i > 1 && board[i-1][j] == '0')
            boundryDFS(board, i-1, j);
        if (i < board.length - 2 && board[i+1][j] == '0')
            boundryDFS(board, i+1, j);
        if (j > 1 && board[i][j-1] == '0')
            boundryDFS(board, i, j-1);
        if (j < board[i].length -2 && board[i][j+1] == '0')
            boundryDFS(board, i, j+1);
    }
}