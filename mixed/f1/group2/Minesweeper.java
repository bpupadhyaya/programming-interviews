// Let's play the minesweeper game (Wikipedia, online game)!
// You are given an m x n char matrix board representing the game board where:
// 'M' represents an unrevealed mine,
// 'E' represents an unrevealed empty square,
// 'B' represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),
// digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
// 'X' represents a revealed mine.
// You are also given an integer array click where click = [clickr, clickc] represents the next click position among all the
// unrevealed squares ('M' or 'E').
// Return the board after revealing this position according to the following rules:
// If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
// If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B' and all of its adjacent
// unrevealed squares should be revealed recursively.
// If an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
// Return the board when no more squares will be revealed.
// Sample 1:
// Input: board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0]
// Output: [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]

class Minesweeper {
    public static void main(String...args) {
        char[][] board = {
                {},
                {},
                {},
                {}
        };
        int[] click = {3,0};
        char[][] updatedBoard = updateBoard(board, click);
        for (int i = 0; i < updatedBoard.length; i++) {
            for (int j = 0; j < updatedBoard[0].length; j++) {
                System.out.print(updatedBoard[i][j] + ",");
            }
            System.out.println();
        }
    }

    static char[][] updateBoard(char[][] board, int[] click) {
        if (board[click[0]][click[1]] == 'M') {
            board[click[0]][click[1]] = 'X';
            return board;
        }
        reveal(board, click[0], click[1]);
        return board;
    }

    private static void reveal(char[][] board, int i, int j) {
        if (i < 0 || j < 0 || i >= board.length || j >= board[0].length || board[i][j] != 'E')
            return;

        board[i][j] = '0';
        int[][] neighbors = {
                {i-1, j-1},{i-1,j},{i-1,j+1},
                {i,j-1},{i,j+1},
                {i+1,j-1},{i+1,j},{i+1,j+1}
        };

        for (int[] neighbor : neighbors) {
            if (neighbor[0] < 0 || neighbor[1] < 0 || neighbor[0] >= board.length || neighbor[1] >= board[0].length)
                continue;
            if (board[neighbor[0]][neighbor[1]] == 'M')
                board[i][j]++;
        }
        if (board[i][j] != 0)
            return;

        board[i][j] = 'B';
        for (int[] neighbor: neighbors)
            reveal(board, neighbor[0], neighbor[1]);
    }
}