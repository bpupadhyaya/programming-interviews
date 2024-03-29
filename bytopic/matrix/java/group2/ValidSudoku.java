// Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the
// following rules:
// 1. Each row must contain the digits 1-9 without repetition.
// 2. Each column must contain the digits 1-9 without repetition.
// 3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
// Note:
// A Sudoku board (partially filled) could be valid but is not necessarily solvable.
// Only the filled cells need to be validated according to the mentioned rules.
// Example:
// Input: board =
//  [["8","3",".",".","7",".",".",".","."]
//  ,["6",".",".","1","9","5",".",".","."]
//  ,[".","9","8",".",".",".",".","6","."]
//  ,["8",".",".",".","6",".",".",".","3"]
//  ,["4",".",".","8",".","3",".",".","1"]
//  ,["7",".",".",".","2",".",".",".","6"]
//  ,[".","6",".",".",".",".","2","8","."]
//  ,[".",".",".","4","1","9",".",".","5"]
//  ,[".",".",".",".","8",".",".","7","9"]]
//Output: false
//Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there
// are two 8's in the top left 3x3 sub-box, it is invalid.
//
// Tag: 34/150
// Tag: 36/2927, R168/2936 (overall frequency ranking)

import java.util.HashSet;
import java.util.Set;
class SudokuValidation {
    public static void main(String...args) {
        char[][] board = {
                {'8','3','.','.','7','.','.','.','.'},
                {'6','.','.','1','9','5','.','.','.'},
                {'.','9','8','.','.','.','.','6','.'},
                {'8','.','.','.','6','.','.','.','3'},
                {'4','.','.','8','.','3','.','.','1'},
                {'7','.','.','.','2','.','.','.','6'},
                {'.','6','.','.','.','.','2','8','.'},
                {'.','.','.','4','1','9','.','.','5'},
                {'.','.','.','.','8','.','.','7','9'}
        };

        System.out.println("Is valid? " + isValidSudoku(board));
    }

    static boolean isValidSudoku(char[][] board) {
        Set seen = new HashSet();
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char number = board[i][j];
                if (number != '.')
                    if (!seen.add(number + " in row " + i) ||
                            !seen.add(number + "in column " + j) ||
                            !seen.add(number + "in block " + i/3 + "-" + j/3))
                        return false;
            }
        }
        return true;
    }
}