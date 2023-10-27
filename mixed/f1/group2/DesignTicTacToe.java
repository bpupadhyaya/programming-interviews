// Assume the following rules are for the tic-tac-toe game on an n x n board between two players:
// 1. A move is guaranteed to be valid and is placed on an empty block.
// 2. Once a winning condition is reached, no more moves are allowed.
// 3. A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
//
// Implement the TicTacToe class:
// TicTacToe(int n) Initializes the object the size of the board n.
// int move(int row, int col, int player) Indicates that the player with id player plays at the cell (row, col) of the board.
// The move is guaranteed to be a valid move, and the two players alternate in making moves. Return
// 0 if there is no winner after the move,
// 1 if player 1 is the winner after the move, or
// 2 if player 2 is the winner after the move.
// Sample 1:
// Input
//["TicTacToe", "move", "move", "move", "move", "move", "move", "move"]
//[[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
//Output
//[null, 0, 0, 0, 0, 0, 0, 1]
// Note: Explanation below, after the code
// Note: Debug the output and make sure it is correct based on above specification, explanation proved below, after the code.

class TicTacToe {
    int[][] count;
    public TicTacToe(int n) {
        count = new int[6*n][3];
    }

    public int move(int row, int col, int player) {
        int n = count.length / 6;
        for (int x: new int[]{row, n+col, 2*n+row+col, 5*n+row-col})
            if (++count[x][player] == n)
                return player;
        return 0;
    }

}

class DesignTicTacToe {
    public static void main(String...args) {
        int[][] count = {
                {0, 0, 1},
                {0, 2, 2},
                {2, 2, 1},
                {1, 1, 2},
                {2, 0, 1},
                {1, 0, 2},
                {2, 1, 1}
        };
        TicTacToe t = new TicTacToe(7);
        System.out.println("Move: 2,1,1: " + t.move(2,1,1));
    }
}

//Explanation
//TicTacToe ticTacToe = new TicTacToe(3);
//Assume that player 1 is "X" and player 2 is "O" in the board.
//ticTacToe.move(0, 0, 1); // return 0 (no one wins)
//|X| | |
//| | | |    // Player 1 makes a move at (0, 0).
//| | | |
//
//ticTacToe.move(0, 2, 2); // return 0 (no one wins)
//|X| |O|
//| | | |    // Player 2 makes a move at (0, 2).
//| | | |
//
//ticTacToe.move(2, 2, 1); // return 0 (no one wins)
//|X| |O|
//| | | |    // Player 1 makes a move at (2, 2).
//| | |X|
//
//ticTacToe.move(1, 1, 2); // return 0 (no one wins)
//|X| |O|
//| |O| |    // Player 2 makes a move at (1, 1).
//| | |X|
//
//ticTacToe.move(2, 0, 1); // return 0 (no one wins)
//|X| |O|
//| |O| |    // Player 1 makes a move at (2, 0).
//|X| |X|
//
//ticTacToe.move(1, 0, 2); // return 0 (no one wins)
//|X| |O|
//|O|O| |    // Player 2 makes a move at (1, 0).
//|X| |X|
//
//ticTacToe.move(2, 1, 1); // return 1 (player 1 wins)
//|X| |O|
//|O|O| |    // Player 1 makes a move at (2, 1).
//|X|X|X|