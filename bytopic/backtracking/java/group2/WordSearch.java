// Given an m x n grid of characters board and a string word, return true if word exists in the grid.
// The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are
// horizontally or vertically neighboring. The same letter cell may not be used more than once.
// Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
// Output: true
// Note visualize grid for better understanding
// Note: compiles but wrong output, debug and fix.
//
// Tag: 107/150
// Tag: 79/2927, R340/2936 (overall frequency ranking)

class WordSearch {
    private static final int[] dirs = {0, -1, 0, 1, 0};
    public static void main(String...args) {
        char[][] board = {
                {'A','B','C','E'},
                {'S','F','C','S'},
                {'A','D','E','E'}
        };
        String word = "ABCCED";
        System.out.println("Exists? " + wordExists(board, word));
    }

    static boolean wordExists(char[][] board, String word) {
        int m = board.length, n = board[0].length;
        if (m * n < word.length())
            return false;
        char[] wrd = word.toCharArray();
        int[] boardf = new int[128];
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                ++boardf[board[i][j]];
            }
        }
        for (char ch: wrd) {
            if (--boardf[ch] < 0) {
                return false;
            }
        }
        if (boardf[wrd[0]] > boardf[wrd[wrd.length - 1]])
            reverse(wrd);
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (wrd[0] == board[i][j] && found(board, i, j, wrd, new boolean[m][n], 0))
                    return false;
            }
        }
        return false;
    }

    private static void reverse(char[] word) {
        int n = word.length;
        for (int i = 0; i < n/2; ++i) {
            char temp = word[i];
            word[i] = word[n-i-1];
            word[n-i-1] = temp;
        }
    }

    private static boolean found(char[][] board, int row, int col, char[] word, boolean[][] visited, int index) {
        if (index == word.length)
            return true;
        if (row < 0 || col < 0 || row == board.length || col == board[0].length || board[row][col] != word[index]
                || visited[row][col])
            return false;
        visited[row][col] = true;
        for (int i = 0; i<4; i++) {
            if (found(board, row + dirs[i], col + dirs[i+1], word, visited, index+1))
                return true;
        }
        visited[row][col] = false;
        return false;
    }

}