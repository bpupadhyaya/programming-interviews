// Implement a basic elimination algorithm for Candy Crush.
// Rules:
// 1. If three or more candies of the same type are adjacent horizontally or vertically, crush them (empty them)
// 2. After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then
// these candies will drop until they hit a candy or bottom at the same time. No new candies drops outside
// the top boundry.
// 3. After the above steps, there may exist more candies that can be crushed. If so, repeat the above steps.
// 4. If there are no more candies that can be crushed, then return the current board.
// Given: m x n integer array board, b[i][j] represents the type of candy, b[i][j] == 0 means empty cell.

class CandyCrush {
    public static void main(String[] args) {
        int[][] board = {{5,4,1},{1,4,5},{1,1,1}};
        int[][] stableBoard = candyCrush(board);
        for (int i = 0; i < stableBoard.length; i++) {
            for (int j = 0; j < stableBoard[0].length; ++j) {
                System.out.print(stableBoard[i][j]+",");
            }
        }
        System.out.println();
    }

    private static int[][] candyCrush(int[][] b) {
        int row = b.length;
        int column = b[0].length;
        boolean contd = false;
        for(int i = 0; i < row; ++i) {
            for(int j = 0; j + 2 < column; ++j) {
                int data = Math.abs(b[i][j]);
                if (data != 0 && data == Math.abs(b[i][j+1]) && data == Math.abs(b[i][j+2])) {
                    b[i][j] = b[i][j+1] = b[i][j+2] = -data;
                    contd = true;
                }
            }
        }
        for(int i = 0; i+2 < row; ++i) {
            for(int j = 0; j < column; ++j) {
                int data = Math.abs(b[i][j]);
                if (data != 0 && data == Math.abs(b[i+1][j]) && data == Math.abs(b[i+2][j])) {
                    b[i][j] = b[i+1][j] = b[i+2][j] = -data;
                    contd = true;
                }
            }
        }
        for ( int j = 0; j < column; ++j) {
            int r = row - 1;
            for (int i = row -1; i >= 0; --i)
                if (b[i][j] > 0)
                    b[r--][j] = b[i][j];
            while (r >= 0)
                b[r--][j] = 0;
        }

        return contd ? candyCrush(b) : b;
    }
}