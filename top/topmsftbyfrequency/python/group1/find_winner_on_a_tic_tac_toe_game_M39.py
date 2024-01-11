"""
Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:

Players take turns placing characters into empty squares ' '.
The first player A always places 'X' characters, while the second player B always places 'O' characters.
'X' and 'O' characters are always placed into empty squares, never on filled ones.
The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on
 grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return
  "Draw". If there are still movements to play return "Pending".

You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and
A will play first.

Example:
Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: A wins, they always play first.

Constraints:
1 <= moves.length <= 9
moves[i].length == 2
0 <= rowi, coli <= 2
There are no repeated elements on moves.
moves follow the rules of tic tac toe.

Tag: M39/50
"""


def tictactoe(moves: list[list[int]]) -> int:
    A = [0]*8
    B = [0]*8
    for i in range(len(moves)):
        r, c = moves[i]
        player = A if i % 2 == 0 else B
        player[r] += 1
        player[c+3] += 1
        if r == c:
            player[6] += 1
        if r == 2-c:
            player[7] += 1
    for i in range(8):
        if A[i] == 3:
            return "A"
        if B[i] == 3:
            return "B"

    return "Draw" if len(moves) == 9 else "Pending"


def main():
    moves = [[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]
    print(tictactoe(moves))


if __name__ == "__main__":
    main()

